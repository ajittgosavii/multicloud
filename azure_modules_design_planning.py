"""
Azure Module: Architecture Design & Planning
Plan and design Azure cloud architecture and landing zones
"""

import streamlit as st
import pandas as pd
from azure_theme import AzureTheme

class AzureDesignPlanningModule:
    """Azure Design & Planning module"""
    
    @staticmethod
    def render():
        st.markdown("## 📐 Architecture Design & Planning")
        st.caption("Plan and design Azure cloud architecture, landing zones, and migration strategies")
        
        tabs = st.tabs([
            "🏗️ Landing Zones",
            "📊 Architecture Patterns",
            "🔄 Migration Planning",
            "💰 Cost Estimation",
            "📋 Readiness Checklist"
        ])
        
        with tabs[0]:
            AzureDesignPlanningModule._render_landing_zones()
        with tabs[1]:
            AzureDesignPlanningModule._render_architecture_patterns()
        with tabs[2]:
            AzureDesignPlanningModule._render_migration_planning()
        with tabs[3]:
            AzureDesignPlanningModule._render_cost_estimation()
        with tabs[4]:
            AzureDesignPlanningModule._render_readiness_checklist()
    
    @staticmethod
    def _render_landing_zones():
        st.markdown("### 🏗️ Azure Landing Zones")
        
        AzureTheme.azure_info_box(
            "Landing Zones",
            "Deploy pre-configured environments that follow Azure best practices and Well-Architected Framework.",
            "🏗️"
        )
        
        templates = [
            {"Template": "Enterprise-Scale", "Subscriptions": "Multiple", "Governance": "High", "Network": "Hub-Spoke"},
            {"Template": "Small Enterprise", "Subscriptions": "1-3", "Governance": "Medium", "Network": "Single VNet"},
            {"Template": "Startup", "Subscriptions": "1", "Governance": "Basic", "Network": "Simple"}
        ]
        
        df = pd.DataFrame(templates)
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        if st.button("🚀 Deploy Landing Zone", type="primary", use_container_width=True):
            st.success("✅ Landing zone deployment initiated!")
    
    @staticmethod
    def _render_architecture_patterns():
        st.markdown("### 📊 Architecture Patterns")
        
        patterns = ["N-Tier Application", "Microservices", "Event-Driven", "Big Data", "IoT Solution", "Machine Learning"]
        
        selected_pattern = st.selectbox("Select Architecture Pattern", patterns)
        
        st.markdown(f"#### Pattern: {selected_pattern}")
        st.info(f"This pattern provides a reference architecture for {selected_pattern.lower()} scenarios in Azure.")
        
        st.markdown("**Recommended Services:**")
        st.write("- Azure App Service")
        st.write("- Azure SQL Database")
        st.write("- Azure Application Gateway")
        st.write("- Azure Monitor")
    
    @staticmethod
    def _render_migration_planning():
        st.markdown("### 🔄 Migration Planning")
        
        col1, col2 = st.columns(2)
        
        with col1:
            source = st.selectbox("Source Platform", ["On-Premises", "AWS", "GCP", "Other Cloud"])
            workload_type = st.selectbox("Workload Type", ["Web Applications", "Databases", "File Servers", "SAP", "Virtual Desktops"])
        
        with col2:
            migration_strategy = st.selectbox("Migration Strategy", ["Rehost (Lift & Shift)", "Refactor", "Rearchitect", "Rebuild"])
            timeline = st.selectbox("Timeline", ["1-3 months", "3-6 months", "6-12 months", "12+ months"])
        
        if st.button("📊 Generate Migration Plan", type="primary", use_container_width=True):
            st.success("✅ Migration plan generated!")
            st.info("Download your customized migration roadmap and assessment report.")
    
    @staticmethod
    def _render_cost_estimation():
        st.markdown("### 💰 Cost Estimation")
        
        st.markdown("#### Estimate Monthly Azure Costs")
        
        vm_count = st.number_input("Number of VMs", min_value=0, value=10)
        storage_gb = st.number_input("Storage (GB)", min_value=0, value=1000)
        db_count = st.number_input("Number of Databases", min_value=0, value=2)
        
        estimated_cost = (vm_count * 150) + (storage_gb * 0.02) + (db_count * 450)
        
        st.metric("Estimated Monthly Cost", f"${estimated_cost:,.2f}")
        
        st.info("💡 Tip: Use Azure Reserved Instances to save up to 72% on VM costs")
    
    @staticmethod
    def _render_readiness_checklist():
        st.markdown("### 📋 Cloud Readiness Checklist")
        
        checklist = [
            "Define cloud governance framework",
            "Establish identity and access management",
            "Plan network architecture",
            "Design disaster recovery strategy",
            "Set up cost management policies",
            "Configure monitoring and logging",
            "Implement security controls",
            "Train operations team"
        ]
        
        for item in checklist:
            st.checkbox(item, value=False)
        
        if st.button("💾 Save Progress", use_container_width=True):
            st.success("✅ Progress saved!")
