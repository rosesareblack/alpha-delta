#!/usr/bin/env python3
"""
FAERS Data Visualization and RSS Feed Generator
Creates visual comparisons of adverse event data and RSS feeds for monitoring
"""

import json
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from datetime import datetime
import xml.etree.ElementTree as ET
from xml.dom import minidom

def setup_matplotlib_for_plotting():
    """
    Setup matplotlib and seaborn for plotting with proper configuration.
    Call this function before creating any plots to ensure proper rendering.
    """
    import warnings
    import matplotlib.pyplot as plt
    import seaborn as sns

    # Ensure warnings are printed
    warnings.filterwarnings('default')  # Show all warnings

    # Configure matplotlib for non-interactive mode
    plt.switch_backend("Agg")

    # Set chart style
    plt.style.use("seaborn-v0_8")
    sns.set_palette("husl")

    # Configure platform-appropriate fonts for cross-platform compatibility
    # Must be set after style.use, otherwise will be overridden by style configuration
    plt.rcParams["font.sans-serif"] = ["Noto Sans CJK SC", "WenQuanYi Zen Hei", "PingFang SC", "Arial Unicode MS", "Hiragino Sans GB"]
    plt.rcParams["axes.unicode_minus"] = False

# FAERS Data from FDA Screenshots (Current as of 2025-10-28)
faers_data = {
    "ACETAMINOPHEN (G)": {
        "total_reports": 106183,
        "total_deaths": 1027,
        "total_life_threatening": 1021,
        "total_hospitalized": 17544,
        "active_ingredient": "Acetaminophen"
    },
    "IBUPROFEN (G)": {
        "total_reports": 63027,
        "total_deaths": 386,
        "total_life_threatening": 232,
        "total_hospitalized": 8945,
        "active_ingredient": "Ibuprofen"
    },
    "ADVIL (P)": {
        "total_reports": 30283,
        "total_deaths": 188,
        "total_life_threatening": 92,
        "total_hospitalized": 4380,
        "active_ingredient": "Ibuprofen"
    },
    "TOPAMAX (P)": {
        "total_reports": 26732,
        "total_deaths": 188,
        "total_life_threatening": 126,
        "total_hospitalized": 3968,
        "active_ingredient": "Topiramate"
    },
    "VYVANSE (P)": {
        "total_reports": 20950,
        "total_deaths": 44,
        "total_life_threatening": 172,
        "total_hospitalized": 3211,
        "active_ingredient": "Lisdexamfetamine"
    },
    "CONCERTA (P)": {
        "total_reports": 7605,
        "total_deaths": 61,
        "total_life_threatening": 31,
        "total_hospitalized": 1503,
        "active_ingredient": "Methylphenidate"
    },
    "STRATTERA (P)": {
        "total_reports": 6478,
        "total_deaths": 94,
        "total_life_threatening": 30,
        "total_hospitalized": 1570,
        "active_ingredient": "Atomoxetine"
    },
    "RITALIN (P)": {
        "total_reports": 2735,
        "total_deaths": 23,
        "total_life_threatening": 9,
        "total_hospitalized": 573,
        "active_ingredient": "Methylphenidate"
    }
}

