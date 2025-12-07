"""
Multi-Cloud Global Sidebar Component
Supports AWS and Azure with provider-specific filters
"""

import streamlit as st
from core_session_manager import SessionManager
from config_settings import AppConfig
from datetime import datetime

class GlobalSidebar:
    """Global sidebar with cloud provider-aware filters and controls"""
    
    @staticmethod
    def render():
        """Render global sidebar based on selected cloud provider"""
        
        # Initialize session state first
        SessionManager.initialize()
        
        # Get cloud provider
        cloud_provider = st.session_state.get('cloud_provider', 'AWS')
        
        with st.sidebar:
            # Cloud Provider Display
            if cloud_provider == "AWS":
                st.markdown("### 🔶 AWS Mode")
            elif cloud_provider == "Azure":
                st.markdown("### 🔷 Azure Mode")
            
            st.markdown("---")
            
            # Demo/Live Mode Toggle
            st.markdown("### 🔄 Data Mode")
            mode = st.radio(
                "Select Mode",
                ["Live", "Demo"],
                index=0 if st.session_state.get('mode', 'Live') == 'Live' else 1,
                help=f"Live: Real {cloud_provider} data | Demo: Sample data for testing",
                horizontal=True
            )
            
            if mode != st.session_state.get('mode'):
                st.session_state.mode = mode
                st.rerun()
            
            if mode == "Demo":
                st.info(f"📊 Demo Mode - Using sample {cloud_provider} data")
            else:
                st.success(f"🔴 Live - Real {cloud_provider} data")
            
            st.markdown("---")
            
            # Render provider-specific filters
            if cloud_provider == "AWS":
                GlobalSidebar._render_aws_filters()
            elif cloud_provider == "Azure":
                GlobalSidebar._render_azure_filters()
            
            st.markdown("---")
            
            # Time range for analytics (common for both)
            st.markdown("### 📅 Time Range")
            time_range = st.selectbox(
                "Period",
                options=['Last 24 Hours', 'Last 7 Days', 'Last 30 Days', 'Last 90 Days'],
                index=2
            )
            
            st.session_state.time_range = time_range
            
            st.markdown("---")
            
            # Refresh controls (common for both)
            st.markdown("### 🔄 Data Refresh")
            
            last_refresh = SessionManager.get('last_refresh', datetime.now())
            st.caption(f"Last refresh: {last_refresh.strftime('%H:%M:%S')}")
            
            if st.button("🔄 Refresh Now", use_container_width=True):
                SessionManager.trigger_refresh()
                st.cache_data.clear()
                st.rerun()
            
            auto_refresh = st.checkbox("Auto-refresh (5 min)", value=False)
            if auto_refresh:
                import time
                time.sleep(300)  # 5 minutes
                st.rerun()
            
            st.markdown("---")
            
            # Platform stats (provider-specific)
            if cloud_provider == "AWS":
                GlobalSidebar._render_aws_stats()
            elif cloud_provider == "Azure":
                GlobalSidebar._render_azure_stats()
    
    @staticmethod
    def _render_aws_filters():
        """Render AWS-specific filters"""
        
        st.markdown("### 🎛️ AWS Filters")
        
        # Load AWS accounts
        accounts = AppConfig.load_aws_accounts()
        active_accounts = [acc for acc in accounts if acc.status == 'active']
        
        # Account selector
        account_options = ['All Accounts'] + [f"{acc.account_name} ({acc.account_id})" for acc in active_accounts]
        selected_account = st.selectbox(
            "Account",
            options=account_options,
            help="Select AWS account to filter resources"
        )
        
        # Update session state based on selection
        if selected_account == 'All Accounts':
            st.session_state.selected_accounts = 'all'
        else:
            # Extract account ID from selection
            account_id = selected_account.split('(')[1].split(')')[0]
            st.session_state.selected_accounts = account_id
        
        # Region selector
        region_options = ['All Regions'] + AppConfig.DEFAULT_REGIONS
        selected_region = st.selectbox(
            "Region",
            options=region_options,
            help="Select AWS region"
        )
        
        # Update session state
        if selected_region == 'All Regions':
            st.session_state.selected_regions = 'all'
        else:
            st.session_state.selected_regions = selected_region
        
        # Environment filter
        env_options = ['All Environments', 'Production', 'Development', 'Staging', 'Sandbox']
        selected_env = st.selectbox(
            "Environment",
            options=env_options
        )
        
        st.session_state.selected_environment = 'all' if selected_env == 'All Environments' else selected_env.lower()
    
    @staticmethod
    def _render_azure_filters():
        """Render Azure-specific filters"""
        
        st.markdown("### 🎛️ Azure Filters")
        
        # Load Azure subscriptions
        subscriptions = AppConfig.load_azure_subscriptions()
        active_subscriptions = [sub for sub in subscriptions if sub.status == 'active']
        
        # Subscription selector
        subscription_options = ['All Subscriptions'] + [f"{sub.subscription_name} ({sub.subscription_id[:8]}...)" for sub in active_subscriptions]
        selected_subscription = st.selectbox(
            "Subscription",
            options=subscription_options,
            help="Select Azure subscription to filter resources"
        )
        
        # Update session state based on selection
        if selected_subscription == 'All Subscriptions':
            st.session_state.selected_subscriptions = 'all'
        else:
            # Extract subscription ID from selection
            sub_id = selected_subscription.split('(')[1].split(')')[0].replace('...', '')
            st.session_state.selected_subscriptions = sub_id
        
        # Azure Region selector
        azure_regions = [
            'All Regions',
            'East US',
            'East US 2',
            'West US',
            'West US 2',
            'Central US',
            'North Europe',
            'West Europe',
            'Southeast Asia',
            'East Asia',
            'UK South',
            'UK West',
            'Canada Central',
            'Canada East',
            'Australia East',
            'Australia Southeast'
        ]
        
        selected_region = st.selectbox(
            "Region",
            options=azure_regions,
            help="Select Azure region"
        )
        
        # Update session state
        if selected_region == 'All Regions':
            st.session_state.selected_regions = 'all'
        else:
            st.session_state.selected_regions = selected_region
        
        # Resource Group filter
        rg_options = ['All Resource Groups', 'Production-RG', 'Development-RG', 'Staging-RG', 'Sandbox-RG']
        selected_rg = st.selectbox(
            "Resource Group",
            options=rg_options
        )
        
        st.session_state.selected_resource_group = 'all' if selected_rg == 'All Resource Groups' else selected_rg
        
        # Environment filter
        env_options = ['All Environments', 'Production', 'Development', 'Staging', 'Sandbox']
        selected_env = st.selectbox(
            "Environment",
            options=env_options
        )
        
        st.session_state.selected_environment = 'all' if selected_env == 'All Environments' else selected_env.lower()
    
    @staticmethod
    def _render_aws_stats():
        """Render AWS platform stats"""
        
        st.markdown("### 📊 AWS Platform Stats")
        
        accounts = AppConfig.load_aws_accounts()
        active_accounts = [acc for acc in accounts if acc.status == 'active']
        
        st.metric("Connected Accounts", len(active_accounts))
        st.metric("Active Regions", len(AppConfig.DEFAULT_REGIONS))
        
        # Account health
        st.markdown("### 🏥 Account Health")
        for acc in active_accounts[:3]:  # Show first 3
            status_icon = "✅" if acc.status == "active" else "❌"
            st.caption(f"{status_icon} {acc.account_name}")
        
        if len(active_accounts) > 3:
            st.caption(f"... and {len(active_accounts) - 3} more")
    
    @staticmethod
    def _render_azure_stats():
        """Render Azure platform stats"""
        
        st.markdown("### 📊 Azure Platform Stats")
        
        subscriptions = AppConfig.load_azure_subscriptions()
        active_subscriptions = [sub for sub in subscriptions if sub.status == 'active']
        
        st.metric("Connected Subscriptions", len(active_subscriptions))
        st.metric("Active Regions", 16)  # Common Azure regions
        
        # Subscription health
        st.markdown("### 🏥 Subscription Health")
        for sub in active_subscriptions[:3]:  # Show first 3
            status_icon = "✅" if sub.status == "active" else "❌"
            st.caption(f"{status_icon} {sub.subscription_name}")
        
        if len(active_subscriptions) > 3:
            st.caption(f"... and {len(active_subscriptions) - 3} more")
