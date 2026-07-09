#!/usr/bin/env python3
"""
Blog Image Downloader for The Low Blood Sugar Solution
Downloads free stock images from Unsplash for blog posts.

Usage:
    python download_blog_images.py

Requirements:
    pip install requests
"""

import requests
import os
import time
from urllib.parse import urlparse

# Create directories
os.makedirs('images/blog', exist_ok=True)

# Unsplash Source API (free, no API key needed for basic usage)
# Format: https://source.unsplash.com/{WIDTH}x{HEIGHT}/?{KEYWORD}
# Note: Unsplash Source is deprecated. Using Unsplash API or direct URLs instead.

# Better approach: Use Lorem Picsum or direct Unsplash image IDs
# These are curated direct links to free Unsplash images

BLOG_IMAGES = {
    # Featured post - Emergency response / medical
    'featured-post.jpg': {
        'url': 'https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=800&h=600&fit=crop',
        'description': 'Medical emergency kit / first aid supplies'
    },

    # Post 1 - Nutrition / healthy meal
    'post-1.jpg': {
        'url': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=600&h=400&fit=crop',
        'description': 'Healthy balanced meal with protein, vegetables, whole grains'
    },

    # Post 2 - Warning signs / symptoms
    'post-2.jpg': {
        'url': 'https://images.unsplash.com/photo-1505751172876-fa1923c5c528?w=600&h=400&fit=crop',
        'description': 'Person feeling dizzy or unwell, holding head'
    },

    # Post 3 - Meal timing / clock
    'post-3.jpg': {
        'url': 'https://images.unsplash.com/photo-1495195134817-aeb325a55b65?w=600&h=400&fit=crop',
        'description': 'Healthy breakfast spread with clock / morning routine'
    },

    # Post 4 - Stress / relaxation
    'post-4.jpg': {
        'url': 'https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=600&h=400&fit=crop',
        'description': 'Person meditating, stress relief, calm environment'
    },

    # Post 5 - Reader story / success
    'post-5.jpg': {
        'url': 'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=600&h=400&fit=crop',
        'description': 'Happy healthy person, wellness lifestyle'
    },

    # Post 6 - Foods / groceries
    'post-6.jpg': {
        'url': 'https://images.unsplash.com/photo-1542838132-92c53300491e?w=600&h=400&fit=crop',
        'description': 'Fresh groceries, fruits, vegetables, healthy food shopping'
    },

    # Post 7 - Exercise / fitness
    'post-7.jpg': {
        'url': 'https://images.unsplash.com/photo-1517836357463-d25dfeac3438?w=600&h=400&fit=crop',
        'description': 'Person exercising, running, or working out'
    },

    # Post 8 - Sleep / night
    'post-8.jpg': {
        'url': 'https://images.unsplash.com/photo-1541781774459-bb2af2f05b55?w=600&h=400&fit=crop',
        'description': 'Peaceful sleep, bedroom, night time, rest'
    },

    # Post 9 - Emergency plan / checklist
    'post-9.jpg': {
        'url': 'https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=600&h=400&fit=crop',
        'description': 'Checklist, planning, notebook, organization'
    },
}

def download_image(filename, url, description):
    """Download an image from URL and save it."""
    filepath = f'images/blog/{filename}'

    # Skip if already exists
    if os.path.exists(filepath):
        print(f"✓ {filename} already exists - skipping")
        return True

    try:
        print(f"Downloading {filename}...")
        print(f"  Description: {description}")

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()

        with open(filepath, 'wb') as f:
            f.write(response.content)

        file_size = len(response.content) / 1024  # KB
        print(f"  ✓ Saved ({file_size:.1f} KB)")

        # Be nice to the server
        time.sleep(1)
        return True

    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False

def main():
    print("=" * 60)
    print("BLOG IMAGE DOWNLOADER")
    print("The Low Blood Sugar Solution")
    print("=" * 60)
    print()

    success_count = 0
    fail_count = 0

    for filename, info in BLOG_IMAGES.items():
        if download_image(filename, info['url'], info['description']):
            success_count += 1
        else:
            fail_count += 1
        print()

    print("=" * 60)
    print(f"DOWNLOAD COMPLETE: {success_count} succeeded, {fail_count} failed")
    print("=" * 60)
    print()
    print("Images saved to: images/blog/")
    print()
    print("If any downloads failed, you can:")
    print("1. Run the script again (skips existing files)")
    print("2. Manually download from the URLs listed above")
    print("3. Use alternative free stock sites like Pexels or Pixabay")

if __name__ == '__main__':
    main()
