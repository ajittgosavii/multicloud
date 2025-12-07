"""
CloudIDP Multi-Cloud Platform v3.0
Enterprise Multi-Cloud Infrastructure Development Platform
"""

import streamlit as st
from datetime import datetime
import sys
from pathlib import Path

# Add current directory to path
sys.path.append(str(Path(__file__).parent))

# Import components
try:
    from config_settings import AppConfig
    from core_session_manager import SessionManager
    from components_navigation import Navigation
    from components_sidebar import GlobalSidebar
    from aws_theme import AWSTheme
    from azure_theme import AzureTheme
except ImportError as e:
    st.error(f"Import error: {e}")
    st.stop()

# Page configuration
st.set_page_config(
    page_title="CloudIDP Multi-Cloud Platform",
    page_icon="☁️",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    """Main application entry point"""
    
    # Initialize session
    SessionManager.initialize()
    
    # ========================================================================
    # CLOUD PROVIDER SELECTION - PROMINENT AT TOP
    # ========================================================================
    
    # Purple gradient header - neutral for cloud selection
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 30px;
        border-radius: 12px;
        margin-bottom: 25px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        text-align: center;
    ">
        <h1 style="color: white; margin: 0; font-weight: 600;">
            ☁️ CloudIDP Multi-Cloud Platform v3.0
        </h1>
        <p style="color: rgba(255,255,255,0.95); font-size: 1.1em; margin-top: 10px;">
            Enterprise Cloud Infrastructure Development Platform
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Cloud Provider Radio Buttons
    st.markdown("### 🌐 Select Cloud Provider")
    
    # Initialize cloud provider if not set
    if 'cloud_provider' not in st.session_state:
        st.session_state.cloud_provider = 'AWS'
    
    # Radio buttons for cloud selection
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        provider = st.radio(
            "Cloud Platform",
            options=["AWS", "Azure", "GCP"],
            horizontal=True,
            key="cloud_selector"
        )
        
        # Update session state
        if provider != st.session_state.cloud_provider:
            st.session_state.cloud_provider = provider
            st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Apply theme and show cloud-specific header
    if st.session_state.cloud_provider == "AWS":
        AWSTheme.apply_aws_theme()
        st.markdown(AWSTheme.aws_header(
            "CloudIDP Multi-Cloud Platform",
            "Enterprise Multi-Account Cloud Infrastructure Development Platform | AWS Mode"
        ), unsafe_allow_html=True)
        AWSTheme.aws_info_box(
            "<strong>Amazon Web Services</strong> - Full feature set available"
        )
        
    elif st.session_state.cloud_provider == "Azure":
        AzureTheme.apply_azure_theme()
        st.markdown(AzureTheme.azure_header(
            "CloudIDP Multi-Cloud Platform",
            "Enterprise Multi-Subscription Cloud Infrastructure Development Platform | Azure Mode"
        ), unsafe_allow_html=True)
        AzureTheme.azure_info_box(
            "<strong>Microsoft Azure</strong> - Full feature set available"
        )
        
    elif st.session_state.cloud_provider == "GCP":
        st.warning("⚠️ **GCP Coming Soon** - Google Cloud Platform support in development")
        st.markdown("""
        ### GCP Support
        
        Google Cloud Platform integration is currently under development.
        
        **Available Now:**
        - ✅ AWS (Full Support)
        - ✅ Azure (Full Support)
        
        **Coming Soon:**
        - 🔄 GCP (In Development)
        """)
        st.stop()
    
    st.markdown("---")
    
    # ========================================================================
    # RENDER NAVIGATION & CONTENT FOR SELECTED CLOUD
    # ========================================================================
    
    # Render sidebar
    GlobalSidebar.render(st.session_state.cloud_provider)
    
    # Render navigation based on cloud provider
    Navigation.render(st.session_state.cloud_provider)

if __name__ == "__main__":
    main()