def create_visual_comparisons():
    """Create comprehensive visual comparisons of FAERS data"""
    setup_matplotlib_for_plotting()
    
    # Convert to DataFrame
    df = pd.DataFrame(faers_data).T
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'drug_name'}, inplace=True)
    
    # Convert numeric columns to proper types
    numeric_cols = ['total_reports', 'total_deaths', 'total_life_threatening', 'total_hospitalized']
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col])
    
    # Calculate derived metrics
    df['death_rate'] = (df['total_deaths'] / df['total_reports'] * 100).round(3)
    df['serious_outcomes'] = df['total_deaths'] + df['total_life_threatening'] + df['total_hospitalized']
    df['serious_rate'] = (df['serious_outcomes'] / df['total_reports'] * 100).round(2)
    
    # Separate ADHD medications from pain medications
    adhd_drugs = df[df['drug_name'].isin(['VYVANSE (P)', 'CONCERTA (P)', 'STRATTERA (P)', 'RITALIN (P)'])].copy()
    pain_drugs = df[df['drug_name'].isin(['ACETAMINOPHEN (G)', 'IBUPROFEN (G)', 'ADVIL (P)'])].copy()
    other_drugs = df[df['drug_name'].isin(['TOPAMAX (P)'])].copy()
    
    # Create multiple visualization charts
    fig = plt.figure(figsize=(20, 24))
    
    # 1. Overall Total Reports Comparison
    plt.subplot(4, 2, 1)
    df_sorted = df.sort_values('total_reports', ascending=True)
    bars = plt.barh(df_sorted['drug_name'], df_sorted['total_reports'])
    plt.xlabel('Total Adverse Event Reports')
    plt.title('Total FAERS Reports by Drug (2025-10-28)', fontsize=14, fontweight='bold')
    plt.grid(axis='x', alpha=0.3)
    
    # Add value labels
    for i, bar in enumerate(bars):
        width = bar.get_width()
        plt.text(width + width*0.01, bar.get_y() + bar.get_height()/2, 
                f'{int(width):,}', ha='left', va='center', fontsize=10)
    
    # 2. Death Rate Comparison
    plt.subplot(4, 2, 2)
    df_death_sorted = df.sort_values('death_rate', ascending=True)
    bars = plt.barh(df_death_sorted['drug_name'], df_death_sorted['death_rate'])
    plt.xlabel('Death Rate (% of Total Reports)')
    plt.title('Death Rate by Drug', fontsize=14, fontweight='bold')
    plt.grid(axis='x', alpha=0.3)
    
    # Add value labels
    for i, bar in enumerate(bars):
        width = bar.get_width()
        plt.text(width + width*0.01, bar.get_y() + bar.get_height()/2, 
                f'{width:.2f}%', ha='left', va='center', fontsize=10)
    
    # 3. ADHD Medications Focus - Total Reports
    plt.subplot(4, 2, 3)
    adhd_sorted = adhd_drugs.sort_values('total_reports', ascending=False)
    bars = plt.bar(range(len(adhd_sorted)), adhd_sorted['total_reports'])
    plt.xlabel('ADHD Medications')
    plt.ylabel('Total Reports')
    plt.title('ADHD Medications: Total FAERS Reports', fontsize=14, fontweight='bold')
    plt.xticks(range(len(adhd_sorted)), [name.replace(' (P)', '') for name in adhd_sorted['drug_name']], rotation=45)
    plt.grid(axis='y', alpha=0.3)
    
    # Add value labels
    for i, bar in enumerate(bars):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height + height*0.01, 
                f'{int(height):,}', ha='center', va='bottom', fontsize=10)
    
    # 4. ADHD Medications Focus - Death Rate
    plt.subplot(4, 2, 4)
    bars = plt.bar(range(len(adhd_sorted)), adhd_sorted['death_rate'])
    plt.xlabel('ADHD Medications')
    plt.ylabel('Death Rate (%)')
    plt.title('ADHD Medications: Death Rate Comparison', fontsize=14, fontweight='bold')
    plt.xticks(range(len(adhd_sorted)), [name.replace(' (P)', '') for name in adhd_sorted['drug_name']], rotation=45)
    plt.grid(axis='y', alpha=0.3)
    
    # Add value labels
    for i, bar in enumerate(bars):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height + height*0.01, 
                f'{height:.2f}%', ha='center', va='bottom', fontsize=10)
    
    # 5. Serious Outcomes Breakdown (Stacked Bar)
    plt.subplot(4, 2, 5)
    df_serious = df.sort_values('serious_outcomes', ascending=True)
    
    # Create stacked bar chart
    deaths = df_serious['total_deaths']
    life_threat = df_serious['total_life_threatening']
    hospital = df_serious['total_hospitalized']
    
    plt.barh(df_serious['drug_name'], deaths, label='Deaths', color='#d62728')
    plt.barh(df_serious['drug_name'], life_threat, left=deaths, label='Life Threatening', color='#ff7f0e')
    plt.barh(df_serious['drug_name'], hospital, left=deaths+life_threat, label='Hospitalized', color='#2ca02c')
    
    plt.xlabel('Number of Serious Outcomes')
    plt.title('Serious Outcomes Breakdown by Type', fontsize=14, fontweight='bold')
    plt.legend()
    plt.grid(axis='x', alpha=0.3)
    
    # 6. Brand vs Generic Comparison (Ibuprofen)
    plt.subplot(4, 2, 6)
    ibu_data = df[df['active_ingredient'] == 'Ibuprofen'].copy()
    
    metrics = ['total_reports', 'total_deaths', 'death_rate']
    x = np.arange(len(metrics))
    width = 0.35
    
    advil_vals = [ibu_data[ibu_data['drug_name'] == 'ADVIL (P)'][metric].iloc[0] for metric in metrics]
    generic_vals = [ibu_data[ibu_data['drug_name'] == 'IBUPROFEN (G)'][metric].iloc[0] for metric in metrics]
    
    plt.bar(x - width/2, advil_vals, width, label='ADVIL (Brand)', alpha=0.8)
    plt.bar(x + width/2, generic_vals, width, label='IBUPROFEN (Generic)', alpha=0.8)
    
    plt.xlabel('Metrics')
    plt.ylabel('Values')
    plt.title('Brand vs Generic: Ibuprofen Comparison', fontsize=14, fontweight='bold')
    plt.xticks(x, ['Total Reports', 'Total Deaths', 'Death Rate (%)'])
    plt.legend()
    plt.grid(axis='y', alpha=0.3)
    
    # 7. Methylphenidate Formulations (Ritalin vs Concerta)
    plt.subplot(4, 2, 7)
    methyl_data = df[df['active_ingredient'] == 'Methylphenidate'].copy()
    
    metrics = ['total_reports', 'total_deaths', 'death_rate']
    x = np.arange(len(metrics))
    width = 0.35
    
    ritalin_vals = [methyl_data[methyl_data['drug_name'] == 'RITALIN (P)'][metric].iloc[0] for metric in metrics]
    concerta_vals = [methyl_data[methyl_data['drug_name'] == 'CONCERTA (P)'][metric].iloc[0] for metric in metrics]
    
    plt.bar(x - width/2, ritalin_vals, width, label='RITALIN', alpha=0.8)
    plt.bar(x + width/2, concerta_vals, width, label='CONCERTA', alpha=0.8)
    
    plt.xlabel('Metrics')
    plt.ylabel('Values')
    plt.title('Methylphenidate Formulations: Ritalin vs Concerta', fontsize=14, fontweight='bold')
    plt.xticks(x, ['Total Reports', 'Total Deaths', 'Death Rate (%)'])
    plt.legend()
    plt.grid(axis='y', alpha=0.3)
    
    # 8. Risk-Benefit Visual (Reports vs Deaths)
    plt.subplot(4, 2, 8)
    scatter = plt.scatter(df['total_reports'], df['total_deaths'], 
                         s=df['serious_rate']*10, alpha=0.6, 
                         c=range(len(df)), cmap='viridis')
    
    # Add drug name labels
    for i, row in df.iterrows():
        plt.annotate(row['drug_name'].replace(' (P)', '').replace(' (G)', ''), 
                    (row['total_reports'], row['total_deaths']),
                    xytext=(5, 5), textcoords='offset points', fontsize=8)
    
    plt.xlabel('Total Reports')
    plt.ylabel('Total Deaths')
    plt.title('Risk Profile: Reports vs Deaths\n(Bubble size = Serious Outcome Rate)', fontsize=14, fontweight='bold')
    plt.grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/workspace/faers_comprehensive_analysis.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    return df

