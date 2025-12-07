"""
Azure Database Services
Handles Azure SQL, Cosmos DB, PostgreSQL, MySQL
"""

from dataclasses import dataclass
from typing import List

@dataclass
class AzureSQLDatabase:
    """Azure SQL Database model"""
    name: str
    server_name: str
    resource_group: str
    location: str
    tier: str
    size: str
    
class AzureDatabaseService:
    """Azure Database Service operations"""
    
    @staticmethod
    def list_sql_databases(subscription_id: str) -> List[AzureSQLDatabase]:
        """List SQL databases"""
        return [
            AzureSQLDatabase(
                name="prod-sqldb-main",
                server_name="prod-sql-server-01",
                resource_group="Database-RG",
                location="East US",
                tier="General Purpose",
                size="GP_Gen5_2"
            )
        ]
