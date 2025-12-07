"""
Azure Module: Security & Compliance
Azure Security Center, Key Vault, and compliance management
"""

import streamlit as st
import pandas as pd
from azure_theme import AzureTheme
import plotly.express as px

class AzureSecurityComplianceModule:
    """Azure Security & Compliance module"""
    
    @staticmethod
    def render():
        st.markdown("## 🔒 Security & Compliance")
        st.caption("Manage Azure Security Center, compliance, and security posture")
        
        tabs = st.tabs([
            "📊 Security Posture",
            "🔐 Security Center",
            "🔑 Key Vault",
            "✅ Compliance",
            "🛡️ Microsoft Defender",
            "📋 Recommendations"
        ])
        
        with tabs[0]:
            AzureSecurityComplianceModule._render_security_posture()
        with tabs[1]:
            AzureSecurityComplianceModule._render_security_center()
        with tabs[2]:
            AzureSecurityComplianceModule._render_key_vault()
        with tabs[3]:
            AzureSecurityComplianceModule._render_compliance()
        with tabs[4]:
            AzureSecurityComplianceModule._render_defender()
        with tabs[5]:
            AzureSecurityComplianceModule._render_recommendations()
    
    @staticmethod
    def _render_security_posture():
        st.markdown("### 📊 Security Posture Dashboard")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            AzureTheme.azure_metric_card("Secure Score", "85%", "🛡️", "+5% this month")
        with col2:
            AzureTheme.azure_metric_card("High Alerts", "3", "🚨", "-2 this week")
        with col3:
            AzureTheme.azure_metric_card("Compliant Resources", "94.2%", "✅")
        with col4:
            AzureTheme.azure_metric_card("Recommendations", "23", "💡")
        
        st.markdown("---")
        
        # Security score trend
        st.markdown("#### 📈 Secure Score Trend")
        
        dates = pd.date_range(start='2024-06-01', end='2024-12-01', freq='M')
        scores = [72, 75, 78, 80, 82, 84, 85]
        
        fig = px.line(x=dates, y=scores, markers=True)
        fig.update_traces(line_color='#0078D4', marker=dict(size=8, color='#50E6FF'))
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(family='Segoe UI', color='#004E8C'),
            xaxis_title="Month",
            yaxis_title="Secure Score (%)"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    @staticmethod
    def _render_security_center():
        st.markdown("### 🔐 Azure Security Center")
        
        AzureTheme.azure_info_box(
            "Security Center",
            "Unified security management and advanced threat protection across hybrid cloud workloads.",
            "🔐"
        )
        
        # Alerts
        st.markdown("#### 🚨 Active Security Alerts")
        
        alerts = [
            {"Severity": "🔴 High", "Alert": "Suspicious PowerShell execution", "Resource": "prod-vm-01", "Time": "2 hours ago"},
            {"Severity": "🟠 Medium", "Alert": "Unusual network traffic", "Resource": "prod-web-app", "Time": "5 hours ago"},
            {"Severity": "🟡 Low", "Alert": "Missing OS updates", "Resource": "dev-vm-03", "Time": "1 day ago"}
        ]
        
        df = pd.DataFrame(alerts)
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        if st.button("🔍 Investigate Alert", use_container_width=True):
            st.info("Opening alert investigation workspace...")
    
    @staticmethod
    def _render_key_vault():
        st.markdown("### 🔑 Azure Key Vault")
        
        st.info("Safeguard cryptographic keys and secrets used by cloud applications and services")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Key Vaults", "5")
        with col2:
            st.metric("Total Secrets", "234")
        with col3:
            st.metric("Certificates", "12")
        
        st.markdown("---")
        
        vaults = [
            {"Name": "prod-kv-main", "Secrets": 45, "Keys": 8, "Certificates": 3, "Location": "East US"},
            {"Name": "shared-kv-001", "Secrets": 89, "Keys": 12, "Certificates": 5, "Location": "West US"}
        ]
        
        df = pd.DataFrame(vaults)
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        if st.button("➕ Create Key Vault", type="primary", use_container_width=True):
            st.success("✅ Key Vault creation wizard opened!")
    
    @staticmethod
    def _render_compliance():
        st.markdown("### ✅ Compliance Dashboard")
        
        # Compliance standards
        standards = ["Azure Security Benchmark", "PCI DSS", "HIPAA", "ISO 27001", "SOC 2"]
        
        selected_standard = st.selectbox("Select Compliance Standard", standards)
        
        st.markdown(f"#### Compliance: {selected_standard}")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Overall Compliance", "94.5%")
        with col2:
            st.metric("Passed Controls", "89/94")
        with col3:
            st.metric("Failed Controls", "5/94")
        
        st.markdown("---")
        
        # Failed controls
        failed_controls = [
            {"Control": "Enable MFA for all users", "Severity": "High", "Resources": 23, "Status": "❌ Failed"},
            {"Control": "Encrypt data at rest", "Severity": "Medium", "Resources": 12, "Status": "❌ Failed"}
        ]
        
        df = pd.DataFrame(failed_controls)
        st.dataframe(df, use_container_width=True, hide_index=True)
    
    @staticmethod
    def _render_defender():
        st.markdown("### 🛡️ Microsoft Defender for Cloud")
        
        defender_plans = [
            {"Plan": "Defender for Servers", "Status": "✅ Enabled", "Protected Resources": 234},
            {"Plan": "Defender for Storage", "Status": "✅ Enabled", "Protected Resources": 156},
            {"Plan": "Defender for SQL", "Status": "✅ Enabled", "Protected Resources": 45},
            {"Plan": "Defender for Containers", "Status": "⏸️ Disabled", "Protected Resources": 0}
        ]
        
        df = pd.DataFrame(defender_plans)
        st.dataframe(df, use_container_width=True, hide_index=True)
    
    @staticmethod
    def _render_recommendations():
        st.markdown("### 💡 Security Recommendations")
        
        recommendations = [
            {"Recommendation": "Enable disk encryption for VMs", "Impact": "High", "Resources": 45, "Effort": "Medium"},
            {"Recommendation": "Rotate storage account keys", "Impact": "Medium", "Resources": 23, "Effort": "Low"},
            {"Recommendation": "Update NSG rules", "Impact": "Low", "Resources": 12, "Effort": "Low"}
        ]
        
        df = pd.DataFrame(recommendations)
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        if st.button("🔧 Apply Recommendations", type="primary", use_container_width=True):
            st.success("✅ Remediation workflow started!")
