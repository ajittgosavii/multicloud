"""
Azure Module: Management Groups
Hierarchical organization and governance structure management
"""

import streamlit as st
import pandas as pd
from azure_theme import AzureTheme

class AzureManagementGroupsUI:
    """Azure Management Groups module"""
    
    @staticmethod
    def render():
        st.markdown("## 🏢 Azure Management Groups")
        st.caption("Organize subscriptions in a hierarchy for unified policy and access management")
        
        tabs = st.tabs([
            "🌳 Hierarchy",
            "📋 Policies",
            "🔐 Access Control",
            "📊 Analytics"
        ])
        
        with tabs[0]:
            AzureManagementGroupsUI._render_hierarchy()
        
        with tabs[1]:
            AzureManagementGroupsUI._render_policies()
        
        with tabs[2]:
            AzureManagementGroupsUI._render_access_control()
        
        with tabs[3]:
            AzureManagementGroupsUI._render_analytics()
    
    @staticmethod
    def _render_hierarchy():
        st.markdown("### 🌳 Management Group Hierarchy")
        
        AzureTheme.azure_info_box(
            "Management Groups",
            "Organize Azure subscriptions into containers for applying policies and access controls at scale.",
            "🏢"
        )
        
        st.markdown("""
        ```
        Tenant Root Group
        ├── Production
        │   ├── Prod-Apps
        │   └── Prod-Data
        ├── Development
        │   ├── Dev-Team-A
        │   └── Dev-Team-B
        └── Shared-Services
            ├── Networking
            └── Security
        ```
        """)
        
        groups_data = [
            {"Name": "Production", "Subscriptions": 5, "Child Groups": 2, "Policies": 12},
            {"Name": "Development", "Subscriptions": 8, "Child Groups": 2, "Policies": 8},
            {"Name": "Shared-Services", "Subscriptions": 3, "Child Groups": 2, "Policies": 15}
        ]
        
        df = pd.DataFrame(groups_data)
        st.dataframe(df, use_container_width=True, hide_index=True)
    
    @staticmethod
    def _render_policies():
        st.markdown("### 📋 Azure Policies")
        
        policies_data = [
            {"Policy": "Allowed Locations", "Effect": "Deny", "Scope": "Production", "Compliance": "100%"},
            {"Policy": "Required Tags", "Effect": "Audit", "Scope": "All", "Compliance": "94%"},
            {"Policy": "Allowed VM SKUs", "Effect": "Deny", "Scope": "Development", "Compliance": "100%"}
        ]
        
        df = pd.DataFrame(policies_data)
        st.dataframe(df, use_container_width=True, hide_index=True)
    
    @staticmethod
    def _render_access_control():
        st.markdown("### 🔐 Access Control")
        
        st.info("Manage role assignments at management group level for inheritance across subscriptions.")
        
        role_data = [
            {"Principal": "IT-Admins", "Role": "Owner", "Scope": "Production", "Type": "Group"},
            {"Principal": "Developers", "Role": "Contributor", "Scope": "Development", "Type": "Group"}
        ]
        
        df = pd.DataFrame(role_data)
        st.dataframe(df, use_container_width=True, hide_index=True)
    
    @staticmethod
    def _render_analytics():
        st.markdown("### 📊 Management Group Analytics")
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Groups", "12")
        with col2:
            st.metric("Total Subscriptions", "28")
        with col3:
            st.metric("Policy Compliance", "96.5%")
        with col4:
            st.metric("Role Assignments", "145")
