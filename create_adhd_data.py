#!/usr/bin/env python3
"""
Script to create ADHD-focused content to replace the LaunchPad demo content.
This will transform the existing content structure to be about ADHD topics.
"""

import json
from datetime import datetime, timedelta

# ADHD-focused article content
adhd_articles = [
    {
        "documentId": "adhd-intro-guide",
        "title": "Understanding ADHD: A Comprehensive Guide for Adults",
        "description": "Discover what ADHD really means for adults, from symptoms and diagnosis to treatment options and daily life strategies. This comprehensive guide provides evidence-based insights to help you navigate life with ADHD.",
        "slug": "understanding-adhd-comprehensive-guide-adults",
        "content": [
            {
                "type": "paragraph",
                "children": [{"type": "text", "text": "Attention Deficit Hyperactivity Disorder (ADHD) affects millions of adults worldwide, yet it's often misunderstood. Far from being just a childhood condition, ADHD persists into adulthood for about 60% of those diagnosed. This guide will help you understand what ADHD really means for adults, from recognizing symptoms to finding effective treatments."}]
            },
            {
                "type": "heading",
                "children": [{"type": "text", "text": "What is Adult ADHD?"}],
                "level": 3
            },
            {
                "type": "paragraph",
                "children": [{"type": "text", "text": "Adult ADHD is a neurodevelopmental condition that affects attention, impulse control, and activity levels. While symptoms may present differently in adults than in children, the core challenges remain the same. Adults with ADHD often struggle with organization, time management, maintaining focus, and regulating emotions."}]
            },
            {
                "type": "heading",
                "children": [{"type": "text", "text": "Common Symptoms in Adults"}],
                "level": 3
            },
            {
                "type": "list",
                "format": "unordered",
                "children": [
                    {"type": "list-item", "children": [{"type": "text", "text": "Difficulty sustaining attention on tasks", "bold": True}]},
                    {"type": "list-item", "children": [{"type": "text", "text": "Procrastination and difficulty meeting deadlines", "bold": True}]},
                    {"type": "list-item", "children": [{"type": "text", "text": "Restlessness and feeling constantly 'on the go'", "bold": True}]},
                    {"type": "list-item", "children": [{"type": "text", "text": "Impulsive decision-making", "bold": True}]},
                    {"type": "list-item", "children": [{"type": "text", "text": "Mood swings and emotional regulation challenges", "bold": True}]},
                    {"type": "list-item", "children": [{"type": "text", "text": "Difficulty organizing tasks and activities", "bold": True}]}
                ]
            },
            {
                "type": "heading",
                "children": [{"type": "text", "text": "Diagnosis Process"}],
                "level": 3
            },
            {
                "type": "paragraph",
                "children": [{"type": "text", "text": "Getting an ADHD diagnosis as an adult involves a comprehensive evaluation by a qualified healthcare professional. This typically includes reviewing childhood history, current symptoms, and ruling out other conditions. Don't let misperceptions about ADHD stop you from seeking help."}]
            },
            {
                "type": "heading",
                "children": [{"type": "text", "text": "Treatment Options"}],
                "level": 3
            },
            {
                "type": "paragraph",
                "children": [{"type": "text", "text": "ADHD treatment for adults often combines medication with behavioral interventions and lifestyle changes. Stimulant medications like methylphenidate and amphetamines are commonly prescribed, while non-stimulant options are available for those who can't tolerate stimulants. Therapy, coaching, and support groups can provide essential coping strategies."}]
            },
            {
                "type": "heading",
                "children": [{"type": "text", "text": "Living Successfully with ADHD"}],
                "level": 2
            },
            {
                "type": "paragraph",
                "children": [{"type": "text", "text": "Living with ADHD doesn't have to mean living with constant struggle. With the right strategies, support, and treatment, many adults with ADHD lead highly successful, fulfilling lives. Focus on finding systems that work for your unique brain, not against it."}]
            }
        ],
        "locale": "en",
        "publishedAt": "2025-01-16T10:00:00.000Z",
        "seo": None,
        "dynamic_zone": [
            {
                "__component": "dynamic-zone.related-articles",
                "id": 1,
                "heading": "More ADHD Resources",
                "sub_heading": None
            }
        ]
    },
    {
        "documentId": "adhd-workplace-strategies",
        "title": "Thriving in the Workplace: ADHD Management Strategies",
        "description": "Learn practical strategies for managing ADHD symptoms in professional settings. From time management techniques to communication strategies, discover how to excel in your career while managing ADHD.",
        "slug": "thriving-workplace-adhd-management-strategies",
        "content": [
            {
                "type": "paragraph",
                "children": [{"type": "text", "text": "Managing ADHD in the workplace presents unique challenges, but with the right strategies, you can not only succeed but thrive in your professional life. This guide explores evidence-based approaches to managing ADHD symptoms while excelling in your career."}]
            },
            {
                "type": "heading",
                "children": [{"type": "text", "text": "Time Management Techniques"}],
                "level": 3
            },
            {
                "type": "paragraph",
                "children": [{"type": "text", "text": "Time management is often one of the biggest challenges for adults with ADHD. Consider breaking large tasks into smaller, manageable chunks, using time-blocking techniques, and implementing accountability systems to stay on track."}]
            },
            {
                "type": "heading",
                "children": [{"type": "text", "text": "Workspace Organization"}],
                "level": 3
            },
            {
                "type": "paragraph",
                "children": [{"type": "text", "text": "A cluttered workspace can amplify ADHD symptoms. Create systems that work with your brain rather than against it. Use visual organization tools, minimize distractions, and establish clear filing systems that make sense to you."}]
            },
            {
                "type": "heading",
                "children": [{"type": "text", "text": "Communication Strategies"}],
                "level": 3
            },
            {
                "type": "paragraph",
                "children": [{"type": "text", "text": "Communicating your ADHD needs to colleagues and supervisors can feel daunting, but it's often necessary for success. Focus on solutions and be prepared to discuss accommodations that benefit both you and your team."}]
            },
            {
                "type": "heading",
                "children": [{"type": "text", "text": "Requesting Accommodations"}],
                "level": 3
            },
            {
                "type": "paragraph",
                "children": [{"type": "text", "text": "Under the Americans with Disabilities Act, you may be entitled to workplace accommodations. These might include flexible work hours, quiet workspaces, or assistive technology. Remember, accommodations help you perform at your best."}]
            },
            {
                "type": "heading",
                "children": [{"type": "text", "text": "Building on Your ADHD Strengths"}],
                "level": 2
            },
            {
                "type": "paragraph",
                "children": [{"type": "text", "text": "Many adults with ADHD possess remarkable strengths like creativity, hyperfocus, problem-solving abilities, and innovative thinking. Don't just manage your symptoms – leverage your unique brainpower to excel in your field."}]
            }
        ],
        "locale": "en",
        "publishedAt": "2025-01-16T11:00:00.000Z",
        "seo": None,
        "dynamic_zone": [
            {
                "__component": "dynamic-zone.related-articles",
                "id": 2,
                "heading": "Professional ADHD Tips",
                "sub_heading": None
            }
        ]
    },
    {
        "documentId": "adhd-relationships-guide",
        "title": "ADHD and Relationships: Building Stronger Connections",
        "description": "Understand how ADHD affects relationships and learn strategies for building stronger connections with family, friends, and partners. Navigate the unique challenges and celebrate the unique strengths that come with ADHD.",
        "slug": "adhd-relationships-building-stronger-connections",
        "content": [
            {
                "type": "paragraph",
                "children": [{"type": "text", "text": "ADHD can significantly impact relationships, but understanding these effects and developing coping strategies can strengthen your connections with others. This guide explores the unique challenges and opportunities that come with ADHD in relationships."}]
            },
            {
                "type": "heading",
                "children": [{"type": "text", "text": "How ADHD Affects Relationships"}],
                "level": 3
            },
            {
                "type": "paragraph",
                "children": [{"type": "text", "text": "ADHD symptoms can create challenges in relationships, from forgetfulness and disorganization to impulse control issues and emotional regulation difficulties. These struggles often affect communication, shared responsibilities, and emotional intimacy."}]
            },
            {
                "type": "heading",
                "children": [{"type": "text", "text": "Communication Strategies"}],
                "level": 3
            },
            {
                "type": "paragraph",
                "children": [{"type": "text", "text": "Open, honest communication is essential for ADHD relationships. Discuss your symptoms openly, explain how they affect you, and work together to develop strategies that support both partners. Remember, understanding is the foundation of connection."}]
            },
            {
                "type": "heading",
                "children": [{"type": "text", "text": "Managing Emotional Regulation"}],
                "level": 3
            },
            {
                "type": "paragraph",
                "children": [{"type": "text", "text": "ADHD can make emotional regulation challenging, leading to intense emotional reactions or feeling overwhelmed. Learn to recognize triggers, develop coping strategies, and practice mindfulness techniques to improve emotional responses."}]
            },
            {
                "type": "heading",
                "children": [{"type": "text", "text": "ADHD Strengths in Relationships"}],
                "level": 3
            },
            {
                "type": "paragraph",
                "children": [{"type": "text", "text": "ADHD brings unique strengths to relationships: creativity, spontaneity, passion, and the ability to see things from different perspectives. Share these strengths and help others understand how ADHD can enrich your connections."}]
            },
            {
                "type": "heading",
                "children": [{"type": "text", "text": "Seeking Professional Support"}],
                "level": 3
            },
            {
                "type": "paragraph",
                "children": [{"type": "text", "text": "Couples therapy, family counseling, or ADHD coaching can provide valuable tools for navigating relationship challenges. Don't hesitate to seek professional support when you need it."}]
            },
            {
                "type": "heading",
                "children": [{"type": "text", "text": "Building Strong Foundations"}],
                "level": 2
            },
            {
                "type": "paragraph",
                "children": [{"type": "text", "text": "Successful ADHD relationships require patience, understanding, and commitment from all parties involved. With the right strategies and support, you can build strong, lasting connections that celebrate both the challenges and strengths of ADHD."}]
            }
        ],
        "locale": "en",
        "publishedAt": "2025-01-16T12:00:00.000Z",
        "seo": None,
        "dynamic_zone": [
            {
                "__component": "dynamic-zone.related-articles",
                "id": 3,
                "heading": "Relationship Resources",
                "sub_heading": None
            }
        ]
    }
]

