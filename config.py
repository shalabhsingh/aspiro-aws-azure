# AWS Resources
AWS_REGION = 'ap-south-1'

# List of EC2 instance IDs to manage
EC2_INSTANCES = [
    'i-0d916fdde0940ce2c',
]

# List of App Runner service ARNs to manage
APPRUNNER_SERVICES = [
    "arn:aws:apprunner:ap-south-1:062983354072:service/founder_sales_service/a0e6cb3da3c44fb5af090323bc2521eb", # founder_sales_service
    "arn:aws:apprunner:ap-south-1:062983354072:service/rp_backend_service/e35eb65be0be487ca77714b66b5a7756" # rp_backend_service
]

# Azure Resources
AZURE_SUBSCRIPTION_ID = 'e9a62ea2-564f-4be3-b048-36bc4d880d7c'  # Your Azure subscription ID
AZURE_RESOURCE_GROUP = 'DefaultResourceGroup-CID'   # Your Azure resource group name

# List of Azure Container Apps to manage
AZURE_CONTAINER_APPS = [
    'vocode-app',  # Example Container App name
]