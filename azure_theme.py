"""
Azure Theme - Professional Dark Blue Theme
Optimized for readability and professional appearance
"""

import streamlit as st

class AzureTheme:
    """Professional Azure theme with optimized contrast"""
    
    # Azure Professional Color Palette
    AZURE_BLUE = "#0078D4"
    AZURE_DARK = "#003366"
    AZURE_LIGHT = "#FFFFFF"
    
    @staticmethod
    def apply_azure_theme():
        """Apply professional Azure theme"""
        
        st.markdown("""
        <style>
        /* Professional Azure Dark Blue Theme */
        
        /* Headers - Dark blue background with white text */
        .main-header {
            background: linear-gradient(135deg, #003366 0%, #005A9E 100%);
            padding: 25px;
            border-radius: 10px;
            border-left: 5px solid #0078D4;
            box-shadow: 0 2px 8px rgba(0,0,0,0.15);
        }
        
        /* Sidebar - Azure Dark */
        section[data-testid="stSidebar"] {
            background-color: #003366;
        }
        
        section[data-testid="stSidebar"] * {
            color: #FFFFFF !important;
        }
        
        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3 {
            color: #50E6FF !important;
        }
        
        /* Buttons - Azure Blue */
        .stButton > button {
            background-color: #0078D4;
            color: #FFFFFF;
            border: none;
            font-weight: 500;
        }
        
        .stButton > button:hover {
            background-color: #005A9E;
        }
        
        /* Info boxes */
        div[data-testid="stInfo"] {
            background-color: #E7F3FF;
            border-left: 4px solid #0078D4;
        }
        
        </style>
        """, unsafe_allow_html=True)
    
    @staticmethod
    def azure_header(title: str, subtitle: str = ""):
        """Create professional Azure header - Dark blue background"""
        subtitle_html = f'<p style="color: #50E6FF; margin: 5px 0 0 0; font-size: 1.1em;">{subtitle}</p>' if subtitle else ""
        
        return f"""
        <div style="
            background: linear-gradient(135deg, #003366 0%, #005A9E 100%);
            padding: 30px;
            border-radius: 10px;
            border-left: 5px solid #0078D4;
            margin-bottom: 20px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        ">
            <h1 style="color: #FFFFFF; margin: 0; font-weight: 600;">
                ☁️ {title}
            </h1>
            {subtitle_html}
        </div>
        """
    
    @staticmethod
    def azure_metric_card(label: str, value: str, icon: str = None, delta: str = None):
        """Azure metric card - renders directly"""
        delta_html = ""
        if delta:
            delta_color = "#00AA00" if "+" in delta or "↑" in delta else "#DD0000"
            delta_html = f'<div style="color: {delta_color}; font-size: 0.9em; margin-top: 5px;">{delta}</div>'
        
        icon_html = f'<div style="color: #666; font-size: 1.5em; margin-bottom: 5px;">{icon}</div>' if icon else ""
        
        html = f"""
        <div style="
            background-color: #FFFFFF;
            padding: 20px;
            border-radius: 8px;
            border-left: 4px solid #0078D4;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        ">
            {icon_html}
            <div style="color: #0078D4; font-size: 0.85em; text-transform: uppercase; font-weight: 600;">{label}</div>
            <div style="color: #003366; font-size: 2em; font-weight: 600; margin-top: 5px;">{value}</div>
            {delta_html}
        </div>
        """
        st.markdown(html, unsafe_allow_html=True)
    
    @staticmethod
    def azure_info_box(content: str, icon: str = "🔷"):
        """Azure info box - renders directly"""
        html = f"""
        <div style="
            background-color: #E7F3FF;
            border-left: 4px solid #0078D4;
            padding: 15px 20px;
            border-radius: 5px;
            color: #003366;
        ">
            <span style="font-size: 1.2em; margin-right: 10px;">{icon}</span>
            {content}
        </div>
        """
        st.markdown(html, unsafe_allow_html=True)
