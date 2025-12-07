"""
Multi-Cloud Configuration Settings
Supports AWS, Azure, and GCP (coming soon)
"""

from dataclasses import dataclass
from typing import List, Dict
from enum import Enum

class CloudProvider(Enum):
    """Supported cloud providers"""
    AWS = "AWS"
    AZURE = "Azure"
    GCP = "GCP"

@dataclass
class AWSAccount:
    """AWS Account configuration"""
    account_id: str
    account_name: str
    environment: str
    status: str = 'active'
    region: str = 'us-east-1'
    tags: Dict = None

@dataclass
class AzureSubscription:
    """Azure Subscription configuration"""
    subscription_id: str
    subscription_name: str
    tenant_id: str
    environment: str
    status: str = 'active'
    location: str = 'East US'
    tags: Dict = None

@dataclass
class GCPProject:
    """GCP Project configuration (for future use)"""
    project_id: str
    project_name: str
    organization_id: str
    environment: str
    status: str = 'active'
    region: str = 'us-central1'
    tags: Dict = None

class AppConfig:
    """Application configuration"""
    
    # AWS Default Regions
    DEFAULT_REGIONS = [
        'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2',
        'eu-west-1', 'eu-west-2', 'eu-central-1',
        'ap-southeast-1', 'ap-southeast-2', 'ap-northeast-1'
    ]
    
    # Azure Default Locations
    AZURE_LOCATIONS = [
        'East US', 'East US 2', 'West US', 'West US 2', 'Central US',
        'North Europe', 'West Europe',
        'Southeast Asia', 'East Asia',
        'UK South', 'UK West',
        'Canada Central', 'Canada East',
        'Australia East', 'Australia Southeast'
    ]
    
    # GCP Default Regions (for future use)
    GCP_REGIONS = [
        'us-central1', 'us-east1', 'us-west1',
        'europe-west1', 'europe-west2',
        'asia-southeast1', 'asia-northeast1'
    ]
    
    @staticmethod
    def load_aws_accounts() -> List[AWSAccount]:
        """Load AWS accounts configuration"""
        # This would typically load from secrets.toml or database
        # For demo purposes, returning sample accounts
        return [
            AWSAccount(
                account_id="123456789012",
                account_name="Production-Main",
                environment="production",
                status="active",
                region="us-east-1",
                tags={"Department": "IT", "CostCenter": "Engineering"}
            ),
            AWSAccount(
                account_id="234567890123",
                account_name="Development",
                environment="development",
                status="active",
                region="us-west-2",
                tags={"Department": "IT", "CostCenter": "Engineering"}
            ),
            AWSAccount(
                account_id="345678901234",
                account_name="Staging",
                environment="staging",
                status="active",
                region="us-east-1",
                tags={"Department": "IT", "CostCenter": "Engineering"}
            )
        ]
    
    @staticmethod
    def load_azure_subscriptions() -> List[AzureSubscription]:
        """Load Azure subscriptions configuration"""
        # This would typically load from secrets.toml or database
        # For demo purposes, returning sample subscriptions
        return [
            AzureSubscription(
                subscription_id="12345678-1234-1234-1234-123456789012",
                subscription_name="Production-Main",
                tenant_id="87654321-4321-4321-4321-210987654321",
                environment="production",
                status="active",
                location="East US",
                tags={"Department": "IT", "CostCenter": "Engineering"}
            ),
            AzureSubscription(
                subscription_id="23456789-2345-2345-2345-234567890123",
                subscription_name="Development",
                tenant_id="87654321-4321-4321-4321-210987654321",
                environment="development",
                status="active",
                location="West US",
                tags={"Department": "IT", "CostCenter": "Engineering"}
            ),
            AzureSubscription(
                subscription_id="34567890-3456-3456-3456-345678901234",
                subscription_name="Staging",
                tenant_id="87654321-4321-4321-4321-210987654321",
                environment="staging",
                status="active",
                location="East US 2",
                tags={"Department": "IT", "CostCenter": "Engineering"}
            )
        ]
    
    @staticmethod
    def load_gcp_projects() -> List[GCPProject]:
        """Load GCP projects configuration (for future use)"""
        # Placeholder for future GCP support
        return []
    
    @staticmethod
    def get_cloud_provider_config(provider: CloudProvider) -> Dict:
        """Get configuration for specific cloud provider"""
        configs = {
            CloudProvider.AWS: {
                "regions": AppConfig.DEFAULT_REGIONS,
                "account_loader": AppConfig.load_aws_accounts
            },
            CloudProvider.AZURE: {
                "locations": AppConfig.AZURE_LOCATIONS,
                "subscription_loader": AppConfig.load_azure_subscriptions
            },
            CloudProvider.GCP: {
                "regions": AppConfig.GCP_REGIONS,
                "project_loader": AppConfig.load_gcp_projects
            }
        }
        return configs.get(provider, {})
