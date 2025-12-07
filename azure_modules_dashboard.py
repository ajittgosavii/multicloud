"""
Azure Module: Main Dashboard
Enterprise multi-subscription Azure cloud management dashboard
"""

import streamlit as st
import pandas as pd
from typing import Dict, List
from datetime import datetime, timedelta
from config_settings import AppConfig
from core_session_manager import SessionManager
from azure_theme import AzureTheme

class AzureDashboardModule:
    """Azure main dashboard with enterprise overview"""
    
    @staticmethod
    def render():
        """Render Azure dashboard"""
        
        st.markdown("## 🏠 Enterprise Azure Cloud Dashboard")
        st.caption("Multi-subscription Azure environment overview with real-time metrics")
        
        # Load subscriptions
        subscriptions = AppConfig.load_azure_subscriptions()
        active_subscriptions = [sub for sub in subscriptions if sub.status == 'active']
        
        if not active_subscriptions:
            st.warning("⚠️ No active Azure subscriptions configured.")
            st.info("Go to **Subscription Lifecycle** → **Onboard Subscription** to add your first subscription.")
            return
        
        # Top metrics - Azure style
        AzureDashboardModule._render_top_metrics(active_subscriptions)
        
        st.markdown("---")
        
        # Charts row
        col1, col2 = st.columns(2)
        
        with col1:
            AzureDashboardModule._render_cost_by_subscription(active_subscriptions)
        
        with col2:
            AzureDashboardModule._render_resource_distribution(active_subscriptions)
        
        st.markdown("---")
        
        # Subscription status table
        AzureDashboardModule._render_subscription_status_table(active_subscriptions)
        
        st.markdown("---")
        
        # Recent activity
        AzureDashboardModule._render_recent_activity()
    
    @staticmethod
    def _render_top_metrics(subscriptions: List):
        """Render top-level metrics"""
        
        st.markdown("### 📊 Key Metrics")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            AzureTheme.azure_metric_card(
                "Total Subscriptions",
                str(len(subscriptions)),
                "🔷",
                "+2 this month"
            )
        
        with col2:
            AzureTheme.azure_metric_card(
                "Total Resources",
                "12,847",
                "📦",
                "+458 this week"
            )
        
        with col3:
            AzureTheme.azure_metric_card(
                "Monthly Cost",
                "$142,890",
                "💰",
                "-8.3% vs last month"
            )
        
        with col4:
            AzureTheme.azure_metric_card(
                "Compliance Score",
                "94.2%",
                "✅",
                "+2.1% improvement"
            )
    
    @staticmethod
    def _render_cost_by_subscription(subscriptions: List):
        """Render cost breakdown by subscription"""
        
        st.markdown("### 💰 Cost by Subscription (Last 30 Days)")
        
        # Sample data
        cost_data = []
        for sub in subscriptions[:8]:
            cost_data.append({
                'Subscription': sub.subscription_name,
                'Cost': pd.np.random.uniform(5000, 25000)
            })
        
        df = pd.DataFrame(cost_data)
        
        import plotly.express as px
        fig = px.bar(
            df,
            x='Subscription',
            y='Cost',
            title="",
            color='Cost',
            color_continuous_scale=['#0078D4', '#50E6FF']
        )
        
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(family='Segoe UI', color='#004E8C'),
            showlegend=False,
            xaxis_title="",
            yaxis_title="Cost (USD)"
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    @staticmethod
    def _render_resource_distribution(subscriptions: List):
        """Render resource distribution chart"""
        
        st.markdown("### 📊 Resource Distribution")
        
        # Sample data
        resource_types = {
            'Virtual Machines': 234,
            'Storage Accounts': 156,
            'SQL Databases': 89,
            'App Services': 67,
            'Virtual Networks': 45,
            'Load Balancers': 34,
            'Azure Functions': 28,
            'Cosmos DB': 12
        }
        
        import plotly.graph_objects as go
        
        fig = go.Figure(data=[go.Pie(
            labels=list(resource_types.keys()),
            values=list(resource_types.values()),
            hole=0.4,
            marker=dict(colors=['#0078D4', '#50E6FF', '#004E8C', '#00BCF2', '#0063B1', '#008272', '#68217A', '#5E5E5E'])
        )])
        
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(family='Segoe UI', color='#004E8C'),
            showlegend=True,
            legend=dict(orientation="v", yanchor="top", y=1, xanchor="left", x=1.02)
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    @staticmethod
    def _render_subscription_status_table(subscriptions: List):
        """Render subscription status table"""
        
        st.markdown("### 🔷 Subscription Status")
        
        # Prepare data
        table_data = []
        for sub in subscriptions:
            table_data.append({
                'Subscription Name': sub.subscription_name,
                'Subscription ID': sub.subscription_id[:8] + '...',
                'Status': '✅ Active' if sub.status == 'active' else '❌ Inactive',
                'Environment': sub.environment.capitalize(),
                'Resources': pd.np.random.randint(50, 500),
                'Monthly Cost': f"${pd.np.random.uniform(5000, 25000):,.2f}",
                'Compliance': f"{pd.np.random.uniform(85, 99):.1f}%"
            })
        
        df = pd.DataFrame(table_data)
        
        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )
    
    @staticmethod
    def _render_recent_activity():
        """Render recent activity feed"""
        
        st.markdown("### 📋 Recent Activity")
        
        activities = [
            {"time": "2 mins ago", "action": "VM created", "resource": "prod-vm-webserver-01", "user": "john.doe@company.com"},
            {"time": "15 mins ago", "action": "Storage account updated", "resource": "prodstorageacct001", "user": "jane.smith@company.com"},
            {"time": "1 hour ago", "action": "SQL Database scaled", "resource": "prod-sqldb-main", "user": "admin@company.com"},
            {"time": "2 hours ago", "action": "Function App deployed", "resource": "prod-func-api", "user": "dev-team@company.com"},
            {"time": "3 hours ago", "action": "Virtual Network created", "resource": "prod-vnet-east-01", "user": "network-admin@company.com"}
        ]
        
        for activity in activities:
            col1, col2, col3, col4 = st.columns([1, 2, 3, 2])
            with col1:
                st.caption(activity['time'])
            with col2:
                st.caption(f"🔵 {activity['action']}")
            with col3:
                st.caption(activity['resource'])
            with col4:
                st.caption(activity['user'])
        
        st.markdown("---")
        
        if st.button("View All Activity →", use_container_width=True):
            st.info("Full activity log coming soon...")
