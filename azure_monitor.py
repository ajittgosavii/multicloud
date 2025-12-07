"""
Azure Monitor
Handles Azure Monitor, Log Analytics, and Application Insights
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
from datetime import datetime, timedelta

@dataclass
class MetricData:
    """Metric data model"""
    timestamp: datetime
    value: float
    unit: str
    aggregation: str

@dataclass
class Alert:
    """Alert model"""
    alert_id: str
    name: str
    severity: str
    status: str
    resource: str
    description: str
    fired_time: datetime
    resolved_time: Optional[datetime] = None

@dataclass
class LogAnalyticsWorkspace:
    """Log Analytics Workspace model"""
    name: str
    resource_group: str
    location: str
    workspace_id: str
    retention_days: int
    sku: str

class AzureMonitorService:
    """Azure Monitor Service operations"""
    
    @staticmethod
    def get_resource_metrics(resource_id: str, metric_name: str, timespan: str = "PT1H", interval: str = "PT5M") -> List[MetricData]:
        """Get metrics for a specific resource"""
        # Placeholder for Azure SDK integration
        # from azure.mgmt.monitor import MonitorManagementClient
        
        # Demo data - CPU usage for last hour
        import random
        metrics = []
        now = datetime.now()
        
        for i in range(12):  # 12 data points for 1 hour with 5-min intervals
            metrics.append(MetricData(
                timestamp=now - timedelta(minutes=i*5),
                value=random.uniform(30, 80),
                unit="Percent",
                aggregation="Average"
            ))
        
        return metrics
    
    @staticmethod
    def get_available_metrics(resource_type: str) -> List[str]:
        """Get available metrics for resource type"""
        metrics_by_type = {
            "Microsoft.Compute/virtualMachines": [
                "Percentage CPU",
                "Network In Total",
                "Network Out Total",
                "Disk Read Bytes",
                "Disk Write Bytes",
                "Available Memory Bytes"
            ],
            "Microsoft.Sql/servers/databases": [
                "cpu_percent",
                "storage_percent",
                "connection_successful",
                "connection_failed",
                "blocked_by_firewall",
                "dtu_consumption_percent"
            ],
            "Microsoft.Storage/storageAccounts": [
                "Transactions",
                "Ingress",
                "Egress",
                "SuccessServerLatency",
                "Availability",
                "UsedCapacity"
            ],
            "Microsoft.ContainerService/managedClusters": [
                "node_cpu_usage_percentage",
                "node_memory_working_set_percentage",
                "kube_pod_status_ready",
                "cluster_autoscaler_unschedulable_pods_count"
            ]
        }
        
        return metrics_by_type.get(resource_type, ["cpu_percent", "memory_percent"])
    
    @staticmethod
    def create_metric_alert(alert_config: Dict) -> bool:
        """Create metric alert rule"""
        # alert_client.metric_alerts.create_or_update(...)
        return True
    
    @staticmethod
    def list_alerts(subscription_id: str, time_range: str = "P1D") -> List[Alert]:
        """List active and recent alerts"""
        return [
            Alert(
                alert_id="alert-001",
                name="High CPU Usage on prod-vm-01",
                severity="High",
                status="Fired",
                resource="prod-vm-01",
                description="CPU usage exceeded 80% threshold",
                fired_time=datetime.now() - timedelta(hours=2)
            ),
            Alert(
                alert_id="alert-002",
                name="Database connection failures",
                severity="Medium",
                status="Resolved",
                resource="prod-sqldb-main",
                description="Connection failures exceeded threshold",
                fired_time=datetime.now() - timedelta(hours=5),
                resolved_time=datetime.now() - timedelta(hours=4)
            ),
            Alert(
                alert_id="alert-003",
                name="High memory usage on AKS cluster",
                severity="Warning",
                status="Fired",
                resource="prod-aks-east",
                description="Memory usage exceeded 75% threshold",
                fired_time=datetime.now() - timedelta(minutes=30)
            )
        ]
    
    @staticmethod
    def resolve_alert(alert_id: str) -> bool:
        """Manually resolve an alert"""
        return True
    
    @staticmethod
    def list_log_analytics_workspaces(subscription_id: str, resource_group: str = None) -> List[LogAnalyticsWorkspace]:
        """List Log Analytics workspaces"""
        return [
            LogAnalyticsWorkspace(
                name="prod-log-analytics",
                resource_group="Monitoring-RG",
                location="East US",
                workspace_id="12345678-1234-1234-1234-123456789012",
                retention_days=90,
                sku="PerGB2018"
            ),
            LogAnalyticsWorkspace(
                name="dev-log-analytics",
                resource_group="Development-RG",
                location="West US",
                workspace_id="87654321-4321-4321-4321-210987654321",
                retention_days=30,
                sku="PerGB2018"
            )
        ]
    
    @staticmethod
    def query_logs(workspace_id: str, query: str, timespan: str = "P1D") -> List[Dict]:
        """Query logs using KQL (Kusto Query Language)"""
        # from azure.monitor.query import LogsQueryClient
        
        # Demo data
        return [
            {
                "TimeGenerated": datetime.now() - timedelta(hours=1),
                "Computer": "prod-vm-01",
                "EventLevel": "Error",
                "Message": "Application error occurred"
            },
            {
                "TimeGenerated": datetime.now() - timedelta(hours=2),
                "Computer": "prod-vm-02",
                "EventLevel": "Warning",
                "Message": "High memory usage detected"
            }
        ]
    
    @staticmethod
    def create_action_group(action_group_config: Dict) -> bool:
        """Create action group for alert notifications"""
        return True
    
    @staticmethod
    def list_action_groups(subscription_id: str, resource_group: str = None) -> List[Dict]:
        """List action groups"""
        return [
            {
                "name": "critical-alerts",
                "email_receivers": ["oncall@company.com", "admin@company.com"],
                "sms_receivers": ["+1-555-0100"],
                "webhook_receivers": ["https://alerts.company.com/webhook"]
            },
            {
                "name": "warning-alerts",
                "email_receivers": ["team@company.com"],
                "sms_receivers": [],
                "webhook_receivers": []
            }
        ]
    
    @staticmethod
    def get_application_insights(resource_group: str, app_insights_name: str) -> Dict:
        """Get Application Insights details"""
        return {
            "name": app_insights_name,
            "instrumentation_key": "12345678-1234-1234-1234-123456789012",
            "connection_string": "InstrumentationKey=12345678-1234-1234-1234-123456789012",
            "location": "East US",
            "application_type": "web"
        }
    
    @staticmethod
    def query_application_insights(app_insights_id: str, query: str, timespan: str = "P1D") -> List[Dict]:
        """Query Application Insights telemetry"""
        return [
            {
                "timestamp": datetime.now() - timedelta(hours=1),
                "name": "GET /api/users",
                "duration": 125.5,
                "success": True,
                "resultCode": "200"
            },
            {
                "timestamp": datetime.now() - timedelta(hours=2),
                "name": "POST /api/orders",
                "duration": 345.2,
                "success": False,
                "resultCode": "500"
            }
        ]
    
    @staticmethod
    def get_service_health_events(subscription_id: str) -> List[Dict]:
        """Get Azure service health events"""
        return [
            {
                "title": "Virtual Machines - East US - Informational",
                "status": "Active",
                "level": "Informational",
                "impact_start_time": datetime.now() - timedelta(hours=6),
                "summary": "Planned maintenance in East US region"
            }
        ]
    
    @staticmethod
    def create_diagnostic_settings(resource_id: str, workspace_id: str, categories: List[str]) -> bool:
        """Configure diagnostic settings for resource"""
        # Send logs to Log Analytics workspace
        return True
    
    @staticmethod
    def get_activity_logs(subscription_id: str, timespan: str = "P1D", filter_string: str = None) -> List[Dict]:
        """Get Azure Activity Logs"""
        return [
            {
                "timestamp": datetime.now() - timedelta(hours=2),
                "operation": "Microsoft.Compute/virtualMachines/write",
                "status": "Succeeded",
                "caller": "john.doe@company.com",
                "resource": "prod-vm-01"
            },
            {
                "timestamp": datetime.now() - timedelta(hours=5),
                "operation": "Microsoft.Storage/storageAccounts/delete",
                "status": "Succeeded",
                "caller": "cleanup-automation",
                "resource": "temp-storage-001"
            }
        ]
