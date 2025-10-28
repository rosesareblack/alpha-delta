#!/usr/bin/env python3
"""
ADHD Clearinghouse - Comprehensive Pharmacology Content Integration
Transform detailed pharmacological information into Strapi-compatible format
"""

import json
from datetime import datetime

def create_pharmacology_articles():
    """Create comprehensive ADHD pharmacology articles"""
    
    # Article 1: LDX Mechanism and Clinical Application
    article_1 = {
        "documentId": "ldx-mechanism-clinical-application",
        "title": "Lisdexamfetamine (LDX): Mechanism of Action and Clinical Application in ADHD Treatment",
        "slug": "lisdexamfetamine-ldx-mechanism-clinical-application",
        "summary": "Comprehensive analysis of LDX as the central pharmacological agent for ADHD and BED, including prodrug mechanism, abuse liability considerations, and clinical rationale for supratherapeutic dosing.",
        "content": [
            {
                "type": "heading",
                "level": 2,
                "content": "Lisdexamfetamine (LDX) as the Central Pharmacological Agent"
            },
            {
                "type": "paragraph",
                "content": "Lisdexamfetamine dimesylate (LDX, Vyvanse) is selected as the central pharmacological strategy due to its unique prodrug structure and its documented efficacy profile across the patient's spectrum of diagnoses. LDX holds FDA approval for both ADHD and Binge Eating Disorder, offering a crucial therapeutic overlap that minimizes the need for complex polypharmacy to manage these two severe, co-occurring conditions."
            },
            {
                "type": "heading",
                "level": 3,
                "content": "Dual FDA Approval: Pharmacological Synergy"
            },
            {
                "type": "paragraph",
                "content": "This dual FDA approval is not merely a convenience, but a profound pharmacological synergy. Both disorders share common neurobiological underpinnings involving dysfunction in the mesolimbic and mesocortical dopamine pathways, particularly in the brain regions governing impulse control, reward processing, and executive function. By effectively modulating Dopamine (DA) and Norepinephrine (NE) via the active d-amphetamine metabolite, LDX simultaneously treats the core deficits of ADHD (inattention, poor organization) and the underlying compulsivity and impulsivity driving BED episodes."
            },
            {
                "type": "paragraph",
                "content": "Utilizing a single, highly effective agent to manage two severe, co-occurring Axis I disorders simplifies the patient's regimen, minimizes the risk of adverse drug interactions associated with polypharmacy, and significantly enhances long-term medication adherence, making LDX the most therapeutically advantageous selection."
            },
            {
                "type": "heading",
                "level": 3,
                "content": "Prodrug Structure and Controlled Release Kinetics"
            },
            {
                "type": "paragraph",
                "content": "The molecule is an inactive prodrug, a condensation of L-lysine (a non-essential amino acid) and dextroamphetamine, which confers a rate-limiting step upon conversion to the active component (d-amphetamine). This unique molecular design fundamentally dictates the drug's predictable release kinetics. The LDX compound is chemically inert until the hydrolysis is mediated by enzymes found predominantly in the blood (specifically within red blood cells) and intestinal mucosa."
            },
            {
                "type": "paragraph",
                "content": "This enzymatic process is the sole rate-limiting factor controlling the speed of d-amphetamine appearance in the systemic circulation. Unlike traditional extended-release (ER) stimulants, which rely on physical delivery mechanisms (e.g., matrix coatings or micro-beads) to slow absorption through the digestive tract, the therapeutic duration of LDX is chemically, not physically, controlled. This chemical stability confers significant PK stability: the enzymatic hydrolysis is largely independent of the gastrointestinal environment, including pH fluctuations, dietary intake, or variations in GI motility."
            },
            {
                "type": "paragraph",
                "content": "This consistent, predictable, and gradual release ensures a smooth, sustained systemic exposure of d-amphetamine, which is vital for minimizing variable efficacy in a metabolically challenged patient."
            },
            {
                "type": "heading",
                "level": 3,
                "content": "Reduced Abuse Liability Through Chemical Protection"
            },
            {
                "type": "paragraph",
                "content": "Crucially, this structure confers a reduced immediate abuse liability relative to traditional immediate-release d-amphetamine, which are highly susceptible to dose manipulation. The subjective, reinforcing effects sought by abusers—the \"rush\" or \"euphoria\"—are directly proportional to the rate of rise in plasma amphetamine concentration, quantified as the dC/dt slope. Traditional amphetamines allow this slope to be dramatically increased when crushed and insufflated or dissolved and injected, leading to a rapid and dangerous surge in Cmax."
            },
            {
                "type": "paragraph",
                "content": "In stark contrast, the prodrug conversion is a saturable enzymatic process; this means the rate at which d-amphetamine is cleaved from L-lysine is constrained by the finite concentration and activity of hydrolytic enzymes in the blood. Attempting to bypass the oral route of administration (e.g., via injection, snorting, or dissolving for sublingual use) does not bypass this biochemical bottleneck. Regardless of the route or the dose administered, the enzymatic conversion rate holds steady, effectively preventing the rapid surge in Cmax that abusers seek."
            },
            {
                "type": "paragraph",
                "content": "This mechanism also provides superior defense against the common failure point of \"dose dumping,\" where physical extended-release tablets, when crushed, instantly release the entire drug load. Because LDX is already fully soluble, its protective feature is chemical, not physical, and cannot be defeated by simple mechanical tampering. This reduced immediate liability is a vital consideration when the patient's metabolic profile necessitates the use of total daily doses far exceeding regulatory maximums."
            },
            {
                "type": "heading",
                "level": 3,
                "content": "Regulatory vs. Pharmacological Risk Assessment"
            },
            {
                "type": "paragraph",
                "content": "It must be noted that even this prodrug carries a Schedule II classification under the Controlled Substances Act, reflecting the high potential for abuse inherent to all amphetamines. This classification is a legal necessity rather than a pharmacological reflection of its actual clinical abuse potential. LDX is scheduled II because its active metabolite, d-amphetamine, is itself a Schedule II substance."
            },
            {
                "type": "paragraph",
                "content": "The regulatory framework often classifies drugs based on the schedule of their active, reinforcing component, which results in the prodrug being grouped alongside highly abusable, immediate-release substances that serve vastly different purposes in clinically distinct populations. This regulatory mandate does not fully account for the unique rate-limiting anti-abuse design inherent to LDX, which functionally differentiates it from substances like cocaine, methamphetamine, or immediate-release amphetamine salts (all Schedule II)."
            },
            {
                "type": "paragraph",
                "content": "From a clinical risk-management standpoint, the Schedule II status is a cautionary flag, but the prodrug structure ensures that the pharmacological risk is significantly mitigated compared to non-prodrug equivalents."
            },
            {
                "type": "heading",
                "level": 3,
                "content": "Neurobiological Rationale for Treatment"
            },
            {
                "type": "paragraph",
                "content": "The core issue lies in the fact that the regulatory abuse model is often predicated on the abuse potential of illicit, non-pharmaceutical substances, such as street methamphetamine, where the sole goal is to achieve an extremely high dC/dt (rate of concentration rise) that leads to profound, addictive euphoria. LDX, by contrast, is a pharmaceutical product designed to maintain a therapeutic-level dopamine signal in the prefrontal cortex (PFC) to normalize function."
            },
            {
                "type": "paragraph",
                "content": "The enzymatic conversion of LDX into d-amphetamine acts as a physiological choke-point: it physically prevents the user from achieving the high dC/dt slope characteristic of abuse. Whether the patient takes 70 mg or attempts to take 200 mg at once, the dC/dt slope remains limited by the enzyme's saturation, neutralizing the pharmacological mechanism of recreational reinforcement."
            },
            {
                "type": "paragraph",
                "content": "The abuse potential of street methamphetamine, therefore, provides a poor pharmacological basis for evaluating the inherent risk of the LDX prodrug system in a therapeutic population."
            },
            {
                "type": "heading",
                "level": 3,
                "content": "Therapeutic Protection Against Substance Use Disorders"
            },
            {
                "type": "paragraph",
                "content": "Available literature suggests that while the molecule is chemically related, the prodrug structure itself lacks verifiable evidence to conflate it directly with dependence, particularly when prescribed appropriately. Instead, effective treatment with stimulants is strongly correlated with abstaining from illegal substances in populations with patients with ADHD."
            },
            {
                "type": "paragraph",
                "content": "This protective effect results from the successful management of core ADHD symptoms (impulsivity and executive dysfunction), which are key drivers of self-medication and subsequent Substance Use Disorder (SUD) development. Untreated ADHD is strongly associated with a Reward Deficiency Syndrome, where chronic low baseline dopamine levels prompt individuals to seek external, immediate, and intense dopaminergic stimulation (i.e., illicit substances) to achieve baseline functionality or relief from dysphoria."
            },
            {
                "type": "paragraph",
                "content": "LDX, through its smooth and sustained delivery of d-amphetamine, normalizes this dopaminergic signaling in the prefrontal cortex, correcting the underlying neurobiological deficit and thus extinguishing the drive for self-medication. Therefore, the clinical decision to use a high dose of LDX balances the minimal immediate abuse liability of the prodrug against the severe, long-term risk of untreated, highly disabling multi-comorbidity, which itself is a major precursor to SUD."
            }
        ],
        "author": "MiniMax Agent",
        "category": "Treatment & Medication",
        "tags": ["LDX", "Vyvanese", "Pharmacology", "ADHD Treatment", "Binge Eating Disorder", "Stimulants"],
        "seo_title": "Lisdexamfetamine (LDX) Mechanism: Clinical Application for ADHD Treatment",
        "seo_description": "Comprehensive analysis of LDX prodrug mechanism, abuse liability considerations, and clinical rationale for optimized ADHD treatment protocols.",
        "published_at": datetime.now().isoformat()
    }

    # Article 2: Rapid Metabolizer Phenomenon
    article_2 = {
        "documentId": "rapid-metabolizer-phenomenon",
        "title": "Understanding Rapid Metabolizers: Pharmacokinetic and Pharmacodynamic Failure in Ultra-Rapid Metabolizers",
        "slug": "rapid-metabolizer-phenomenon-pharmacokinetic-failure",
        "summary": "Clinical analysis of the rapid metabolizer phenotype, including mechanistic understanding of accelerated LDX clearance and therapeutic strategies for sustained symptom control.",
        "content": [
            {
                "type": "heading",
                "level": 2,
                "content": "Pharmacokinetic and Pharmacodynamic Failure in Ultra-Rapid Metabolizers"
            },
            {
                "type": "heading",
                "level": 3,
                "content": "The Clinical Phenotype of Stimulant 'Rapid Metabolizers' (RM)"
            },
            {
                "type": "paragraph",
                "content": "The term \"rapid metabolizer\" (RM) describes a real clinical phenomenon characterized by a significant abbreviation of the stimulant's duration of efficacy and/or an insufficient clinical response at conventional dosages. The classic manifestation of this phenotype is a rapid onset of therapeutic effect followed by a swift cessation, often described as a \"crash.\" This results in the maximum approved once-daily dose of 70 mg of LDX providing effective functional coverage for only 3 to 6 hours, rather than the expected full day."
            },
            {
                "type": "heading",
                "level": 3,
                "content": "Mechanistic Analysis of LDX Hydrolysis and Clearance"
            },
            {
                "type": "paragraph",
                "content": "LDX is an inactive prodrug that requires rate-limiting hydrolysis, predominantly in the blood, to release the active component, d-amphetamine. The failure in the RM phenotype involves a complex interplay of conversion and clearance:"
            },
            {
                "type": "list",
                "style": "unordered",
                "items": [
                    "Accelerated Conversion: The rate-limiting hydrolysis, mediated primarily by erythrocyte-based enzymes, may be subject to individual variability, resulting in Accelerated Conversion. This hydrolysis of LDX to d-amphetamine might be faster or more efficient than the population mean, potentially leading to a slightly higher or earlier initial peak plasma concentration (Cmax) of the active metabolite. However, this acceleration alone does not fully account for the dramatic shortening of clinical duration.",
                    "Accelerated Clearance of the Active Metabolite: Accelerated Clearance of the Active Metabolite is the true core of the RM problem. Once the active d-amphetamine is released, it is subject to standard hepatic metabolism (primarily via CYP2D6) and renal excretion. In the ultra-rapid metabolizer, genetic polymorphisms or other factors cause the active d-amphetamine to be cleared from the systemic circulation significantly faster than average. This causes a precipitous drop in therapeutic plasma concentration and a critically shortened effective half-life (T1/2). This phenomenon severely compresses the PK curve, causing the plasma concentration to fall below the Minimal Effective Concentration (MEC) prematurely."
                ]
            },
            {
                "type": "paragraph",
                "content": "This combination severely compresses the PK curve. Even if the maximum concentration (Cmax) is achieved quickly, the overall exposure over the duration of a functional day, quantified by the Area Under the Curve (AUC), is dramatically reduced. The therapeutic blood level is prematurely abandoned, leading directly to the clinical manifestation of the \"crash\" and the need for immediate re-dosing, often 6-8 hours earlier than expected."
            },
            {
                "type": "paragraph",
                "content": "Since the extended-release property of LDX is chemically dependent on the rate-limiting step of prodrug conversion—and is not achieved through a physical delivery mechanism susceptible to tampering or rapid gastric transit—the therapeutic intervention must fundamentally circumvent the accelerated clearance of the active metabolite by adding more substrate (LDX) at the point when the plasma concentration of d-amphetamine drops below the minimal effective concentration (MEC). This strategy effectively creates a new Cmax and AUC to extend the daily coverage."
            },
            {
                "type": "table",
                "headers": ["PK Parameter", "Standard Metabolism Profile", "Ultra-Rapid Metabolism (RM) Profile", "Clinical Consequence for RM Patient"],
                "rows": [
                    ["LDX Conversion Rate", "Rate-limited by hydrolysis", "Accelerated or highly efficient conversion", "Faster onset; higher initial exposure to d-amphetamine"],
                    ["d-Amphetamine Tmax", "Typically 3.5 hours", "Potentially faster onset (<3 hours)", "Early peak effect; rapid initiation of wear-off phase"],
                    ["Duration of Therapeutic Effect", "8–14 hours", "3–6 hours (or less)", "Coverage failure (e.g., 'crash'); necessitates re-dosing"]
                ],
                "caption": "Table 1: Pharmacokinetic Comparison: Standard vs. Ultra-Rapid Metabolism of LDX"
            }
        ],
        "author": "MiniMax Agent",
        "category": "Treatment & Medication",
        "tags": ["Rapid Metabolizer", "Pharmacokinetics", "LDX", "Dosing", "ADHD Treatment"],
        "seo_title": "Rapid Metabolizer Phenomenon: Understanding LDX Pharmacokinetic Failure",
        "seo_description": "Clinical analysis of rapid metabolizer phenotype and therapeutic strategies for sustained ADHD symptom control.",
        "published_at": datetime.now().isoformat()
    }

    # Article 3: Optimized Dosing and Therapeutic Drug Monitoring
    article_3 = {
        "documentId": "optimized-dosing-therapeutic-monitoring",
        "title": "Optimizing LDX Dose and Duration: Individualized Treatment Protocols and Therapeutic Drug Monitoring",
        "slug": "optimized-ldx-dosing-therapeutic-drug-monitoring",
        "summary": "Comprehensive guide to supratherapeutic LDX dosing, including allometric scaling, inverted U-curve optimization, and therapeutic drug monitoring protocols for rapid metabolizers.",
        "content": [
            {
                "type": "heading",
                "level": 2,
                "content": "Optimizing Dose and Duration in the Rapid Metabolizer"
            },
            {
                "type": "heading",
                "level": 3,
                "content": "Individualized Optimization vs. Regulatory Maximums"
            },
            {
                "type": "paragraph",
                "content": "While regulatory bodies recommend a maximum approved dose of 70 mg/day for LDX, clinical practice mandates that the dose for every patient must be individually optimized based on documented therapeutic efficacy and the side effect profile. Apparent stimulant failure is often, in fact, medication underdosing, which occurs in refractory cases or in large adult patients whose required dose based on milligrams per kilogram (mg/kg) exceeds the absolute milligram limit."
            },
            {
                "type": "heading",
                "level": 3,
                "content": "Clinical Justification for Supratherapeutic Dosing (>70 mg/d)"
            },
            {
                "type": "paragraph",
                "content": "For the refractory patient who fails the 70 mg/d maximum due to metabolic challenges, a robust clinical rationale is essential for dose escalation. This rationale is grounded in the principle of treatment optimization rather than deviation, recognizing that the regulatory limit is a population average, not an absolute pharmacological ceiling."
            },
            {
                "type": "heading",
                "level": 4,
                "content": "Allometric Scaling and Body Weight (Pharmacokinetic Adequacy)"
            },
            {
                "type": "paragraph",
                "content": "Standard drug efficacy studies determine the maximum dose based on average body weight and statistical safety margins derived from population means. However, pharmacology dictates that drug concentrations scale with mass. For a heavier patient (e.g., a 120 kg adult), a dose of 70 mg translates to a concentration per kilogram (mg/kg) that is significantly lower than in a standard 70 kg reference individual."
            },
            {
                "type": "paragraph",
                "content": "This mg/kg basis is the first compelling argument for exceeding the absolute milligram limit. When the patient's body mass dictates a need for a dose that exceeds the FDA maximum (e.g., 100 mg/day or more), the clinician is adhering to the pharmacokinetic principle of allometric scaling. Clinical precedent exists where doses substantially higher than the FDA maximum (e.g., 100 mg/day or 120 mg/day) have been successfully argued as being within the standard of care for refractory, non-diverting populations, provided the treatment goal is clearly defined and achieved."
            },
            {
                "type": "heading",
                "level": 4,
                "content": "Severity of Illness and Therapeutic Imperative (Ethical and Clinical Necessity)"
            },
            {
                "type": "paragraph",
                "content": "Given the multiple, severe, and synergistic comorbidities (ADHD-I, BED, Narcolepsy), this patient is classified as having severe, multi-system impairment. The presence of three highly disabling Axis I conditions necessitates an aggressive, optimized dosing approach because the functional consequences of untreated illness (e.g., occupational failure, obesity-related health risks, and affective lability) far outweigh the controlled risks of optimized pharmacotherapy."
            },
            {
                "type": "paragraph",
                "content": "The patient's clinical situation transforms the argument from one of mere symptom control to one of disability mitigation and functional restoration."
            },
            {
                "type": "heading",
                "level": 3,
                "content": "The Neurobiological Rationale for Cognitive Efficacy: The Inverted U-Curve"
            },
            {
                "type": "paragraph",
                "content": "The patient's ADHD-I subtype means core functional deficits center on complex executive functions controlled by the Dorsolateral Prefrontal Cortex (DLPFC), including sustained attention, planning, and working memory. Optimal treatment requires achieving sufficient, but not excessive, saturation of the DAT and NET transporter sites in the PFC."
            },
            {
                "type": "heading",
                "level": 4,
                "content": "Target Saturation and Modulatory Effect"
            },
            {
                "type": "paragraph",
                "content": "d-amphetamine exerts its effect by acting as an Indirect Sympathomimetic, reversing the flow of Dopamine (DA) and Norepinephrine (NE) via the respective transporters. For cognitive function, the goal is not maximum dopamine release, but optimal concentration in the synaptic cleft. Insufficient DA (the baseline state of ADHD) leads to poor signal-to-noise ratio in the PFC. Excessive DA (high-dose or abuse-level) leads to over-stimulation, resulting in anxiety, rigidity, and the deterioration of working memory."
            },
            {
                "type": "heading",
                "level": 4,
                "content": "The Cognitive Threshold and the Inverted U-Curve"
            },
            {
                "type": "paragraph",
                "content": "The relationship between prefrontal DA concentration and cognitive performance is governed by the Inverted U-Curve Hypothesis. Cognitive performance is highest at an intermediate, optimal level of DA signaling. Below this level (underdosing/rapid clearance), efficacy is low. Above this level (overdosing/toxicity), performance rapidly declines. It is hypothesized that the ADHD-I phenotype necessitates a preferentially higher plasma concentration of d-amphetamine to adequately modulate the DA/NE systems in the PFC required for cognitive normalization, pushing the patient toward the optimal peak of this U-curve."
            },
            {
                "type": "paragraph",
                "content": "The patient's therapeutic failure is thus driven by a combination of factors: a) Rapid PK clearance (shorter T1/2) prematurely drops the concentration below the optimal cognitive threshold, and b) the Pharmacodynamic requirement of the ADHD-I phenotype demands an intrinsically higher plasma concentration to reach the target saturation in the first place. The high total dose strategy is necessary to overcome both the clearance speed and the high PD set-point."
            },
            {
                "type": "heading",
                "level": 3,
                "content": "The Necessity and Protocol for Therapeutic Drug Monitoring (TDM)"
            },
            {
                "type": "paragraph",
                "content": "Prescribing above the 70 mg/d threshold introduces elevated risks. To bridge the gap between clinical necessity (to overcome metabolic failure) and regulatory risk management, a high-dose regimen must be meticulously supported by Therapeutic Drug Monitoring (TDM). This moves the decision from subjective guesswork to objective, verifiable pharmacology."
            },
            {
                "type": "heading",
                "level": 4,
                "content": "Objective Justification and Risk Mitigation"
            },
            {
                "type": "paragraph",
                "content": "TDM is the definitive tool to objectively confirm the rapid clearance kinetics (duration failure) and to ensure that the necessary high total dose does not translate into dangerous peak concentrations (Cmax). This serves a critical risk management function by creating an auditable record that the clinician is managing the drug within a documented therapeutic window, even if the total milligram count is off-label."
            },
            {
                "type": "heading",
                "level": 4,
                "content": "Sample Timing and Kinetic Confirmation"
            },
            {
                "type": "paragraph",
                "content": "Blood draws must be strategically timed to validate the core clinical problem and the safety of the solution:"
            },
            {
                "type": "list",
                "style": "unordered",
                "items": [
                    "Cmax Sample (Safety Check): Taken 3.0 to 4.0 hours after the largest single morning dose. The primary goal is to ensure the peak plasma concentration is below acute toxicity or euphoria thresholds (>80 ng/mL).",
                    "Ctrough Sample (Efficacy/RM Confirmation): Taken immediately prior to the second, noon dose. A Ctrough level dropping rapidly to sub-therapeutic levels (e.g., <15 ng/mL) confirms the patient's Accelerated Clearance status (RM phenotype) and objectively justifies the need for the divided, high-dose strategy."
                ]
            },
            {
                "type": "heading",
                "level": 4,
                "content": "Metabolite Ratio Analysis"
            },
            {
                "type": "paragraph",
                "content": "Beyond simply measuring d-amphetamine levels, TDM can also measure the ratio of the prodrug Lisdexamfetamine (LDX) to the active metabolite d-amphetamine. A disproportionately low ratio of LDX/d-amphetamine could indicate an Accelerated Conversion rate (though less common than accelerated clearance), while an unusually high ratio may suggest a lack of compliance or a different metabolic issue. This advanced metric provides a deeper insight into the patient's unique enzymatic profile."
            },
            {
                "type": "heading",
                "level": 4,
                "content": "Target Range and Safety Thresholds"
            },
            {
                "type": "paragraph",
                "content": "The Goal Cmax should aim for the upper-end of the validated therapeutic window (e.g., 35–50 ng/mL in adults) to achieve the necessary cognitive saturation for the ADHD-I subtype. Crucially, the Safety Ceiling of Cmax must remain below >80 ng/mL, as concentrations approaching this level dramatically increase the risk of cardiovascular events, anxiety, psychosis, and subjective reinforcing effects that increase the risk of misuse."
            }
        ],
        "author": "MiniMax Agent",
        "category": "Treatment & Medication",
        "tags": ["LDX Dosing", "Therapeutic Drug Monitoring", "ADHD-I", "Supratherapeutic Dosing", "Pharmacokinetics"],
        "seo_title": "Optimized LDX Dosing: Individualized Protocols and Therapeutic Monitoring",
        "seo_description": "Comprehensive guide to supratherapeutic LDX dosing protocols and therapeutic drug monitoring for ADHD-I treatment optimization.",
        "published_at": datetime.now().isoformat()
    }

    return [article_1, article_2, article_3]

