#!/usr/bin/env python3
"""
Batch update image paths in workshop markdown files
"""
import re
from pathlib import Path

def update_file(filepath, replacements):
    """Update a file with multiple replacements"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        for old, new in replacements:
            content = content.replace(old, new)
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Updated: {filepath}")
            return True
        else:
            print(f"⏭️  Skipped (no changes): {filepath}")
            return False
    except Exception as e:
        print(f"❌ Error updating {filepath}: {e}")
        return False

# API Gateway English files
api_en_files = {
    r'd:\workshop\fcj-workshop-template\content\5-Workshop\5.9-api-gateway\5.9.1-create-api\_index.md': [
        ('![API Gateway Console](/images/5-Workshop/5.9-api/001-api-console.png)', ''),
        ('![Create REST API](/images/5-Workshop/5.9-api/002-create-rest-api.png)', ''),
        ('![API Settings](/images/5-Workshop/5.9-api/003-api-settings.png)', '![Create API](/images/5-Workshop/5.9-api/001-create-api.png)'),
        ('![API Created](/images/5-Workshop/5.9-api/004-api-created.png)', ''),
    ],
    r'd:\workshop\fcj-workshop-template\content\5-Workshop\5.9-api-gateway\5.9.2-authorizer\_index.md': [
        ('![Create Authorizer](/images/5-Workshop/5.9-api/005-create-authorizer.png)', ''),
        ('![Authorizer Config](/images/5-Workshop/5.9-api/006-authorizer-config.png)', '![Cognito Authorizer](/images/5-Workshop/5.9-api/002-cognito-authorizer.png)'),
        ('![Authorizer Created](/images/5-Workshop/5.9-api/007-authorizer-created.png)', ''),
    ],
    r'd:\workshop\fcj-workshop-template\content\5-Workshop\5.9-api-gateway\5.9.3-resources\_index.md': [
        ('![Create Resource](/images/5-Workshop/5.9-api/008-create-resource.png)', ''),
        ('![Create Method](/images/5-Workshop/5.9-api/009-create-method.png)', ''),
        ('![Method Authorization](/images/5-Workshop/5.9-api/010-method-auth.png)', '![Create Resource Method](/images/5-Workshop/5.9-api/003-create-resource-method.png)'),
        ('![All Resources](/images/5-Workshop/5.9-api/011-all-resources.png)', ''),
    ],
    r'd:\workshop\fcj-workshop-template\content\5-Workshop\5.9-api-gateway\5.9.4-deploy\_index.md': [
        ('![Deploy API](/images/5-Workshop/5.9-api/012-deploy-api.png)', ''),
        ('![Stage Settings](/images/5-Workshop/5.9-api/013-stage-settings.png)', ''),
        ('![Invoke URL](/images/5-Workshop/5.9-api/014-invoke-url.png)', '![Invoke URL](/images/5-Workshop/5.9-api/004-invoke-url.png)'),
        ('![Throttling](/images/5-Workshop/5.9-api/015-throttling.png)', ''),
    ],
}

# CloudFront files
cloudfront_files = {
    r'd:\workshop\fcj-workshop-template\content\5-Workshop\5.10-cloudfront\_index.vi.md': 'vi',
    r'd:\workshop\fcj-workshop-template\content\5-Workshop\5.10-cloudfront\_index.md': 'en',
}

# Monitoring files
monitoring_files = {
    r'd:\workshop\fcj-workshop-template\content\5-Workshop\5.12-monitoring\_index.vi.md': 'vi',
    r'd:\workshop\fcj-workshop-template\content\5-Workshop\5.12-monitoring\_index.md': 'en',
}

# Route53 files
route53_files = {
    r'd:\workshop\fcj-workshop-template\content\5-Workshop\5.11-route53-ssl\_index.vi.md': 'vi',
    r'd:\workshop\fcj-workshop-template\content\5-Workshop\5.11-route53-ssl\_index.md': 'en',
}

def main():
    print("🚀 Batch updating image paths...")
    print("=" * 60)
    
    # Update API Gateway English files
    print("\n📁 API Gateway (English):")
    for filepath, replacements in api_en_files.items():
        update_file(filepath, replacements)
    
    print("\n✨ Done!")

if __name__ == '__main__':
    main()
