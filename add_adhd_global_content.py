#!/usr/bin/env python3
"""
Complete ADHD transformation script - updates global settings, pages, and navigation
"""

import json
import shutil
import os
from datetime import datetime

def create_adhd_global_content():
    """Create global settings for ADHD clearinghouse"""
    
    # Create backup of original data
    shutil.copy('/workspace/strapi/strapi/data/entities/entities_00001.jsonl', 
                '/workspace/strapi/strapi/data/entities/entities_00001_backup.jsonl')
    
    # Read current entities
    with open('/workspace/strapi/strapi/data/entities/entities_00001.jsonl', 'r') as f:
        current_entities = [json.loads(line) for line in f if line.strip()]
    
    # Add global and page content for ADHD
    new_entities = [
        {
            "type": "api::global.global",
            "id": 100,
            "data": {
                "documentId": "adhd-global-settings",
                "seo": {
                    "metaTitle": "ADHD Clearinghouse - Your ADHD Resource Hub",
                    "metaDescription": "Comprehensive ADHD resources, expert guidance, and practical strategies. From diagnosis to daily living, find the support you need to thrive with ADHD.",
                    "keywords": "ADHD clearinghouse, ADHD resources, adult ADHD, ADHD support, ADHD strategies",
                    "metaRobots": "index, follow",
                    "structuredData": None,
                    "metaViewport": "width=device-width, initial-scale=1",
                    "canonicalURL": None
                },
                "navbar": {
                    "displayName": "ADHD Clearinghouse Navigation",
                    "links": [
                        {
                            "url": "/",
                            "text": "Home",
                            "newTab": False
                        },
                        {
                            "url": "/blog",
                            "text": "Resources",
                            "newTab": False
                        },
                        {
                            "url": "/symptoms-diagnosis",
                            "text": "Symptoms & Diagnosis",
                            "newTab": False
                        },
                        {
                            "url": "/treatment",
                            "text": "Treatment",
                            "newTab": False
                        },
                        {
                            "url": "/strategies",
                            "text": "Daily Strategies",
                            "newTab": False
                        },
                        {
                            "url": "/workplace",
                            "text": "Workplace",
                            "newTab": False
                        }
                    ]
                },
                "footer": {
                    "displayName": "ADHD Clearinghouse Footer",
                    "columns": [
                        {
                            "title": "Quick Links",
                            "links": [
                                {
                                    "url": "/",
                                    "text": "Home"
                                },
                                {
                                    "url": "/blog",
                                    "text": "Latest Articles"
                                },
                                {
                                    "url": "/about",
                                    "text": "About Us"
                                },
                                {
                                    "url": "/contact",
                                    "text": "Contact"
                                }
                            ]
                        },
                        {
                            "title": "Resources",
                            "links": [
                                {
                                    "url": "/symptoms",
                                    "text": "ADHD Symptoms"
                                },
                                {
                                    "url": "/treatment",
                                    "text": "Treatment Options"
                                },
                                {
                                    "url": "/workplace",
                                    "text": "Workplace Strategies"
                                },
                                {
                                    "url": "/relationships",
                                    "text": "Relationships"
                                }
                            ]
                        },
                        {
                            "title": "Support",
                            "links": [
                                {
                                    "url": "/faq",
                                    "text": "FAQ"
                                },
                                {
                                    "url": "/helplines",
                                    "text": "Crisis Helplines"
                                },
                                {
                                    "url": "/support-groups",
                                    "text": "Find Support Groups"
                                },
                                {
                                    "url": "/professionals",
                                    "text": "Find Professionals"
                                }
                            ]
                        },
                        {
                            "title": "Organizations",
                            "links": [
                                {
                                    "url": "https://www.adhd.org",
                                    "text": "CHADD"
                                },
                                {
                                    "url": "https://www.additude.org",
                                    "text": "ADDitude Magazine"
                                },
                                {
                                    "url": "https://www.adhdfoundation.org",
                                    "text": "ADHD Foundation"
                                },
                                {
                                    "url": "https://www.cdc.gov/ncbddd/adhd",
                                    "text": "CDC ADHD Info"
                                }
                            ]
                        }
                    ],
                    "copyright": {
                        "text": "© 2025 ADHD Clearinghouse. This site provides educational information only and is not a substitute for professional medical advice."
                    },
                    "socialLinks": [
                        {
                            "url": "https://twitter.com/adhdclearinghouse",
                            "text": "Twitter",
                            "newTab": True
                        },
                        {
                            "url": "https://facebook.com/adhdclearinghouse",
                            "text": "Facebook",
                            "newTab": True
                        }
                    ]
                },
                "createdAt": "2024-08-01T13:39:26.851Z",
                "updatedAt": "2025-01-16T16:00:00.000Z",
                "publishedAt": "2025-01-16T16:00:00.000Z",
                "locale": "en"
            }
        },
        {
            "type": "api::page.page",
            "id": 101,
            "data": {
                "documentId": "adhd-homepage",
                "title": "ADHD Clearinghouse - Your Complete ADHD Resource",
                "description": "Welcome to the ADHD Clearinghouse - your comprehensive resource for understanding, managing, and thriving with ADHD. Find expert guidance, practical strategies, and supportive community.",
                "slug": "homepage",
                "content": [
                    {
                        "type": "heading",
                        "children": [{"type": "text", "text": "Welcome to the ADHD Clearinghouse"}],
                        "level": 1
                    },
                    {
                        "type": "paragraph",
                        "children": [{"type": "text", "text": "Your comprehensive resource for understanding, managing, and thriving with ADHD. We provide evidence-based information, practical strategies, and a supportive community to help you navigate life with ADHD."}]
                    },
                    {
                        "type": "heading",
                        "children": [{"type": "text", "text": "What We Offer"}],
                        "level": 2
                    },
                    {
                        "type": "paragraph",
                        "children": [{"type": "text", "text": "Our ADHD clearinghouse brings together expert guidance, research-based strategies, and real-world solutions for adults living with ADHD."}]
                    },
                    {
                        "type": "list",
                        "format": "unordered",
                        "children": [
                            {"type": "list-item", "children": [{"type": "text", "text": "Comprehensive symptom guides and self-assessment tools"}]},
                            {"type": "list-item", "children": [{"type": "text", "text": "Treatment options and medication information"}]},
                            {"type": "list-item", "children": [{"type": "text", "text": "Workplace strategies and accommodation guides"}]},
                            {"type": "list-item", "children": [{"type": "text", "text": "Relationship and family resources"}]},
                            {"type": "list-item", "children": [{"type": "text", "text": "Daily living strategies and life hacks"}]},
                            {"type": "list-item", "children": [{"type": "text", "text": "Latest research and scientific updates"}]}
                        ]
                    }
                ],
                "createdAt": "2024-09-16T12:25:00.000Z",
                "updatedAt": "2025-01-16T16:00:00.000Z",
                "publishedAt": "2024-09-16T12:25:00.000Z",
                "locale": "en",
                "seo": {
                    "metaTitle": "ADHD Clearinghouse - Your Complete ADHD Resource",
                    "metaDescription": "Comprehensive ADHD resources, expert guidance, and practical strategies. From symptoms to treatment, find everything you need to thrive with ADHD.",
                    "keywords": "ADHD, ADHD resources, ADHD guide, adult ADHD, ADHD symptoms, ADHD treatment",
                    "metaRobots": "index, follow"
                }
            }
        },
        {
            "type": "api::page.page",
            "id": 102,
            "data": {
                "documentId": "adhd-about-page",
                "title": "About ADHD Clearinghouse",
                "description": "Learn about our mission to provide comprehensive, evidence-based ADHD resources and support for adults navigating life with ADHD.",
                "slug": "about",
                "content": [
                    {
                        "type": "heading",
                        "children": [{"type": "text", "text": "About the ADHD Clearinghouse"}],
                        "level": 1
                    },
                    {
                        "type": "paragraph",
                        "children": [{"type": "text", "text": "The ADHD Clearinghouse was created to bridge the gap between clinical research and everyday life for adults with ADHD. We believe that everyone deserves access to accurate, helpful information about ADHD."}]
                    },
                    {
                        "type": "heading",
                        "children": [{"type": "text", "text": "Our Mission"}],
                        "level": 2
                    },
                    {
                        "type": "paragraph",
                        "children": [{"type": "text", "text": "To provide comprehensive, evidence-based resources that help adults with ADHD understand their condition, access appropriate treatment, and develop practical strategies for success."}]
                    },
                    {
                        "type": "heading",
                        "children": [{"type": "text", "text": "What Makes Us Different"}],
                        "level": 2
                    },
                    {
                        "type": "paragraph",
                        "children": [{"type": "text", "text": "We focus specifically on adult ADHD, recognizing that the challenges and needs of adults differ significantly from those of children. Our content is created by professionals and reviewed by medical experts."}]
                    },
                    {
                        "type": "heading",
                        "children": [{"type": "text", "text": "Our Commitment"}],
                        "level": 2
                    },
                    {
                        "type": "paragraph",
                        "children": [{"type": "text", "text": "We are committed to providing accurate, up-to-date information that empowers individuals with ADHD to make informed decisions about their health and wellbeing."}]
                    }
                ],
                "createdAt": "2024-09-16T12:26:00.000Z",
                "updatedAt": "2025-01-16T16:00:00.000Z",
                "publishedAt": "2024-09-16T12:26:00.000Z",
                "locale": "en",
                "seo": {
                    "metaTitle": "About ADHD Clearinghouse - Our Mission & Values",
                    "metaDescription": "Learn about our mission to provide comprehensive ADHD resources and support for adults with ADHD. Evidence-based information you can trust.",
                    "keywords": "ADHD clearinghouse about, ADHD resources mission, adult ADHD support"
                }
            }
        }
    ]
    
    # Add these entities to the current ones
    current_entities.extend(new_entities)
    
    # Write back to file
    with open('/workspace/strapi/strapi/data/entities/entities_00001.jsonl', 'w') as f:
        for entity in current_entities:
            f.write(json.dumps(entity) + '\n')
    
    print(f"✅ Added {len(new_entities)} global/page entities for ADHD clearinghouse")
    return len(new_entities)

