
# azure_modules_cicd_unified.py
import streamlit as st
import pandas as pd
from azure_theme import AzureTheme

class AzureUnifiedCICDModule:
    @staticmethod
    def render():
        st.markdown("## 📄 Azure DevOps CI/CD Pipelines")
        st.caption("Manage Azure DevOps pipelines and deployment automation")
        
        tabs = st.tabs(["📊 Overview", "🔧 Pipelines", "🚀 Releases", "📦 Artifacts", "⚙️ Settings"])
        
        with tabs[0]:
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                AzureTheme.azure_metric_card("Pipelines", "23", "🔧")
            with col2:
                AzureTheme.azure_metric_card("Successful Runs", "156", "✅")
            with col3:
                AzureTheme.azure_metric_card("Failed Runs", "12", "❌")
            with col4:
                AzureTheme.azure_metric_card("Avg Duration", "4m 32s", "⏱️")
            
            st.markdown("---")
            
            recent_runs = [
                {"Pipeline": "prod-web-app-ci", "Status": "✅ Succeeded", "Trigger": "Push", "Duration": "3m 45s", "Time": "2 hours ago"},
                {"Pipeline": "staging-api-cd", "Status": "✅ Succeeded", "Trigger": "Manual", "Duration": "5m 20s", "Time": "4 hours ago"},
                {"Pipeline": "dev-build-ci", "Status": "❌ Failed", "Trigger": "PR", "Duration": "2m 10s", "Time": "6 hours ago"}
            ]
            df = pd.DataFrame(recent_runs)
            st.dataframe(df, use_container_width=True, hide_index=True)
        
        with tabs[1]:
            st.markdown("### 🔧 Azure Pipelines")
            
            if st.button("➕ Create New Pipeline", type="primary", use_container_width=True):
                st.success("✅ Pipeline wizard opened!")
            
            pipelines = [
                {"Name": "prod-web-app-ci", "Type": "CI", "Repo": "azure-repos/web-app", "Trigger": "main branch"},
                {"Name": "staging-api-cd", "Type": "CD", "Repo": "azure-repos/api", "Trigger": "manual"}
            ]
            df = pd.DataFrame(pipelines)
            st.dataframe(df, use_container_width=True, hide_index=True)