# ADHD-focused categories
adhd_categories = [
    {"documentId": "symptoms-diagnosis", "name": "Symptoms & Diagnosis", "locale": None},
    {"documentId": "treatment-medication", "name": "Treatment & Medication", "locale": None},
    {"documentId": "daily-living-strategies", "name": "Daily Living & Strategies", "locale": None},
    {"documentId": "workplace-education", "name": "Workplace & Education", "locale": None},
    {"documentId": "relationships-social", "name": "Relationships & Social", "locale": None},
    {"documentId": "research-science", "name": "Research & Science", "locale": None},
    {"documentId": "adhd-strengths", "name": "ADHD Strengths", "locale": None}
]

# Blog page content for ADHD
adhd_blog_page = {
    "documentId": "adhd-blog-main",
    "heading": "ADHD Resources & Insights",
    "sub_heading": "Evidence-based information, practical strategies, and personal stories to help you understand and thrive with ADHD.",
    "locale": "en",
    "publishedAt": "2025-01-16T09:00:00.000Z",
    "seo": {
        "metaTitle": "ADHD Clearinghouse - Resources & Insights",
        "metaDescription": "Comprehensive ADHD resources including symptom guides, treatment information, workplace strategies, relationship advice, and research updates. Find the support you need.",
        "keywords": "ADHD, adult ADHD, ADHD symptoms, ADHD treatment, ADHD strategies",
        "metaRobots": "index, follow",
        "structuredData": None,
        "metaViewport": "width=device-width, initial-scale=1",
        "canonicalURL": None
    },
    "dynamic_zone": []
}

print("ADHD content structure created successfully!")
print(f"Articles: {len(adhd_articles)}")
print(f"Categories: {len(adhd_categories)}")
print("Blog page: 1")