def create_adhd_faq_content():
    """Create FAQ content for ADHD"""
    
    with open('/workspace/strapi/strapi/data/entities/entities_00001.jsonl', 'r') as f:
        current_entities = [json.loads(line) for line in f if line.strip()]
    
    faq_entities = [
        {
            "type": "api::faq.faq",
            "id": 200,
            "data": {
                "documentId": "what-is-adhd",
                "question": "What is ADHD and how is it diagnosed in adults?",
                "answer": "ADHD (Attention Deficit Hyperactivity Disorder) is a neurodevelopmental condition that affects attention, impulse control, and activity levels. In adults, diagnosis involves a comprehensive evaluation by a qualified healthcare professional, typically including a review of childhood symptoms, current functioning, and ruling out other conditions.",
                "createdAt": "2024-09-16T12:35:00.000Z",
                "updatedAt": "2025-01-16T16:00:00.000Z",
                "publishedAt": "2024-09-16T12:35:00.000Z",
                "locale": "en"
            }
        },
        {
            "type": "api::faq.faq",
            "id": 201,
            "data": {
                "documentId": "adhd-treatment-options",
                "question": "What treatment options are available for adult ADHD?",
                "answer": "ADHD treatment for adults typically includes a combination of medication (stimulants like methylphenidate or amphetamines, or non-stimulants), behavioral therapy, coaching, and lifestyle modifications. Treatment plans are individualized based on symptoms, lifestyle, and personal preferences.",
                "createdAt": "2024-09-16T12:36:00.000Z",
                "updatedAt": "2025-01-16T16:00:00.000Z",
                "publishedAt": "2024-09-16T12:36:00.000Z",
                "locale": "en"
            }
        },
        {
            "type": "api::faq.faq",
            "id": 202,
            "data": {
                "documentId": "adhd-workplace-accommodations",
                "question": "What workplace accommodations are available for employees with ADHD?",
                "answer": "Under the Americans with Disabilities Act, employees with ADHD may be entitled to accommodations such as flexible work hours, quiet workspaces, extended time for tasks, written instructions for verbal directions, and assistive technology. These accommodations help individuals perform at their best.",
                "createdAt": "2024-09-16T12:37:00.000Z",
                "updatedAt": "2025-01-16T16:00:00.000Z",
                "publishedAt": "2024-09-16T12:37:00.000Z",
                "locale": "en"
            }
        }
    ]
    
    current_entities.extend(faq_entities)
    
    with open('/workspace/strapi/strapi/data/entities/entities_00001.jsonl', 'w') as f:
        for entity in current_entities:
            f.write(json.dumps(entity) + '\n')
    
    print(f"✅ Added {len(faq_entities)} FAQ entities for ADHD")
    return len(faq_entities)

if __name__ == "__main__":
    print("🚀 Creating comprehensive ADHD Clearinghouse content...")
    
    # Add global settings and pages
    global_added = create_adhd_global_content()
    
    # Add FAQ content
    faq_added = create_adhd_faq_content()
    
    print(f"\n🎉 ADHD Clearinghouse transformation complete!")
    print(f"📊 Total entities added:")
    print(f"   - Global settings & pages: {global_added}")
    print(f"   - FAQ items: {faq_added}")
    print(f"\n✨ The site is now ready with ADHD-focused content!")
    print(f"📍 Original backup saved as: entities_00001_backup.jsonl")