def create_rss_feeds(df):
    """Create RSS feeds for ongoing FAERS monitoring"""
    
    # Main FAERS RSS Feed
    rss = ET.Element("rss", version="2.0")
    channel = ET.SubElement(rss, "channel")
    
    ET.SubElement(channel, "title").text = "ADHD Clearinghouse: FAERS Pharmacovigilance Updates"
    ET.SubElement(channel, "link").text = "https://adhd-clearinghouse.com/faers-updates"
    ET.SubElement(channel, "description").text = "Current FDA Adverse Event Reporting System (FAERS) data for ADHD medications and comparator drugs"
    ET.SubElement(channel, "language").text = "en-us"
    ET.SubElement(channel, "lastBuildDate").text = datetime.now().strftime("%a, %d %b %Y %H:%M:%S GMT")
    ET.SubElement(channel, "generator").text = "ADHD Clearinghouse Pharmacovigilance System"
    
    # Add items for each drug
    for _, row in df.iterrows():
        item = ET.SubElement(channel, "item")
        
        drug_name = row['drug_name']
        ET.SubElement(item, "title").text = f"FAERS Update: {drug_name} - {row['total_reports']} Total Reports"
        ET.SubElement(item, "description").text = f"""
        <![CDATA[
        <h3>Current FAERS Data for {drug_name}</h3>
        <ul>
        <li><strong>Total Reports:</strong> {row['total_reports']:,}</li>
        <li><strong>Deaths:</strong> {row['total_deaths']}</li>
        <li><strong>Death Rate:</strong> {row['death_rate']}%</li>
        <li><strong>Life Threatening:</strong> {row['total_life_threatening']}</li>
        <li><strong>Hospitalizations:</strong> {row['total_hospitalized']}</li>
        <li><strong>Active Ingredient:</strong> {row['active_ingredient']}</li>
        </ul>
        <p><em>Data current as of 2025-10-28. FAERS reports represent suspected associations, not proven causation.</em></p>
        ]]>
        """
        ET.SubElement(item, "link").text = f"https://adhd-clearinghouse.com/faers/{drug_name.lower().replace(' ', '-').replace('(', '').replace(')', '')}"
        ET.SubElement(item, "guid").text = f"faers-{drug_name.lower().replace(' ', '-').replace('(', '').replace(')', '')}-20251028"
        ET.SubElement(item, "pubDate").text = datetime.now().strftime("%a, %d %b %Y %H:%M:%S GMT")
    
    # Create ADHD-specific RSS feed
    adhd_rss = ET.Element("rss", version="2.0")
    adhd_channel = ET.SubElement(adhd_rss, "channel")
    
    ET.SubElement(adhd_channel, "title").text = "ADHD Medications: FAERS Safety Updates"
    ET.SubElement(adhd_channel, "link").text = "https://adhd-clearinghouse.com/adhd-faers-updates"
    ET.SubElement(adhd_channel, "description").text = "Focused FAERS adverse event monitoring for ADHD medications: Vyvanse, Concerta, Strattera, Ritalin"
    ET.SubElement(adhd_channel, "language").text = "en-us"
    ET.SubElement(adhd_channel, "lastBuildDate").text = datetime.now().strftime("%a, %d %b %Y %H:%M:%S GMT")
    
    # Add ADHD medication items
    adhd_drugs = df[df['drug_name'].isin(['VYVANSE (P)', 'CONCERTA (P)', 'STRATTERA (P)', 'RITALIN (P)'])]
    for _, row in adhd_drugs.iterrows():
        item = ET.SubElement(adhd_channel, "item")
        
        drug_name = row['drug_name']
        ET.SubElement(item, "title").text = f"ADHD Safety Alert: {drug_name} FAERS Profile"
        ET.SubElement(item, "description").text = f"""
        <![CDATA[
        <h3>ADHD Medication Safety Profile: {drug_name}</h3>
        <table border="1" style="border-collapse: collapse;">
        <tr><th>Metric</th><th>Value</th><th>Context</th></tr>
        <tr><td>Total Reports</td><td>{row['total_reports']:,}</td><td>Lifetime FAERS reports</td></tr>
        <tr><td>Deaths</td><td>{row['total_deaths']}</td><td>{row['death_rate']}% of reports</td></tr>
        <tr><td>Serious Outcomes</td><td>{row['serious_outcomes']:,}</td><td>{row['serious_rate']}% of reports</td></tr>
        <tr><td>Active Ingredient</td><td>{row['active_ingredient']}</td><td>Pharmacological class</td></tr>
        </table>
        <p><strong>Clinical Context:</strong> This data should be interpreted alongside prescribing volume, patient population, and reporting patterns.</p>
        ]]>
        """
        ET.SubElement(item, "link").text = f"https://adhd-clearinghouse.com/medications/{row['active_ingredient'].lower()}"
        ET.SubElement(item, "guid").text = f"adhd-faers-{drug_name.lower().replace(' ', '-').replace('(', '').replace(')', '')}-20251028"
        ET.SubElement(item, "pubDate").text = datetime.now().strftime("%a, %d %b %Y %H:%M:%S GMT")
    
    # Save RSS feeds
    def prettify(elem):
        rough_string = ET.tostring(elem, 'unicode')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")
    
    with open('/workspace/faers_pharmacovigilance_feed.xml', 'w', encoding='utf-8') as f:
        f.write(prettify(rss))
    
    with open('/workspace/adhd_faers_safety_feed.xml', 'w', encoding='utf-8') as f:
        f.write(prettify(adhd_rss))
    
    print("RSS feeds created:")
    print("- faers_pharmacovigilance_feed.xml (All drugs)")
    print("- adhd_faers_safety_feed.xml (ADHD medications only)")