def update_strapi_entities():
    """Update the existing Strapi entities with the new pharmacology content"""
    
    try:
        # Read existing entities
        with open('/workspace/strapi/strapi/data/entities/entities_00001.jsonl', 'r') as f:
            lines = f.readlines()
        
        entities = []
        for line in lines:
            if line.strip():
                entities.append(json.loads(line))
        
        # Create new pharmacology articles
        new_articles = create_pharmacology_articles()
        
        # Add the new articles to entities
        for i, article in enumerate(new_articles):
            # Create entity structure similar to existing articles
            entity = {
                "documentId": article["documentId"],
                "title": article["title"],
                "slug": article["slug"],
                "summary": article["summary"],
                "content": json.dumps(article["content"]),
                "author": article["author"],
                "seo_title": article["seo_title"],
                "seo_description": article["seo_description"],
                "published_at": article["published_at"],
                "createdAt": article["published_at"],
                "updatedAt": article["published_at"],
                "publishedAt": article["published_at"],
                "locale": "en"
            }
            
            # Create Strapi entity format
            strapi_entity = {
                "data": {
                    "id": 100 + i,  # New IDs for new articles
                    "attributes": entity
                }
            }
            
            # Add to entities list
            entities.append(strapi_entity)
        
        # Write updated entities back to file
        with open('/workspace/strapi/strapi/data/entities/entities_00001.jsonl', 'w') as f:
            for entity in entities:
                f.write(json.dumps(entity, separators=(',', ':')) + '\n')
        
        print(f"Successfully added {len(new_articles)} pharmacology articles to Strapi entities")
        print(f"Total entities: {len(entities)}")
        
        # Create new export
        import subprocess
        import tarfile
        
        # Create tar.gz export
        with tarfile.open('/workspace/strapi/strapi/data/pharmacology_enhanced_export_20250128.tar.gz', 'w:gz') as tar:
            tar.add('/workspace/strapi/strapi/data', arcname='.')
        
        print("Created enhanced export: pharmacology_enhanced_export_20250128.tar.gz")
        
        return True
        
    except Exception as e:
        print(f"Error updating entities: {e}")
        return False

if __name__ == "__main__":
    print("Creating comprehensive ADHD pharmacology content...")
    print("="*60)
    
    articles = create_pharmacology_articles()
    
    for i, article in enumerate(articles, 1):
        print(f"\nArticle {i}: {article['title']}")
        print(f"Summary: {article['summary']}")
        print(f"Tags: {', '.join(article['tags'])}")
        print(f"Category: {article['category']}")
        print("-" * 50)
    
    # Update Strapi entities
    print("\nUpdating Strapi entities with pharmacology content...")
    success = update_strapi_entities()
    
    if success:
        print("\n✅ Successfully integrated comprehensive ADHD pharmacology content!")
        print("\nThis content includes:")
        print("• LDX prodrug mechanism and clinical application")
        print("• Rapid metabolizer phenomenon analysis")
        print("• Optimized dosing protocols and therapeutic monitoring")
        print("• Neurobiological rationale and safety considerations")
        print("• Regulatory vs. pharmacological risk assessment")
        print("\nThe content is now ready for Strapi import and provides:")
        print("• Professional-grade pharmacological information")
        print("• Evidence-based treatment protocols")
        print("• Safety monitoring guidelines")
        print("• Clinical decision-making support")
    else:
        print("\n❌ Failed to update Strapi entities")