"""
Multi-Cloud Navigation Component
Supports AWS and Azure with provider-specific module routing
"""

import streamlit as st
from core_session_manager import SessionManager

class Navigation:
    """Main application navigation with multi-cloud support"""
    
    @staticmethod
    def render():
        """Render main navigation with cloud provider awareness"""
        
        # Get cloud provider from session state
        cloud_provider = st.session_state.get('cloud_provider', 'AWS')
        
        # Initialize active module in session state
        if 'active_module' not in st.session_state:
            st.session_state.active_module = 'Dashboard'
        
        # Define all navigation items (16 modules - same for both AWS and Azure)
        nav_items = [
            {"key": "Dashboard", "icon": "🏠", "label": "Dashboard"},
            {"key": "Account Management", "icon": "👥", "label": "Account Mgmt" if cloud_provider == "AWS" else "Subscription Mgmt"},
            {"key": "Resource Inventory", "icon": "📦", "label": "Resources"},
            {"key": "Network", "icon": "🌐", "label": "Network"},
            {"key": "Organizations", "icon": "🏢", "label": "Organizations" if cloud_provider == "AWS" else "Management Groups"},
            {"key": "Design & Planning", "icon": "📐", "label": "Design"},
            {"key": "Provisioning", "icon": "🚀", "label": "Provisioning"},
            {"key": "CI/CD", "icon": "📄", "label": "CI/CD"},
            {"key": "Operations", "icon": "⚙️", "label": "Operations"},
            {"key": "Advanced Operations", "icon": "⚡", "label": "Advanced Ops"},
            {"key": "Security", "icon": "🔒", "label": "Security & AI"},
            {"key": "Container Management", "icon": "📦", "label": "EKS/AKS"},
            {"key": "FinOps & Cost", "icon": "💰", "label": "FinOps"},
            {"key": "Lifecycle", "icon": "♻️", "label": "Lifecycle"},
            {"key": "Developer Experience", "icon": "👨‍💻", "label": "DevEx"},
            {"key": "AI Assistant", "icon": "🤖", "label": "AI Assistant"}
        ]
        
        # Display current cloud provider mode
        st.markdown(f"### 🧭 Navigation - {cloud_provider} Mode")
        
        # Row 1: First 8 modules
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        cols_row1 = [col1, col2, col3, col4, col5, col6, col7, col8]
        
        for idx, item in enumerate(nav_items[:8]):
            with cols_row1[idx]:
                button_type = "primary" if st.session_state.active_module == item['key'] else "secondary"
                if st.button(
                    f"{item['icon']} {item['label']}",
                    key=f"nav_{item['key']}",
                    use_container_width=True,
                    type=button_type
                ):
                    st.session_state.active_module = item['key']
                    st.rerun()
        
        # Row 2: Next 8 modules
        col9, col10, col11, col12, col13, col14, col15, col16 = st.columns(8)
        cols_row2 = [col9, col10, col11, col12, col13, col14, col15, col16]
        
        for idx, item in enumerate(nav_items[8:]):
            with cols_row2[idx]:
                button_type = "primary" if st.session_state.active_module == item['key'] else "secondary"
                if st.button(
                    f"{item['icon']} {item['label']}",
                    key=f"nav_{item['key']}",
                    use_container_width=True,
                    type=button_type
                ):
                    st.session_state.active_module = item['key']
                    st.rerun()
        
        st.markdown("---")
        
        # Render the active module based on cloud provider
        Navigation._render_module(st.session_state.active_module, cloud_provider)
    
    @staticmethod
    def _render_module(module_name: str, cloud_provider: str):
        """Render module based on cloud provider"""
        
        try:
            # Module 0: Dashboard
            if module_name == "Dashboard":
                if cloud_provider == "AWS":
                    from modules_dashboard import DashboardModule
                    DashboardModule.render()
                elif cloud_provider == "Azure":
                    from azure_modules_dashboard import AzureDashboardModule
                    AzureDashboardModule.render()
            
            # Module 1: Account/Subscription Management
            elif module_name == "Account Management":
                if cloud_provider == "AWS":
                    from modules_account_management import AccountManagementModule
                    AccountManagementModule.render()
                elif cloud_provider == "Azure":
                    from azure_modules_subscription_management import AzureSubscriptionManagementModule
                    AzureSubscriptionManagementModule.render()
            
            # Module 2: Resource Inventory
            elif module_name == "Resource Inventory":
                if cloud_provider == "AWS":
                    from modules_resource_inventory import ResourceInventoryModule
                    ResourceInventoryModule.render()
                elif cloud_provider == "Azure":
                    from azure_modules_resource_inventory import AzureResourceInventoryModule
                    AzureResourceInventoryModule.render()
            
            # Module 3: Network Management
            elif module_name == "Network":
                if cloud_provider == "AWS":
                    from modules_network_management import NetworkManagementUI
                    NetworkManagementUI.render()
                elif cloud_provider == "Azure":
                    from azure_modules_network_management import AzureNetworkManagementUI
                    AzureNetworkManagementUI.render()
            
            # Module 4: Organizations/Management Groups
            elif module_name == "Organizations":
                if cloud_provider == "AWS":
                    from modules_organizations import OrganizationsManagementUI
                    OrganizationsManagementUI.render()
                elif cloud_provider == "Azure":
                    from azure_modules_management_groups import AzureManagementGroupsUI
                    AzureManagementGroupsUI.render()
            
            # Module 5: Design & Planning
            elif module_name == "Design & Planning":
                if cloud_provider == "AWS":
                    from modules_design_planning import DesignPlanningModule
                    DesignPlanningModule.render()
                elif cloud_provider == "Azure":
                    from azure_modules_design_planning import AzureDesignPlanningModule
                    AzureDesignPlanningModule.render()
            
            # Module 6: Provisioning & Deployment
            elif module_name == "Provisioning":
                if cloud_provider == "AWS":
                    from modules_provisioning import ProvisioningModule
                    ProvisioningModule.render()
                elif cloud_provider == "Azure":
                    from azure_modules_provisioning import AzureProvisioningModule
                    AzureProvisioningModule.render()
            
            # Module 7: CI/CD
            elif module_name == "CI/CD":
                if cloud_provider == "AWS":
                    from modules_cicd_unified import UnifiedCICDModule
                    UnifiedCICDModule.render()
                elif cloud_provider == "Azure":
                    from azure_modules_cicd_unified import AzureUnifiedCICDModule
                    AzureUnifiedCICDModule.render()
            
            # Module 8: Operations
            elif module_name == "Operations":
                if cloud_provider == "AWS":
                    from modules_operations import OperationsModule
                    OperationsModule.render()
                elif cloud_provider == "Azure":
                    from azure_modules_operations import AzureOperationsModule
                    AzureOperationsModule.render()
            
            # Module 9: Advanced Operations
            elif module_name == "Advanced Operations":
                if cloud_provider == "AWS":
                    from modules_advanced_operations import AdvancedOperationsModule
                    AdvancedOperationsModule.render()
                elif cloud_provider == "Azure":
                    from azure_modules_advanced_operations import AzureAdvancedOperationsModule
                    AzureAdvancedOperationsModule.render()
            
            # Module 10: Security, Compliance & AI
            elif module_name == "Security":
                if cloud_provider == "AWS":
                    from modules_security_compliance import UnifiedSecurityComplianceModule
                    UnifiedSecurityComplianceModule.render()
                elif cloud_provider == "Azure":
                    from azure_modules_security_compliance import AzureSecurityComplianceModule
                    AzureSecurityComplianceModule.render()
            
            # Module 11: Container Management (EKS/AKS)
            elif module_name == "Container Management":
                if cloud_provider == "AWS":
                    from modules_eks_management import EKSManagementModule
                    EKSManagementModule.render()
                elif cloud_provider == "Azure":
                    from azure_modules_aks_management import AzureAKSManagementModule
                    AzureAKSManagementModule.render()
            
            # Module 12: FinOps & Cost
            elif module_name == "FinOps & Cost":
                if cloud_provider == "AWS":
                    from modules_finops import FinOpsModule
                    FinOpsModule.render()
                elif cloud_provider == "Azure":
                    from azure_modules_finops import AzureFinOpsModule
                    AzureFinOpsModule.render()
            
            # Module 13: Account/Subscription Lifecycle
            elif module_name == "Lifecycle":
                if cloud_provider == "AWS":
                    from modules_account_lifecycle import AccountLifecycleModule
                    AccountLifecycleModule.render()
                elif cloud_provider == "Azure":
                    from azure_modules_subscription_lifecycle import AzureSubscriptionLifecycleModule
                    AzureSubscriptionLifecycleModule.render()
            
            # Module 14: Developer Experience
            elif module_name == "Developer Experience":
                if cloud_provider == "AWS":
                    from modules_devex import DevExModule
                    DevExModule.render()
                elif cloud_provider == "Azure":
                    from azure_modules_devex import AzureDevExModule
                    AzureDevExModule.render()
            
            # Module 15: AI Assistant
            elif module_name == "AI Assistant":
                if cloud_provider == "AWS":
                    from modules_ai_assistant import AIAssistantModule
                    AIAssistantModule.render()
                elif cloud_provider == "Azure":
                    from azure_modules_ai_assistant import AzureAIAssistantModule
                    AzureAIAssistantModule.render()
                    
        except Exception as e:
            st.error(f"Error loading {module_name} for {cloud_provider}: {str(e)}")
            st.info(f"Module under development for {cloud_provider}. Please check back later.")
