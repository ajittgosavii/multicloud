"""
Multi-Cloud Session Manager
Manages session state for AWS, Azure, and GCP
"""

import streamlit as st
from datetime import datetime
from typing import Any, Dict

class SessionManager:
    """Centralized session state management for multi-cloud platform"""
    
    @staticmethod
    def initialize():
        """Initialize session state with defaults"""
        
        defaults = {
            # Cloud provider settings
            'cloud_provider': 'AWS',
            
            # Common settings
            'mode': 'Live',
            'time_range': 'Last 30 Days',
            'last_refresh': datetime.now(),
            
            # AWS specific
            'selected_accounts': 'all',
            'selected_regions': 'all',
            
            # Azure specific
            'selected_subscriptions': 'all',
            'selected_resource_group': 'all',
            
            # GCP specific (for future)
            'selected_projects': 'all',
            
            # Common filters
            'selected_environment': 'all',
            
            # Navigation
            'active_module': 'Dashboard',
            
            # User preferences
            'theme_preference': 'auto',
            
            # Cache
            'cache_enabled': True,
            'cache_ttl': 300,  # 5 minutes
            
            # Feature flags
            'feature_ai_assistant': True,
            'feature_auto_refresh': False,
        }
        
        for key, value in defaults.items():
            if key not in st.session_state:
                st.session_state[key] = value
    
    @staticmethod
    def get(key: str, default: Any = None) -> Any:
        """Get session state value"""
        return st.session_state.get(key, default)
    
    @staticmethod
    def set(key: str, value: Any):
        """Set session state value"""
        st.session_state[key] = value
    
    @staticmethod
    def trigger_refresh():
        """Trigger data refresh"""
        st.session_state.last_refresh = datetime.now()
    
    @staticmethod
    def get_active_account_count() -> int:
        """Get count of active AWS accounts"""
        from config_settings import AppConfig
        accounts = AppConfig.load_aws_accounts()
        return len([acc for acc in accounts if acc.status == 'active'])
    
    @staticmethod
    def get_active_subscription_count() -> int:
        """Get count of active Azure subscriptions"""
        from config_settings import AppConfig
        subscriptions = AppConfig.load_azure_subscriptions()
        return len([sub for sub in subscriptions if sub.status == 'active'])
    
    @staticmethod
    def get_active_project_count() -> int:
        """Get count of active GCP projects (for future use)"""
        from config_settings import AppConfig
        projects = AppConfig.load_gcp_projects()
        return len([proj for proj in projects if proj.status == 'active'])
    
    @staticmethod
    def get_cloud_context() -> Dict:
        """Get current cloud context"""
        provider = st.session_state.get('cloud_provider', 'AWS')
        
        if provider == 'AWS':
            return {
                'provider': 'AWS',
                'account': st.session_state.get('selected_accounts', 'all'),
                'region': st.session_state.get('selected_regions', 'all'),
                'environment': st.session_state.get('selected_environment', 'all')
            }
        elif provider == 'Azure':
            return {
                'provider': 'Azure',
                'subscription': st.session_state.get('selected_subscriptions', 'all'),
                'location': st.session_state.get('selected_regions', 'all'),
                'resource_group': st.session_state.get('selected_resource_group', 'all'),
                'environment': st.session_state.get('selected_environment', 'all')
            }
        elif provider == 'GCP':
            return {
                'provider': 'GCP',
                'project': st.session_state.get('selected_projects', 'all'),
                'region': st.session_state.get('selected_regions', 'all'),
                'environment': st.session_state.get('selected_environment', 'all')
            }
        
        return {}
    
    @staticmethod
    def switch_cloud_provider(provider: str):
        """Switch cloud provider and reset filters"""
        st.session_state.cloud_provider = provider
        st.session_state.active_module = 'Dashboard'
        
        # Reset filters
        st.session_state.selected_environment = 'all'
        st.session_state.selected_regions = 'all'
        
        if provider == 'AWS':
            st.session_state.selected_accounts = 'all'
        elif provider == 'Azure':
            st.session_state.selected_subscriptions = 'all'
            st.session_state.selected_resource_group = 'all'
        elif provider == 'GCP':
            st.session_state.selected_projects = 'all'
