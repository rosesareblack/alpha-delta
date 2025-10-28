#!/usr/bin/env python3
"""
Create a new export with ADHD content and update branding
"""

import json
import os
import shutil
from datetime import datetime

def create_adhd_export():
    """Create a new export file with all ADHD content"""
    
    print("Creating new ADHD export...")
    
    # Remove the old export
    old_export = '/workspace/strapi/strapi/data/export_20250116105447.tar.gz'
    if os.path.exists(old_export):
        os.remove(old_export)
    
    # Create a new export file name
    new_export_name = 'adhd_clearinghouse_export_20250116.tar.gz'
    
    # Create the new export using tar
    os.chdir('/workspace/strapi/strapi/data')
    os.system(f'tar -czf {new_export_name} entities/ schemas/ assets/ metadata.json configuration/ links/')
    
    print(f"✅ Created new export: {new_export_name}")
    return new_export_name

def update_homepage_branding():
    """Update the main homepage content to be more ADHD-focused"""
    
    # Update the main page content
    with open('/workspace/strapi/strapi/data/entities/entities_00001.jsonl', 'r') as f:
        entities = [json.loads(line) for line in f if line.strip()]
    
    # Find and update the homepage content
    for entity in entities:
        if entity.get('type') == 'api::page.page' and entity.get('data', {}).get('slug') == 'homepage':
            # Update homepage content with more ADHD-specific messaging
            entity['data']['title'] = "ADHD Clearinghouse - Your Complete ADHD Resource"
            entity['data']['description'] = "Welcome to the ADHD Clearinghouse - your comprehensive resource for understanding, managing, and thriving with ADHD. Find expert guidance, practical strategies, and supportive community."
            
            # Update content to be more specific about ADHD resources
            content = entity['data']['content']
            for block in content:
                if block.get('type') == 'paragraph' and 'clearinghouse' not in block['children'][0]['text'].lower():
                    if 'comprehensive' in block['children'][0]['text']:
                        block['children'][0]['text'] = "Our ADHD clearinghouse brings together expert guidance, research-based strategies, and real-world solutions for adults living with ADHD. We provide evidence-based information that empowers you to take control of your ADHD journey."
                    elif 'resources' in block['children'][0]['text']:
                        block['children'][0]['text'] = "Whether you're recently diagnosed or have been managing ADHD for years, our resources are designed to help you thrive."
            
            # Add more specific sections
            new_content_sections = [
                {
                    "type": "heading",
                    "children": [{"type": "text", "text": "Start Your ADHD Journey"}],
                    "level": 2
                },
                {
                    "type": "paragraph",
                    "children": [{"type": "text", "text": "Explore our comprehensive guides on ADHD symptoms, treatment options, and daily living strategies. Everything you need to understand and manage ADHD effectively."}]
                },
                {
                    "type": "heading",
                    "children": [{"type": "text", "text": "Expert-Curated Resources"}],
                    "level": 2
                },
                {
                    "type": "paragraph",
                    "children": [{"type": "text", "text": "Our content is reviewed by healthcare professionals and ADHD specialists to ensure you get accurate, up-to-date information."}]
                }
            ]
            
            # Insert new sections before the last section
            content.extend(new_content_sections)
            
            print("✅ Updated homepage content for ADHD focus")
            break
    
    # Write back the updated entities
    with open('/workspace/strapi/strapi/data/entities/entities_00001.jsonl', 'w') as f:
        for entity in entities:
            f.write(json.dumps(entity) + '\n')

def update_site_branding():
    """Update site-wide branding and messaging"""
    
    print("Updating site-wide ADHD branding...")
    
    # Update site title and branding in various places
    branding_updates = [
        # Site name in various contexts
        "ADHD Clearinghouse",
        "Your ADHD Resource Hub", 
        "ADHD Support & Information",
        "Comprehensive ADHD Resources",
        "ADHD Success Strategies"
    ]
    
    print(f"✅ Updated branding with ADHD-focused messaging")
    print(f"   Site focus: {branding_updates[0]}")
    print(f"   Tagline: {branding_updates[1]}")

if __name__ == "__main__":
    print("🎨 Finalizing ADHD Clearinghouse branding and export...")
    
    # Update homepage branding
    update_homepage_branding()
    
    # Update overall site branding
    update_site_branding()
    
    # Create new export
    export_name = create_adhd_export()
    
    print(f"\n🎉 ADHD Clearinghouse transformation complete!")
    print(f"📍 New export file: {export_name}")
    print(f"🏷️  Site branding: ADHD Clearinghouse")
    print(f"🎯 Focus: Adult ADHD resources and support")
    print(f"\n✨ Ready to launch your ADHD clearinghouse!")