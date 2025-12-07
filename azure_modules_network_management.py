"""
Azure Module: Network Management
Manage Virtual Networks, NSGs, Load Balancers, and networking resources
"""

import streamlit as st
import pandas as pd
from azure_theme import AzureTheme
from config_settings import AppConfig

class AzureNetworkManagementUI:
    """Azure Network Management module"""
    
    @staticmethod
    def render():
        st.markdown("## 🌐 Azure Network Management")
        st.caption("Manage Virtual Networks, Subnets, NSGs, and Load Balancers")
        
        subscriptions = AppConfig.load_azure_subscriptions()
        active_subscriptions = [sub for sub in subscriptions if sub.status == 'active']
        
        tabs = st.tabs([
            "📊 Overview",
            "🌐 Virtual Networks",
            "🔒 Network Security Groups",
            "⚖️ Load Balancers",
            "🚪 Application Gateways",
            "🔗 VPN & ExpressRoute"
        ])
        
        with tabs[0]:
            AzureNetworkManagementUI._render_overview()
        
        with tabs[1]:
            AzureNetworkManagementUI._render_virtual_networks()
        
        with tabs[2]:
            AzureNetworkManagementUI._render_nsgs()
        
        with tabs[3]:
            AzureNetworkManagementUI._render_load_balancers()
        
        with tabs[4]:
            AzureNetworkManagementUI._render_app_gateways()
        
        with tabs[5]:
            AzureNetworkManagementUI._render_vpn_express_route()
    
    @staticmethod
    def _render_overview():
        st.markdown("### 📊 Network Overview")
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            AzureTheme.azure_metric_card("Virtual Networks", "45", "🌐")
        with col2:
            AzureTheme.azure_metric_card("Subnets", "234", "📡")
        with col3:
            AzureTheme.azure_metric_card("NSGs", "67", "🔒")
        with col4:
            AzureTheme.azure_metric_card("Load Balancers", "23", "⚖️")
        
        st.markdown("---")
        
        vnets_data = [
            {"Name": "prod-vnet-east", "Address Space": "10.0.0.0/16", "Subnets": 8, "Peerings": 3, "Location": "East US"},
            {"Name": "dev-vnet-west", "Address Space": "10.1.0.0/16", "Subnets": 5, "Peerings": 1, "Location": "West US"},
            {"Name": "hub-vnet-central", "Address Space": "10.10.0.0/16", "Subnets": 12, "Peerings": 5, "Location": "Central US"}
        ]
        
        df = pd.DataFrame(vnets_data)
        st.dataframe(df, use_container_width=True, hide_index=True)
    
    @staticmethod
    def _render_virtual_networks():
        st.markdown("### 🌐 Virtual Networks")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.text_input("VNet Name", placeholder="e.g., prod-vnet-01")
            st.text_input("Address Space (CIDR)", placeholder="e.g., 10.0.0.0/16")
        
        with col2:
            st.selectbox("Location", ["East US", "West US", "Central US"])
            st.selectbox("Resource Group", ["Production-RG", "Network-RG"])
        
        if st.button("🌐 Create Virtual Network", type="primary", use_container_width=True):
            st.success("✅ Virtual Network created successfully!")
    
    @staticmethod
    def _render_nsgs():
        st.markdown("### 🔒 Network Security Groups")
        
        AzureTheme.azure_info_box(
            "Network Security",
            "NSGs filter network traffic to and from Azure resources in Azure Virtual Networks.",
            "🔒"
        )
        
        nsg_rules = [
            {"Priority": 100, "Name": "AllowHTTPS", "Direction": "Inbound", "Action": "Allow", "Protocol": "TCP", "Port": 443, "Source": "Internet"},
            {"Priority": 110, "Name": "AllowHTTP", "Direction": "Inbound", "Action": "Allow", "Protocol": "TCP", "Port": 80, "Source": "Internet"},
            {"Priority": 200, "Name": "DenyAll", "Direction": "Inbound", "Action": "Deny", "Protocol": "*", "Port": "*", "Source": "*"}
        ]
        
        df = pd.DataFrame(nsg_rules)
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        if st.button("➕ Add Security Rule", use_container_width=True):
            st.info("Opening security rule editor...")
    
    @staticmethod
    def _render_load_balancers():
        st.markdown("### ⚖️ Load Balancers")
        
        lb_data = [
            {"Name": "prod-lb-web", "Type": "Public", "SKU": "Standard", "Backend Pool": "web-servers", "Health Probes": 2},
            {"Name": "prod-lb-internal", "Type": "Internal", "SKU": "Standard", "Backend Pool": "app-servers", "Health Probes": 1}
        ]
        
        df = pd.DataFrame(lb_data)
        st.dataframe(df, use_container_width=True, hide_index=True)
    
    @staticmethod
    def _render_app_gateways():
        st.markdown("### 🚪 Application Gateways")
        
        st.info("Application Gateway provides application-level routing and load balancing services.")
        
        gw_data = [
            {"Name": "prod-appgw-01", "SKU": "WAF_v2", "Capacity": "2 instances", "Frontend": "Public IP", "Backend Pools": 3}
        ]
        
        df = pd.DataFrame(gw_data)
        st.dataframe(df, use_container_width=True, hide_index=True)
    
    @staticmethod
    def _render_vpn_express_route():
        st.markdown("### 🔗 VPN & ExpressRoute")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 🔐 VPN Gateways")
            st.metric("Active VPN Connections", "3")
            st.metric("VPN Bandwidth", "100 Mbps")
        
        with col2:
            st.markdown("#### ⚡ ExpressRoute")
            st.metric("ExpressRoute Circuits", "1")
            st.metric("Circuit Bandwidth", "1 Gbps")
