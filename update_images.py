import os
import re

# Mapping of correct image paths for each section
image_mappings = {
    # Lambda section (4 images)
    '5.8-lambda': [
        ('001-create-function.png', 'Create function'),
        ('002-placeholder-code.png', 'Placeholder code'),
        ('003-env-vars.png', 'Environment variables'),
        ('004-sqs-trigger.png', 'SQS trigger')
    ],
    # API Gateway section (4 images)
    '5.9-api': [
        ('001-create-api.png', 'Create API'),
        ('002-cognito-authorizer.png', 'Cognito authorizer'),
        ('003-create-resource-method.png', 'Create resource/method'),
        ('004-invoke-url.png', 'Invoke URL')
    ],
    # CloudFront section (2 images)
    '5.10-cloudfront': [
        ('001-cloudfront-config.png', 'CloudFront configuration'),
        ('002-domain-error-pages.png', 'Domain and error pages')
    ],
    # Monitoring section (1 image)
    '5.11-monitoring': [
        ('001-sns-subscription.png', 'SNS subscription')
    ],
    # Route 53 section (5 images)
    '5.12-route53': [
        ('001-route53-hosted-zone.png', 'Hosted zone'),
        ('002-namecheap-custom-dns.png', 'Namecheap DNS'),
        ('003-acm-request-cert.png', 'ACM certificate'),
        ('004-cloudfront-custom-domain.png', 'CloudFront domain'),
        ('005-route53-alias-record.png', 'Route 53 alias')
    ]
}

# Files to update for Lambda
lambda_files = [
    'd:\\workshop\\fcj-workshop-template\\content\\5-Workshop\\5.8-lambda\\5.8.1-create-functions\\_index.vi.md',
    'd:\\workshop\\fcj-workshop-template\\content\\5-Workshop\\5.8-lambda\\5.8.1-create-functions\\_index.md',
    'd:\\workshop\\fcj-workshop-template\\content\\5-Workshop\\5.8-lambda\\5.8.2-env-vars\\_index.vi.md',
    'd:\\workshop\\fcj-workshop-template\\content\\5-Workshop\\5.8-lambda\\5.8.2-env-vars\\_index.md',
    'd:\\workshop\\fcj-workshop-template\\content\\5-Workshop\\5.8-lambda\\5.8.3-sqs-trigger\\_index.vi.md',
    'd:\\workshop\\fcj-workshop-template\\content\\5-Workshop\\5.8-lambda\\5.8.3-sqs-trigger\\_index.md',
]

# Files to update for API Gateway
api_files = [
    'd:\\workshop\\fcj-workshop-template\\content\\5-Workshop\\5.9-api-gateway\\5.9.1-create-api\\_index.vi.md',
    'd:\\workshop\\fcj-workshop-template\\content\\5-Workshop\\5.9-api-gateway\\5.9.1-create-api\\_index.md',
    'd:\\workshop\\fcj-workshop-template\\content\\5-Workshop\\5.9-api-gateway\\5.9.2-authorizer\\_index.vi.md',
    'd:\\workshop\\fcj-workshop-template\\content\\5-Workshop\\5.9-api-gateway\\5.9.2-authorizer\\_index.md',
    'd:\\workshop\\fcj-workshop-template\\content\\5-Workshop\\5.9-api-gateway\\5.9.3-resources\\_index.vi.md',
    'd:\\workshop\\fcj-workshop-template\\content\\5-Workshop\\5.9-api-gateway\\5.9.3-resources\\_index.md',
    'd:\\workshop\\fcj-workshop-template\\content\\5-Workshop\\5.9-api-gateway\\5.9.4-deploy\\_index.vi.md',
    'd:\\workshop\\fcj-workshop-template\\content\\5-Workshop\\5.9-api-gateway\\5.9.4-deploy\\_index.md',
]

# Files to update for CloudFront
cloudfront_files = [
    'd:\\workshop\\fcj-workshop-template\\content\\5-Workshop\\5.10-cloudfront\\_index.vi.md',
    'd:\\workshop\\fcj-workshop-template\\content\\5-Workshop\\5.10-cloudfront\\_index.md',
]

# Files to update for Monitoring
monitoring_files = [
    'd:\\workshop\\fcj-workshop-template\\content\\5-Workshop\\5.12-monitoring\\_index.vi.md',
    'd:\\workshop\\fcj-workshop-template\\content\\5-Workshop\\5.12-monitoring\\_index.md',
]

# Files to update for Route 53
route53_files = [
    'd:\\workshop\\fcj-workshop-template\\content\\5-Workshop\\5.11-route53-ssl\\_index.vi.md',
    'd:\\workshop\\fcj-workshop-template\\content\\5-Workshop\\5.11-route53-ssl\\_index.md',
]

def remove_wrong_image_refs(content):
    """Remove incorrect image references from markdown"""
    # Remove all image markdown syntax
    content = re.sub(r'!\[.*?\]\(/images/5-Workshop/[^\)]+\)', '', content)
    return content

print("Image path update script created!")
print("Run this script to update all workshop files with correct image paths")
