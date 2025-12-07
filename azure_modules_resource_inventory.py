"""
Azure Module: Resource Inventory
Comprehensive Azure resource tracking and inventory management
"""

import streamlit as st
import pandas as pd
from typing import Dict, List
from datetime import datetime
from azure_theme import AzureTheme
from config_settings import AppConfig
import plotly.express as px
import plotly.graph_objects as go

class AzureResourceInventoryModule:
    """Azure Resource Inventory module"""
    
    @staticmethod
    def render():
        """Render Azure resource inventory module"""
        
        st.markdown("## 📦 Azure Resource Inventory")
        st.caption("Comprehensive Azure resource tracking across all subscriptions")
        
        subscriptions = AppConfig.load_azure_subscriptions()
        active_subscriptions = [sub for sub in subscriptions if sub.status == 'active']
        
        if not active_subscriptions:
            st.warning("⚠️ No active Azure subscriptions configured.")
            return
        
        tabs = st.tabs([
            "📊 Overview",
            "🔍 Resource Explorer",
            "🏷️ Tag Explorer",
            "📈 Analytics",
            "🔄 Change Tracking",
            "📤 Export"
        ])
        
        with tabs[0]:
            AzureResourceInventoryModule._render_overview(active_subscriptions)
        
        with tabs[1]:
            AzureResourceInventoryModule._render_resource_explorer(active_subscriptions)
        
        with tabs[2]:
            AzureResourceInventoryModule._render_tag_explorer()
        
        with tabs[3]:
            AzureResourceInventoryModule._render_analytics()
        
        with tabs[4]:
            AzureResourceInventoryModule._render_change_tracking()
        
        with tabs[5]:
            AzureResourceInventoryModule._render_export()
    
    @staticmethod
    def _render_overview(subscriptions: List):
        """Render inventory overview"""
        
        st.markdown("### 📊 Resource Inventory Overview")
        
        # Key metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            AzureTheme.azure_metric_card("Total Resources", "12,847", "📦", "+458 this week")
        
        with col2:
            AzureTheme.azure_metric_card("Resource Groups", "48", "📁", "+2 this month")
        
        with col3:
            AzureTheme.azure_metric_card("Resource Types", "67", "🔧")
        
        with col4:
            AzureTheme.azure_metric_card("Untagged", "234", "⚠️", "-45 this week")
        
        st.markdown("---")
        
        # Resource distribution charts
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 📊 Resources by Type")
            
            resource_types = {
                'Virtual Machines': 234,
                'Storage Accounts': 156,
                'SQL Databases': 89,
                'App Services': 67,
                'Virtual Networks': 45,
                'Load Balancers': 34,
                'Azure Functions': 28,
                'Key Vaults': 23,
                'Cosmos DB': 12,
                'AKS Clusters': 8
            }
            
            fig = px.bar(
                x=list(resource_types.values()),
                y=list(resource_types.keys()),
                orientation='h',
                title="",
                color=list(resource_types.values()),
                color_continuous_scale=['#0078D4', '#50E6FF']
            )
            
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family='Segoe UI', color='#004E8C'),
                showlegend=False
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("#### 🌍 Resources by Location")
            
            locations = {
                'East US': 3456,
                'West US': 2890,
                'East US 2': 2345,
                'Central US': 1890,
                'West Europe': 1456,
                'North Europe': 890
            }
            
            fig = go.Figure(data=[go.Pie(
                labels=list(locations.keys()),
                values=list(locations.values()),
                hole=0.4,
                marker=dict(colors=['#0078D4', '#50E6FF', '#004E8C', '#00BCF2', '#0063B1', '#008272'])
            )])
            
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family='Segoe UI', color='#004E8C')
            )
            
            st.plotly_chart(fig, use_container_width=True)
    
    @staticmethod
    def _render_resource_explorer(subscriptions: List):
        """Render resource explorer"""
        
        st.markdown("### 🔍 Resource Explorer")
        
        # Filters
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            selected_subscription = st.selectbox(
                "Subscription",
                ["All"] + [s.subscription_name for s in subscriptions]
            )
        
        with col2:
            resource_type = st.selectbox(
                "Resource Type",
                ["All", "Virtual Machines", "Storage Accounts", "SQL Databases", "App Services", "Virtual Networks"]
            )
        
        with col3:
            location = st.selectbox(
                "Location",
                ["All", "East US", "West US", "Central US", "West Europe"]
            )
        
        with col4:
            status = st.selectbox(
                "Status",
                ["All", "Running", "Stopped", "Deallocated"]
            )
        
        # Search
        search_term = st.text_input("🔍 Search resources", placeholder="Search by name, tag, or resource ID...")
        
        st.markdown("---")
        
        # Resource table
        st.markdown("#### 📋 Resources")
        
        resources_data = [
            {
                "Name": "prod-web-vm-01",
                "Type": "Virtual Machine",
                "Resource Group": "Production-RG",
                "Location": "East US",
                "Status": "✅ Running",
                "Tags": "Environment:Prod, App:Web",
                "Cost/Mo": "$145.80"
            },
            {
                "Name": "prodstorageacct001",
                "Type": "Storage Account",
                "Resource Group": "Production-RG",
                "Location": "East US",
                "Status": "✅ Active",
                "Tags": "Environment:Prod",
                "Cost/Mo": "$67.40"
            },
            {
                "Name": "prod-sqldb-main",
                "Type": "SQL Database",
                "Resource Group": "Database-RG",
                "Location": "East US 2",
                "Status": "✅ Online",
                "Tags": "Environment:Prod, Tier:Critical",
                "Cost/Mo": "$890.50"
            },
            {
                "Name": "prod-app-service-01",
                "Type": "App Service",
                "Resource Group": "Production-RG",
                "Location": "West US",
                "Status": "✅ Running",
                "Tags": "Environment:Prod, App:API",
                "Cost/Mo": "$234.20"
            },
            {
                "Name": "dev-test-vm-02",
                "Type": "Virtual Machine",
                "Resource Group": "Development-RG",
                "Location": "West US",
                "Status": "⏸️ Stopped",
                "Tags": "Environment:Dev",
                "Cost/Mo": "$0.00"
            }
        ]
        
        df_resources = pd.DataFrame(resources_data)
        
        # Apply filters
        if search_term:
            df_resources = df_resources[df_resources.apply(lambda row: search_term.lower() in row.astype(str).str.lower().values.any(), axis=1)]
        
        st.dataframe(df_resources, use_container_width=True, hide_index=True)
        
        # Resource actions
        st.markdown("---")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            if st.button("🔄 Refresh Inventory", use_container_width=True):
                st.info("Refreshing resource inventory...")
        
        with col2:
            if st.button("🏷️ Bulk Tag", use_container_width=True):
                st.info("Opening bulk tag editor...")
        
        with col3:
            if st.button("💰 Cost Analysis", use_container_width=True):
                st.info("Opening cost analysis...")
        
        with col4:
            if st.button("📊 Generate Report", use_container_width=True):
                st.info("Generating inventory report...")
    
    @staticmethod
    def _render_tag_explorer():
        """Render tag explorer"""
        
        st.markdown("### 🏷️ Tag Explorer")
        
        AzureTheme.azure_info_box(
            "Tag Compliance",
            "Track tag coverage and enforce tagging policies across your Azure resources.",
            "🏷️"
        )
        
        # Tag coverage metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Tag Coverage", "94.2%", "+2.3%")
        with col2:
            st.metric("Tagged Resources", "12,113", "+500")
        with col3:
            st.metric("Untagged Resources", "734", "-45")
        with col4:
            st.metric("Tag Keys in Use", "23")
        
        st.markdown("---")
        
        # Most common tags
        st.markdown("#### 📊 Most Common Tags")
        
        tag_usage = {
            'Environment': 11234,
            'CostCenter': 10890,
            'Owner': 9456,
            'Project': 8234,
            'Application': 7890,
            'Department': 6543
        }
        
        fig = px.bar(
            x=list(tag_usage.keys()),
            y=list(tag_usage.values()),
            title="",
            color=list(tag_usage.values()),
            color_continuous_scale=['#0078D4', '#50E6FF']
        )
        
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(family='Segoe UI', color='#004E8C'),
            showlegend=False
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Untagged resources
        st.markdown("#### ⚠️ Untagged Resources")
        
        untagged_data = [
            {"Resource": "temp-storage-001", "Type": "Storage Account", "Resource Group": "Temp-RG", "Location": "East US"},
            {"Resource": "test-vm-orphan", "Type": "Virtual Machine", "Resource Group": "Test-RG", "Location": "West US"},
            {"Resource": "legacy-db-01", "Type": "SQL Database", "Resource Group": "Legacy-RG", "Location": "Central US"}
        ]
        
        df_untagged = pd.DataFrame(untagged_data)
        st.dataframe(df_untagged, use_container_width=True, hide_index=True)
    
    @staticmethod
    def _render_analytics():
        """Render analytics"""
        
        st.markdown("### 📈 Resource Analytics")
        
        # Growth trend
        st.markdown("#### 📊 Resource Growth Trend")
        
        dates = pd.date_range(start='2024-01-01', end='2024-12-01', freq='M')
        resources = [8000, 8500, 9200, 9800, 10500, 11200, 11800, 12100, 12400, 12650, 12800, 12847]
        
        fig = px.line(
            x=dates,
            y=resources,
            title="",
            markers=True
        )
        
        fig.update_traces(line_color='#0078D4', marker=dict(size=8, color='#50E6FF'))
        
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(family='Segoe UI', color='#004E8C'),
            xaxis_title="Month",
            yaxis_title="Total Resources"
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Resource lifecycle
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### ➕ Recently Created (Last 7 Days)")
            recent = pd.DataFrame({
                'Resource': ['prod-vm-new-01', 'staging-app-02', 'dev-storage-03'],
                'Type': ['VM', 'App Service', 'Storage'],
                'Created': ['2 days ago', '3 days ago', '5 days ago']
            })
            st.dataframe(recent, use_container_width=True, hide_index=True)
        
        with col2:
            st.markdown("#### 🗑️ Recently Deleted (Last 7 Days)")
            deleted = pd.DataFrame({
                'Resource': ['old-test-vm', 'temp-db-001', 'legacy-storage'],
                'Type': ['VM', 'SQL DB', 'Storage'],
                'Deleted': ['1 day ago', '4 days ago', '6 days ago']
            })
            st.dataframe(deleted, use_container_width=True, hide_index=True)
    
    @staticmethod
    def _render_change_tracking():
        """Render change tracking"""
        
        st.markdown("### 🔄 Change Tracking")
        
        # Recent changes
        changes_data = [
            {"Timestamp": "2024-12-06 14:30", "Resource": "prod-web-vm-01", "Action": "Modified", "User": "john.doe@company.com", "Change": "VM size updated to Standard_D4s_v3"},
            {"Timestamp": "2024-12-06 13:15", "Resource": "prod-app-service-01", "Action": "Scaled", "User": "DevOps Pipeline", "Change": "Scaled up to P2v2"},
            {"Timestamp": "2024-12-06 12:00", "Resource": "dev-test-rg", "Action": "Created", "User": "jane.smith@company.com", "Change": "New resource group created"},
            {"Timestamp": "2024-12-06 10:45", "Resource": "temp-storage-old", "Action": "Deleted", "User": "cleanup-automation", "Change": "Resource deleted"},
            {"Timestamp": "2024-12-06 09:30", "Resource": "prod-sqldb-main", "Action": "Modified", "User": "admin@company.com", "Change": "Firewall rules updated"}
        ]
        
        df_changes = pd.DataFrame(changes_data)
        st.dataframe(df_changes, use_container_width=True, hide_index=True)
        
        # Change statistics
        st.markdown("---")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Changes Today", "47")
        with col2:
            st.metric("Changes This Week", "312")
        with col3:
            st.metric("Most Active User", "DevOps Pipeline")
        with col4:
            st.metric("Most Changed Resource", "prod-app-service-01")
    
    @staticmethod
    def _render_export():
        """Render export options"""
        
        st.markdown("### 📤 Export Resource Inventory")
        
        AzureTheme.azure_info_box(
            "Export Options",
            "Export your resource inventory in various formats for reporting and analysis.",
            "📤"
        )
        
        export_format = st.selectbox(
            "Export Format",
            ["CSV", "Excel", "JSON", "PDF Report"]
        )
        
        include_options = st.multiselect(
            "Include",
            ["Resource Details", "Tags", "Cost Information", "Compliance Status", "Change History"],
            default=["Resource Details", "Tags"]
        )
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("📥 Download Export", type="primary", use_container_width=True):
                st.success(f"✅ Inventory exported as {export_format}")
        
        with col2:
            if st.button("📧 Email Report", use_container_width=True):
                st.info("📧 Report will be emailed to your address")
