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
    
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 30px;
        border-radius: 15px;
        margin-bottom: 30px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.2);
        text-align: center;
    ">
        <h1 style="color: white; margin: 0;">
            ☁️ Multi-Cloud Infrastructure Platform
        </h1>
        <p style="color: rgba(255,255,255,0.9); font-size: 1.1em; margin-top: 10px;">
            Enterprise Cloud Management - AWS | Azure | GCP
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Cloud Provider Radio Buttons - Large and Centered
    st.markdown("### 🌐 Select Your Cloud Provider")
    
    # Initialize cloud provider if not set
    if 'cloud_provider' not in st.session_state:
        st.session_state.cloud_provider = 'AWS'
    
    # Create columns for centered radio buttons
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        provider = st.radio(
            "Choose Cloud Platform:",
            options=["AWS", "Azure", "GCP"],
            horizontal=True,
            key="cloud_selector",
            label_visibility="visible"
        )
        
        # Update session state
        if provider != st.session_state.cloud_provider:
            st.session_state.cloud_provider = provider
            st.rerun()
    
    # Show provider info
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.session_state.cloud_provider == "AWS":
        st.success("🔶 **AWS Mode Active** - Amazon Web Services modules loaded")
        AWSTheme.apply_aws_theme()
        
    elif st.session_state.cloud_provider == "Azure":
        st.info("🔷 **Azure Mode Active** - Microsoft Azure modules loaded")
        AzureTheme.apply_azure_theme()
        
    elif st.session_state.cloud_provider == "GCP":
        st.warning("⚠️ **GCP Coming Soon** - Google Cloud Platform support in development")
        st.markdown("""
        ### GCP Support
        
        Google Cloud Platform integration is currently under development.
        
        **Available Now:**
        - AWS (Full Support)
        - Azure (Full Support)
        
        **Coming Soon:**
        - GCP (In Development)
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
