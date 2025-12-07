"""
Azure Module: FinOps & Cost Management
Cost analysis, optimization, and financial operations
"""

import streamlit as st
import pandas as pd
from azure_theme import AzureTheme
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

class AzureFinOpsModule:
    """Azure FinOps & Cost Management module"""
    
    @staticmethod
    def render():
        st.markdown("## 💰 FinOps & Cost Management")
        st.caption("Cost analysis, budgets, optimization, and financial operations")
        
        tabs = st.tabs([
            "📊 Cost Dashboard",
            "💰 Cost Analysis",
            "🎯 Budgets & Alerts",
            "💡 Optimization",
            "📈 Forecasting",
            "📋 Reports"
        ])
        
        with tabs[0]:
            AzureFinOpsModule._render_cost_dashboard()
        with tabs[1]:
            AzureFinOpsModule._render_cost_analysis()
        with tabs[2]:
            AzureFinOpsModule._render_budgets()
        with tabs[3]:
            AzureFinOpsModule._render_optimization()
        with tabs[4]:
            AzureFinOpsModule._render_forecasting()
        with tabs[5]:
            AzureFinOpsModule._render_reports()
    
    @staticmethod
    def _render_cost_dashboard():
        st.markdown("### 📊 Cost Dashboard")
        
        # Key metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            AzureTheme.azure_metric_card("Current Month", "$142,890", "💰", "-8.3% vs last month")
        with col2:
            AzureTheme.azure_metric_card("Forecast (Month End)", "$156,400", "📊", "+5.2%")
        with col3:
            AzureTheme.azure_metric_card("Savings Opportunities", "$23,450", "💡")
        with col4:
            AzureTheme.azure_metric_card("Reserved Instances", "34%", "📦", "+5% coverage")
        
        st.markdown("---")
        
        # Cost trend
        st.markdown("#### 📈 Monthly Cost Trend")
        
        months = pd.date_range(start='2024-01-01', end='2024-12-01', freq='M')
        costs = [125000, 130000, 128000, 135000, 142000, 138000, 145000, 148000, 152000, 149000, 147000, 142890]
        
        fig = px.line(x=months, y=costs, markers=True)
        fig.update_traces(line_color='#0078D4', marker=dict(size=8, color='#50E6FF'))
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(family='Segoe UI', color='#004E8C'),
            xaxis_title="Month",
            yaxis_title="Cost (USD)"
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Top cost services
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 💸 Top Cost Services")
            
            services_cost = {
                'Virtual Machines': 45230,
                'SQL Database': 28450,
                'Storage': 18900,
                'App Services': 15670,
                'AKS': 12340,
                'VPN Gateway': 8900
            }
            
            fig = px.bar(
                x=list(services_cost.values()),
                y=list(services_cost.keys()),
                orientation='h',
                color=list(services_cost.values()),
                color_continuous_scale=['#0078D4', '#50E6FF']
            )
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family='Segoe UI', color='#004E8C'),
                showlegend=False
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("#### 🌍 Cost by Location")
            
            location_cost = {
                'East US': 58900,
                'West US': 42300,
                'Central US': 28450,
                'West Europe': 13240
            }
            
            fig = go.Figure(data=[go.Pie(
                labels=list(location_cost.keys()),
                values=list(location_cost.values()),
                hole=0.4,
                marker=dict(colors=['#0078D4', '#50E6FF', '#004E8C', '#00BCF2'])
            )])
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family='Segoe UI', color='#004E8C')
            )
            st.plotly_chart(fig, use_container_width=True)
    
    @staticmethod
    def _render_cost_analysis():
        st.markdown("### 💰 Cost Analysis")
        
        # Filters
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            time_range = st.selectbox("Time Range", ["This Month", "Last Month", "Last 3 Months", "Last 6 Months", "Last Year"])
        with col2:
            group_by = st.selectbox("Group By", ["Service", "Resource Group", "Location", "Tag"])
        with col3:
            subscription_filter = st.selectbox("Subscription", ["All", "Production", "Development", "Staging"])
        with col4:
            granularity = st.selectbox("Granularity", ["Daily", "Monthly"])
        
        st.markdown("---")
        
        # Cost breakdown table
        st.markdown("#### 📋 Detailed Cost Breakdown")
        
        cost_data = [
            {"Resource Group": "Production-RG", "Service": "Virtual Machines", "Cost": "$28,450", "% of Total": "19.9%", "Trend": "↓ 5%"},
            {"Resource Group": "Production-RG", "Service": "SQL Database", "Cost": "$18,900", "% of Total": "13.2%", "Trend": "↑ 3%"},
            {"Resource Group": "Development-RG", "Service": "App Services", "Cost": "$12,340", "% of Total": "8.6%", "Trend": "→ 0%"},
            {"Resource Group": "Networking-RG", "Service": "VPN Gateway", "Cost": "$8,900", "% of Total": "6.2%", "Trend": "↓ 2%"}
        ]
        
        df = pd.DataFrame(cost_data)
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        # Download options
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("📥 Download CSV", use_container_width=True):
                st.success("✅ Cost data exported to CSV")
        with col2:
            if st.button("📧 Email Report", use_container_width=True):
                st.info("📧 Report will be emailed to your address")
    
    @staticmethod
    def _render_budgets():
        st.markdown("### 🎯 Budgets & Cost Alerts")
        
        AzureTheme.azure_info_box(
            "Cost Budgets",
            "Set budgets and receive alerts when costs exceed thresholds.",
            "🎯"
        )
        
        # Current budgets
        st.markdown("#### 📊 Active Budgets")
        
        budgets = [
            {"Budget": "Monthly Production", "Amount": "$150,000", "Current": "$142,890", "% Used": "95.3%", "Status": "⚠️ Warning"},
            {"Budget": "Monthly Development", "Amount": "$50,000", "Current": "$35,670", "% Used": "71.3%", "Status": "✅ On Track"},
            {"Budget": "Annual Total", "Amount": "$1,800,000", "Current": "$1,456,780", "% Used": "80.9%", "Status": "✅ On Track"}
        ]
        
        df = pd.DataFrame(budgets)
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        st.markdown("---")
        
        # Create budget
        with st.expander("➕ Create New Budget"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.text_input("Budget Name", placeholder="e.g., Q1 2024 Budget")
                st.number_input("Amount ($)", min_value=1000, max_value=10000000, value=100000, step=1000)
                st.selectbox("Period", ["Monthly", "Quarterly", "Annually"])
            
            with col2:
                st.selectbox("Scope", ["Subscription", "Resource Group", "Management Group"])
                st.multiselect("Alert Thresholds (%)", [50, 75, 90, 100], default=[80, 90, 100])
                st.text_input("Alert Email", placeholder="finance@company.com")
            
            if st.button("🎯 Create Budget", type="primary", use_container_width=True):
                st.success("✅ Budget created successfully!")
    
    @staticmethod
    def _render_optimization():
        st.markdown("### 💡 Cost Optimization Recommendations")
        
        # Savings summary
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Savings Identified", "$23,450/mo")
        with col2:
            st.metric("Quick Wins", "$8,900/mo")
        with col3:
            st.metric("Medium Effort", "$10,200/mo")
        with col4:
            st.metric("High Effort", "$4,350/mo")
        
        st.markdown("---")
        
        # Recommendations
        st.markdown("#### 💡 Top Recommendations")
        
        recommendations = [
            {
                "Recommendation": "Right-size underutilized VMs",
                "Impact": "$8,900/month",
                "Effort": "Low",
                "Resources": 23,
                "Priority": "🔴 High",
                "Action": "Resize"
            },
            {
                "Recommendation": "Purchase Reserved Instances",
                "Impact": "$7,200/month",
                "Effort": "Low",
                "Resources": 12,
                "Priority": "🔴 High",
                "Action": "Purchase"
            },
            {
                "Recommendation": "Delete unattached disks",
                "Impact": "$2,340/month",
                "Effort": "Low",
                "Resources": 45,
                "Priority": "🟠 Medium",
                "Action": "Delete"
            },
            {
                "Recommendation": "Use Azure Hybrid Benefit",
                "Impact": "$5,010/month",
                "Effort": "Medium",
                "Resources": 18,
                "Priority": "🟠 Medium",
                "Action": "Configure"
            }
        ]
        
        df = pd.DataFrame(recommendations)
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        if st.button("🔧 Apply Selected Recommendations", type="primary", use_container_width=True):
            st.success("✅ Optimization workflow initiated!")
    
    @staticmethod
    def _render_forecasting():
        st.markdown("### 📈 Cost Forecasting")
        
        st.info("AI-powered cost forecasting based on historical trends and planned changes")
        
        # Forecast parameters
        col1, col2 = st.columns(2)
        
        with col1:
            forecast_period = st.selectbox("Forecast Period", ["Next 30 Days", "Next 90 Days", "Next 6 Months", "Next Year"])
        with col2:
            confidence_level = st.slider("Confidence Level", 80, 99, 95)
        
        st.markdown("---")
        
        # Forecast chart
        st.markdown("#### 📊 Cost Forecast")
        
        # Generate forecast data
        historical_dates = pd.date_range(end=datetime.now(), periods=90, freq='D')
        forecast_dates = pd.date_range(start=datetime.now(), periods=90, freq='D')
        
        historical_costs = [4500 + (i * 10) + (i % 7 * 100) for i in range(90)]
        forecast_costs = [historical_costs[-1] + (i * 12) for i in range(90)]
        
        df = pd.DataFrame({
            'Date': list(historical_dates) + list(forecast_dates),
            'Cost': historical_costs + forecast_costs,
            'Type': ['Historical'] * 90 + ['Forecast'] * 90
        })
        
        fig = px.line(df, x='Date', y='Cost', color='Type')
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(family='Segoe UI', color='#004E8C')
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Forecast summary
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Forecasted Next Month", "$156,400")
        with col2:
            st.metric("vs Current Month", "+9.5%")
        with col3:
            st.metric("Confidence", f"{confidence_level}%")
    
    @staticmethod
    def _render_reports():
        st.markdown("### 📋 Cost Reports")
        
        # Report templates
        st.markdown("#### 📄 Report Templates")
        
        templates = [
            {"Name": "Executive Summary", "Frequency": "Monthly", "Recipients": "5", "Last Sent": "Dec 1, 2024"},
            {"Name": "Detailed Cost Analysis", "Frequency": "Weekly", "Recipients": "12", "Last Sent": "Dec 5, 2024"},
            {"Name": "Department Chargeback", "Frequency": "Monthly", "Recipients": "8", "Last Sent": "Dec 1, 2024"}
        ]
        
        df = pd.DataFrame(templates)
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        st.markdown("---")
        
        # Generate custom report
        st.markdown("#### 🔧 Generate Custom Report")
        
        col1, col2 = st.columns(2)
        
        with col1:
            report_type = st.selectbox("Report Type", ["Cost Summary", "Detailed Analysis", "Trend Analysis", "Chargeback"])
            time_period = st.selectbox("Time Period", ["This Month", "Last Month", "Last Quarter", "YTD"])
        
        with col2:
            format_type = st.selectbox("Format", ["PDF", "Excel", "PowerPoint"])
            include_charts = st.checkbox("Include Charts", value=True)
        
        if st.button("📊 Generate Report", type="primary", use_container_width=True):
            st.success("✅ Report generated successfully!")
            st.download_button("📥 Download Report", data="Sample report data", file_name="cost_report.pdf")