def create_summary_report(df):
    """Create a summary report of key findings"""
    
    report = f"""# FAERS Pharmacovigilance Analysis Report
*Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*
*Data Source: FDA FAERS Public Dashboard (Current as of 2025-10-28)*

## Executive Summary

This analysis examines adverse event reports from the FDA's FAERS database for 8 commonly prescribed medications across pain management and ADHD treatment categories.

### Key Findings

**Highest Total Reports:**
1. Acetaminophen (Generic): {df[df['drug_name'] == 'ACETAMINOPHEN (G)']['total_reports'].iloc[0]:,} reports
2. Ibuprofen (Generic): {df[df['drug_name'] == 'IBUPROFEN (G)']['total_reports'].iloc[0]:,} reports
3. Advil (Brand): {df[df['drug_name'] == 'ADVIL (P)']['total_reports'].iloc[0]:,} reports

**Highest Death Rates (% of reports resulting in death):**
1. {df.sort_values('death_rate', ascending=False).iloc[0]['drug_name']}: {df.sort_values('death_rate', ascending=False).iloc[0]['death_rate']:.2f}%
2. {df.sort_values('death_rate', ascending=False).iloc[1]['drug_name']}: {df.sort_values('death_rate', ascending=False).iloc[1]['death_rate']:.2f}%
3. {df.sort_values('death_rate', ascending=False).iloc[2]['drug_name']}: {df.sort_values('death_rate', ascending=False).iloc[2]['death_rate']:.2f}%

## ADHD Medication Analysis

"""
    
    adhd_drugs = df[df['drug_name'].isin(['VYVANSE (P)', 'CONCERTA (P)', 'STRATTERA (P)', 'RITALIN (P)'])].copy()
    adhd_drugs = adhd_drugs.sort_values('death_rate', ascending=False)
    
    report += "### ADHD Medications Safety Profile Ranking (by death rate):\n\n"
    for i, (_, row) in enumerate(adhd_drugs.iterrows(), 1):
        report += f"{i}. **{row['drug_name']}** ({row['active_ingredient']})\n"
        report += f"   - Total Reports: {row['total_reports']:,}\n"
        report += f"   - Deaths: {row['total_deaths']} ({row['death_rate']:.2f}%)\n"
        report += f"   - Serious Outcomes: {row['serious_outcomes']:,} ({row['serious_rate']:.1f}%)\n\n"
    
    report += """
## Important Disclaimers

⚠️ **FAERS Data Limitations:**
- Reports represent suspected associations, not proven causation
- Reporting rates vary significantly between drugs based on usage patterns
- Higher report volumes often correlate with higher prescription volumes
- Data should not be used for direct drug-to-drug safety comparisons without considering utilization rates

## Clinical Context

This data provides valuable pharmacovigilance insights but must be interpreted alongside:
- Prescribing volume and patient exposure data
- Underlying patient population characteristics
- Indication-specific risk factors
- Post-marketing surveillance studies

## Monitoring Recommendations

1. **Continue FAERS monitoring** for trend analysis
2. **Integrate with prescription volume data** for normalized risk assessment
3. **Monitor emerging safety signals** through automated alerts
4. **Correlate with clinical literature** and regulatory updates

---
*For real-time updates, subscribe to our RSS feeds:*
- [All Drugs Pharmacovigilance Feed](./faers_pharmacovigilance_feed.xml)
- [ADHD Medications Safety Feed](./adhd_faers_safety_feed.xml)
"""
    
    with open('/workspace/FAERS_ANALYSIS_REPORT.md', 'w', encoding='utf-8') as f:
        f.write(report)
    
    print("Summary report created: FAERS_ANALYSIS_REPORT.md")

if __name__ == "__main__":
    print("Creating FAERS data visualizations and RSS feeds...")
    
    # Create visualizations
    df = create_visual_comparisons()
    print("✓ Comprehensive visualization created: faers_comprehensive_analysis.png")
    
    # Create RSS feeds
    create_rss_feeds(df)
    print("✓ RSS feeds created")
    
    # Create summary report
    create_summary_report(df)
    print("✓ Analysis report created")
    
    # Export structured data
    df.to_json('/workspace/faers_structured_data.json', orient='records', indent=2)
    df.to_csv('/workspace/faers_structured_data.csv', index=False)
    print("✓ Structured data exported (JSON and CSV)")
    
    print("\nFiles created:")
    print("- faers_comprehensive_analysis.png (8-panel visualization)")
    print("- faers_pharmacovigilance_feed.xml (RSS feed - all drugs)")
    print("- adhd_faers_safety_feed.xml (RSS feed - ADHD medications)")
    print("- FAERS_ANALYSIS_REPORT.md (summary report)")
    print("- faers_structured_data.json (structured data)")
    print("- faers_structured_data.csv (CSV export)")