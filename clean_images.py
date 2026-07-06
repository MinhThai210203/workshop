import os
import re
import glob

# Get list of all actual images
actual_images = set()
workshop_img_path = r"d:\workshop\fcj-workshop-template\static\images\5-Workshop"
for root, dirs, files in os.walk(workshop_img_path):
    for file in files:
        if file.endswith('.png'):
            rel_path = os.path.relpath(os.path.join(root, file), r"d:\workshop\fcj-workshop-template\static")
            actual_images.add(rel_path.replace('\\', '/'))

print(f"Found {len(actual_images)} actual images")

# Process all markdown files
workshop_content_path = r"d:\workshop\fcj-workshop-template\content\5-Workshop"
md_files = []
for root, dirs, files in os.walk(workshop_content_path):
    for file in files:
        if file.endswith('.md'):
            md_files.append(os.path.join(root, file))

print(f"Found {len(md_files)} markdown files to process")

removed_count = 0
for md_file in md_files:
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Find all image references
        pattern = r'!\[.*?\]\(/images/(5-Workshop/[^)]+)\)'
        matches = re.findall(pattern, content)
        
        for match in matches:
            if match not in actual_images:
                # Remove this image line
                img_line_pattern = r'!\[.*?\]\(/images/' + re.escape(match) + r'\)\s*\n*'
                content = re.sub(img_line_pattern, '', content)
                removed_count += 1
                print(f"Removed: /images/{match} from {os.path.basename(md_file)}")
        
        if content != original:
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(content)
    
    except Exception as e:
        print(f"Error processing {md_file}: {e}")

print(f"\nTotal image references removed: {removed_count}")
