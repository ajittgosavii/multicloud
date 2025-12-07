"""
Azure Storage Services
Handles Azure Storage Accounts, Blob, Files, Queues, and Tables
"""

from dataclasses import dataclass
from typing import List, Dict

@dataclass
class AzureStorageAccount:
    """Azure Storage Account model"""
    name: str
    resource_group: str
    location: str
    sku: str  # Standard_LRS, Standard_GRS, etc.
    kind: str  # StorageV2, BlobStorage, etc.
    access_tier: str  # Hot, Cool, Archive
    
class AzureStorageService:
    """Azure Storage Service operations"""
    
    @staticmethod
    def list_storage_accounts(subscription_id: str) -> List[AzureStorageAccount]:
        """List storage accounts"""
        return [
            AzureStorageAccount(
                name="prodstorageacct001",
                resource_group="Production-RG",
                location="East US",
                sku="Standard_GRS",
                kind="StorageV2",
                access_tier="Hot"
            )
        ]
    
    @staticmethod
    def get_account_sizes() -> List[str]:
        """Get available storage account SKUs"""
        return [
            "Standard_LRS", "Standard_GRS", "Standard_RAGRS",
            "Standard_ZRS", "Premium_LRS", "Premium_ZRS"
        ]
