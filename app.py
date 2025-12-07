"""
CloudIDP Multi-Cloud Platform v3.0
Enterprise Multi-Cloud Infrastructure Development Platform
Supports: AWS | Azure | GCP (Coming Soon)
"""

import streamlit as st
from datetime import datetime
import sys
from pathlib import Path

# Add src to path
sys.path.append(str(Path(__file__).parent / "src"))

from config_settings import AppConfig
from core_session_manager import SessionManager
from components_navigation import Navigation
from components_sidebar import GlobalSidebar
from aws_theme import AWSTheme
from azure_theme import AzureTheme

# Page configuration
st.set_page_config(
    page_title="CloudIDP Multi-Cloud Platform v3.0",
    page_icon="☁️",
    layout="wide",
    initial_sidebar_state="expanded"
)

def apply_cloud_theme(provider: str):
    """Apply theme based on selected cloud provider"""
    if provider == "AWS":
        AWSTheme.apply_aws_theme()
    elif provider == "Azure":
        AzureTheme.apply_azure_theme()
    # GCP theme will be added later

def main():
    """Main application entry point"""
    
    # Initialize session
    SessionManager.initialize()
    
    # Cloud Provider Selection - TOP OF PAGE (before any other content)
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    ">
        <h2 style="color: white; margin: 0; text-align: center;">
            ☁️ CloudIDP Multi-Cloud Platform v3.0
        </h2>
        <p style="color: white; margin: 5px 0 0 0; text-align: center; opacity: 0.9;">
            Enterprise Cloud Infrastructure Development Platform
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Cloud Provider Selector
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("### 🌐 Select Cloud Provider")
        
        # Initialize cloud provider in session state
        if 'cloud_provider' not in st.session_state:
            st.session_state.cloud_provider = 'AWS'
        
        provider = st.radio(
            "Cloud Platform",
            options=["AWS", "Azure", "GCP (Coming Soon)"],
            horizontal=True,
            key="cloud_provider_selector",
            index=["AWS", "Azure", "GCP (Coming Soon)"].index(st.session_state.cloud_provider) 
                if st.session_state.cloud_provider in ["AWS", "Azure", "GCP (Coming Soon)"] else 0
        )
        
        # Update session state if changed
        if provider != st.session_state.cloud_provider:
            st.session_state.cloud_provider = provider
            st.rerun()
        
        # Show info about selected provider
        if provider == "AWS":
            st.info("🔶 **Amazon Web Services** - Full feature set available")
        elif provider == "Azure":
            st.info("🔷 **Microsoft Azure** - Full feature set available")
        elif provider == "GCP (Coming Soon)":
            st.warning("🟡 **Google Cloud Platform** - Coming in next release")
            st.stop()  # Don't render rest of app for GCP yet
    
    st.markdown("---")
    
    # Apply theme based on provider
    apply_cloud_theme(st.session_state.cloud_provider)
    
    # Render provider-specific header
    if st.session_state.cloud_provider == "AWS":
        AWSTheme.aws_header(
            "CloudIDP Multi-Cloud Platform",
            "Enterprise Multi-Account Cloud Infrastructure Development Platform | AWS Mode"
        )
    elif st.session_state.cloud_provider == "Azure":
        AzureTheme.azure_header(
            "CloudIDP Multi-Cloud Platform",
            "Enterprise Multi-Subscription Cloud Infrastructure Development Platform | Azure Mode"
        )
    
    # Render global sidebar
    GlobalSidebar.render()
    
    # Render main navigation
    Navigation.render()
    
    # Cloud-specific footer
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.caption(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    with col2:
        if st.session_state.cloud_provider == "AWS":
            st.caption(f"🔗 Connected Accounts: {SessionManager.get_active_account_count()}")
        elif st.session_state.cloud_provider == "Azure":
            st.caption(f"🔗 Connected Subscriptions: {SessionManager.get_active_subscription_count()}")
    with col3:
        st.caption(f"🚀 CloudIDP v3.0 - {st.session_state.cloud_provider} Mode")

if __name__ == "__main__":
    main()
