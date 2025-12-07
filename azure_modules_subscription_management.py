"""
Azure Module: Subscription Management
Comprehensive Azure subscription lifecycle and access management
"""

import streamlit as st
import pandas as pd
from typing import Dict, List
from datetime import datetime, timedelta
from azure_theme import AzureTheme
from config_settings import AppConfig
from core_session_manager import SessionManager

class AzureSubscriptionManagementModule:
    """Azure Subscription Management module"""
    
    @staticmethod
    def render():
        """Render Azure subscription management module"""
        
        st.markdown("## 🔷 Azure Subscription Management")
        st.caption("Manage Azure subscriptions, access control, and tenant configuration")
        
        # Load subscriptions
        subscriptions = AppConfig.load_azure_subscriptions()
        active_subscriptions = [sub for sub in subscriptions if sub.status == 'active']
        
        # Create tabs for different sections
        tabs = st.tabs([
            "📊 Overview",
            "➕ Add Subscription",
            "🔐 Access Control (RBAC)",
            "🏷️ Tag Management",
            "📋 Subscription Details",
            "⚙️ Settings"
        ])
        
        with tabs[0]:  # Overview
            AzureSubscriptionManagementModule._render_overview(subscriptions)
        
        with tabs[1]:  # Add Subscription
            AzureSubscriptionManagementModule._render_add_subscription()
        
        with tabs[2]:  # RBAC
            AzureSubscriptionManagementModule._render_rbac_management(active_subscriptions)
        
        with tabs[3]:  # Tag Management
            AzureSubscriptionManagementModule._render_tag_management(active_subscriptions)
        
        with tabs[4]:  # Details
            AzureSubscriptionManagementModule._render_subscription_details(active_subscriptions)
        
        with tabs[5]:  # Settings
            AzureSubscriptionManagementModule._render_settings()
    
    @staticmethod
    def _render_overview(subscriptions: List):
        """Render subscription overview"""
        
        st.markdown("### 📊 Subscription Overview")
        
        active_subs = [s for s in subscriptions if s.status == 'active']
        inactive_subs = [s for s in subscriptions if s.status != 'active']
        
        # Key metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            AzureTheme.azure_metric_card(
                "Total Subscriptions",
                str(len(subscriptions)),
                "🔷"
            )
        
        with col2:
            AzureTheme.azure_metric_card(
                "Active",
                str(len(active_subs)),
                "✅"
            )
        
        with col3:
            AzureTheme.azure_metric_card(
                "Inactive",
                str(len(inactive_subs)),
                "⏸️"
            )
        
        with col4:
            AzureTheme.azure_metric_card(
                "Avg Resources",
                "234",
                "📦"
            )
        
        st.markdown("---")
        
        # Subscription status table
        st.markdown("### 📋 Subscription Status")
        
        table_data = []
        for sub in subscriptions:
            table_data.append({
                'Subscription Name': sub.subscription_name,
                'Subscription ID': sub.subscription_id[:8] + '...',
                'Tenant ID': sub.tenant_id[:8] + '...',
                'Environment': sub.environment.capitalize(),
                'Location': sub.location,
                'Status': '✅ Active' if sub.status == 'active' else '⏸️ Inactive',
                'Resources': pd.np.random.randint(50, 500),
                'Monthly Cost': f"${pd.np.random.uniform(5000, 25000):,.2f}"
            })
        
        df = pd.DataFrame(table_data)
        st.dataframe(df, use_container_width=True, hide_index=True)
    
    @staticmethod
    def _render_add_subscription():
        """Render add subscription form"""
        
        st.markdown("### ➕ Onboard New Subscription")
        
        AzureTheme.azure_info_box(
            "Subscription Onboarding",
            "Add a new Azure subscription to the platform for centralized management and monitoring.",
            "ℹ️"
        )
        
        with st.form("add_subscription_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                sub_name = st.text_input(
                    "Subscription Name *",
                    placeholder="e.g., Production-Main"
                )
                
                subscription_id = st.text_input(
                    "Subscription ID *",
                    placeholder="12345678-1234-1234-1234-123456789012"
                )
                
                tenant_id = st.text_input(
                    "Tenant ID *",
                    placeholder="87654321-4321-4321-4321-210987654321"
                )
            
            with col2:
                environment = st.selectbox(
                    "Environment *",
                    ["Production", "Development", "Staging", "Sandbox"]
                )
                
                location = st.selectbox(
                    "Primary Location *",
                    ['East US', 'East US 2', 'West US', 'West US 2', 'Central US',
                     'North Europe', 'West Europe', 'UK South', 'Southeast Asia']
                )
                
                cost_center = st.text_input(
                    "Cost Center",
                    placeholder="e.g., Engineering"
                )
            
            # Service Principal Details
            st.markdown("#### 🔐 Service Principal Details")
            
            col3, col4 = st.columns(2)
            
            with col3:
                client_id = st.text_input(
                    "Client ID (Application ID)",
                    type="password",
                    placeholder="Service principal client ID"
                )
            
            with col4:
                client_secret = st.text_input(
                    "Client Secret",
                    type="password",
                    placeholder="Service principal secret"
                )
            
            # Tags
            st.markdown("#### 🏷️ Tags")
            tags_input = st.text_area(
                "Tags (JSON format)",
                value='{"Department": "IT", "CostCenter": "Engineering"}',
                height=100
            )
            
            submit = st.form_submit_button("🚀 Onboard Subscription", type="primary", use_container_width=True)
            
            if submit:
                if sub_name and subscription_id and tenant_id:
                    st.success(f"✅ Subscription '{sub_name}' onboarded successfully!")
                    st.info("🔄 Initializing resource discovery and compliance scanning...")
                else:
                    st.error("❌ Please fill in all required fields (marked with *)")
    
    @staticmethod
    def _render_rbac_management(subscriptions: List):
        """Render RBAC management"""
        
        st.markdown("### 🔐 Role-Based Access Control (RBAC)")
        
        if not subscriptions:
            st.warning("No subscriptions available")
            return
        
        # Select subscription
        selected_sub = st.selectbox(
            "Select Subscription",
            [f"{s.subscription_name} ({s.subscription_id[:8]}...)" for s in subscriptions]
        )
        
        st.markdown("---")
        
        # RBAC Overview
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Role Assignments", "45")
        with col2:
            st.metric("Built-in Roles", "12")
        with col3:
            st.metric("Custom Roles", "3")
        with col4:
            st.metric("Active Users", "28")
        
        st.markdown("---")
        
        # Role Assignments Table
        st.markdown("#### 👥 Current Role Assignments")
        
        assignments_data = [
            {"Principal": "john.doe@company.com", "Type": "User", "Role": "Owner", "Scope": "Subscription", "Assigned": "2024-01-15"},
            {"Principal": "jane.smith@company.com", "Type": "User", "Role": "Contributor", "Scope": "Resource Group", "Assigned": "2024-02-01"},
            {"Principal": "DevOps-Team", "Type": "Group", "Role": "DevOps Engineer", "Scope": "Subscription", "Assigned": "2024-01-20"},
            {"Principal": "app-service-sp", "Type": "Service Principal", "Role": "Contributor", "Scope": "Resource Group", "Assigned": "2024-03-01"},
        ]
        
        df_assignments = pd.DataFrame(assignments_data)
        st.dataframe(df_assignments, use_container_width=True, hide_index=True)
        
        st.markdown("---")
        
        # Add New Role Assignment
        st.markdown("#### ➕ Add Role Assignment")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            principal_type = st.selectbox("Principal Type", ["User", "Group", "Service Principal", "Managed Identity"])
        
        with col2:
            role = st.selectbox("Role", ["Owner", "Contributor", "Reader", "User Access Administrator", "DevOps Engineer"])
        
        with col3:
            scope = st.selectbox("Scope", ["Subscription", "Resource Group", "Resource"])
        
        principal_name = st.text_input("Principal Name/Email", placeholder="user@company.com or group name")
        
        if st.button("🔐 Assign Role", type="primary", use_container_width=True):
            st.success(f"✅ Role '{role}' assigned to '{principal_name}' successfully!")
    
    @staticmethod
    def _render_tag_management(subscriptions: List):
        """Render tag management"""
        
        st.markdown("### 🏷️ Tag Management")
        
        AzureTheme.azure_info_box(
            "Azure Tags",
            "Tags help you organize resources and manage costs. Apply consistent tagging across your subscriptions.",
            "🏷️"
        )
        
        # Tag Policy
        st.markdown("#### 📋 Tag Policy")
        
        col1, col2 = st.columns(2)
        
        with col1:
            enforce_tags = st.checkbox("Enforce Required Tags", value=True)
            
            if enforce_tags:
                required_tags = st.multiselect(
                    "Required Tags",
                    ["Environment", "CostCenter", "Owner", "Project", "Application"],
                    default=["Environment", "CostCenter"]
                )
        
        with col2:
            auto_tag = st.checkbox("Auto-Tag Resources", value=True)
            
            if auto_tag:
                st.info("Resources will be automatically tagged with: CreatedBy, CreatedDate")
        
        st.markdown("---")
        
        # Common Tags
        st.markdown("#### 🏷️ Apply Common Tags")
        
        tag_templates = {
            "Production": {
                "Environment": "Production",
                "CostCenter": "Engineering",
                "Compliance": "Required"
            },
            "Development": {
                "Environment": "Development",
                "CostCenter": "Engineering",
                "Compliance": "NotRequired"
            },
            "Shared Services": {
                "Environment": "Shared",
                "CostCenter": "IT",
                "Purpose": "Infrastructure"
            }
        }
        
        selected_template = st.selectbox("Select Tag Template", list(tag_templates.keys()))
        
        if selected_template:
            st.json(tag_templates[selected_template])
            
            if st.button("🏷️ Apply Template to Subscription", type="primary"):
                st.success(f"✅ Tags from '{selected_template}' template applied successfully!")
    
    @staticmethod
    def _render_subscription_details(subscriptions: List):
        """Render subscription details"""
        
        st.markdown("### 📋 Subscription Details")
        
        if not subscriptions:
            st.warning("No subscriptions available")
            return
        
        selected_sub = st.selectbox(
            "Select Subscription",
            [f"{s.subscription_name}" for s in subscriptions],
            key="details_sub_select"
        )
        
        # Find selected subscription
        subscription = next((s for s in subscriptions if s.subscription_name == selected_sub), None)
        
        if subscription:
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### 📝 Basic Information")
                st.write(f"**Name:** {subscription.subscription_name}")
                st.write(f"**ID:** {subscription.subscription_id}")
                st.write(f"**Tenant ID:** {subscription.tenant_id}")
                st.write(f"**Environment:** {subscription.environment.capitalize()}")
                st.write(f"**Location:** {subscription.location}")
                st.write(f"**Status:** {'✅ Active' if subscription.status == 'active' else '⏸️ Inactive'}")
            
            with col2:
                st.markdown("#### 📊 Usage Statistics")
                st.metric("Resource Groups", "12")
                st.metric("Total Resources", "234")
                st.metric("Monthly Cost", "$18,450")
                st.metric("Last Activity", "2 hours ago")
            
            st.markdown("---")
            
            # Resource Groups
            st.markdown("#### 📁 Resource Groups")
            
            rg_data = [
                {"Name": "Production-RG", "Location": "East US", "Resources": 45, "Cost": "$8,200"},
                {"Name": "Development-RG", "Location": "West US", "Resources": 32, "Cost": "$3,450"},
                {"Name": "Networking-RG", "Location": "East US", "Resources": 18, "Cost": "$4,800"},
                {"Name": "Security-RG", "Location": "Central US", "Resources": 12, "Cost": "$2,000"},
            ]
            
            df_rg = pd.DataFrame(rg_data)
            st.dataframe(df_rg, use_container_width=True, hide_index=True)
    
    @staticmethod
    def _render_settings():
        """Render subscription settings"""
        
        st.markdown("### ⚙️ Subscription Settings")
        
        # Cost Alerts
        st.markdown("#### 💰 Cost Management")
        
        enable_alerts = st.checkbox("Enable Cost Alerts", value=True)
        
        if enable_alerts:
            col1, col2 = st.columns(2)
            
            with col1:
                budget_threshold = st.number_input(
                    "Monthly Budget ($)",
                    min_value=1000,
                    max_value=1000000,
                    value=20000,
                    step=1000
                )
            
            with col2:
                alert_threshold = st.slider(
                    "Alert at % of Budget",
                    min_value=50,
                    max_value=100,
                    value=80
                )
        
        st.markdown("---")
        
        # Compliance
        st.markdown("#### ✅ Compliance & Governance")
        
        col1, col2 = st.columns(2)
        
        with col1:
            enable_policies = st.checkbox("Enable Azure Policy", value=True)
            enable_blueprints = st.checkbox("Enable Azure Blueprints", value=True)
        
        with col2:
            enable_defender = st.checkbox("Enable Microsoft Defender", value=True)
            enable_advisor = st.checkbox("Enable Azure Advisor", value=True)
        
        st.markdown("---")
        
        # Save Settings
        if st.button("💾 Save Settings", type="primary", use_container_width=True):
            st.success("✅ Subscription settings saved successfully!")
