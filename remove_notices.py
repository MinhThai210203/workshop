import os
import re

def remove_notice_blocks(content):
    """Remove all notice blocks from markdown content"""
    # Pattern to match notice blocks including their content
    pattern = r'\{\{%\s*notice\s+(tip|info|warning|note)\s*%\}\}.*?\{\{%\s*/notice\s*%\}\}\n*'
    content = re.sub(pattern, '', content, flags=re.DOTALL)
    return content

def process_file(filepath):
    """Process a single markdown file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        content = remove_notice_blocks(content)
        
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    workshop_path = r"d:\workshop\fcj-workshop-template\content\5-Workshop"
    count = 0
    
    for root, dirs, files in os.walk(workshop_path):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                if process_file(filepath):
                    count += 1
                    print(f"Processed: {filepath}")
    
    print(f"\nTotal files modified: {count}")

if __name__ == "__main__":
    main()
