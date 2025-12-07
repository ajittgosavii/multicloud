"""
AWS Theme - Professional Dark/Orange Theme
Optimized for readability and professional appearance
"""

import streamlit as st

class AWSTheme:
    """Professional AWS theme with optimized contrast"""
    
    # AWS Professional Color Palette
    AWS_ORANGE = "#FF9900"
    AWS_DARK = "#232F3E"
    AWS_LIGHT = "#FFFFFF"
    
    @staticmethod
    def apply_aws_theme():
        """Apply professional AWS theme"""
        
        st.markdown("""
        <style>
        /* Professional AWS Dark/Orange Theme */
        
        /* Headers - Dark background with white text */
        .main-header {
            background: linear-gradient(135deg, #232F3E 0%, #37475A 100%);
            padding: 25px;
            border-radius: 10px;
            border-left: 5px solid #FF9900;
            box-shadow: 0 2px 8px rgba(0,0,0,0.15);
        }
        
        /* Sidebar - AWS Dark */
        section[data-testid="stSidebar"] {
            background-color: #232F3E;
        }
        
        section[data-testid="stSidebar"] * {
            color: #FFFFFF !important;
        }
        
        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3 {
            color: #FF9900 !important;
        }
        
        /* Buttons - AWS Orange */
        .stButton > button {
            background-color: #FF9900;
            color: #FFFFFF;
            border: none;
            font-weight: 500;
        }
        
        .stButton > button:hover {
            background-color: #EC7211;
        }
        
        /* Info boxes */
        div[data-testid="stSuccess"] {
            background-color: #F0F8F0;
            border-left: 4px solid #FF9900;
        }
        
        </style>
        """, unsafe_allow_html=True)
    
    @staticmethod
    def aws_header(title: str, subtitle: str = ""):
        """Create professional AWS header - Dark background"""
        subtitle_html = f'<p style="color: #FFB84D; margin: 5px 0 0 0; font-size: 1.1em;">{subtitle}</p>' if subtitle else ""
        
        return f"""
        <div style="
            background: linear-gradient(135deg, #232F3E 0%, #37475A 100%);
            padding: 30px;
            border-radius: 10px;
            border-left: 5px solid #FF9900;
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
    def aws_metric_card(label: str, value: str, icon: str = None, delta: str = None):
        """AWS metric card - renders directly"""
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
            border-left: 4px solid #FF9900;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        ">
            {icon_html}
            <div style="color: #FF9900; font-size: 0.85em; text-transform: uppercase; font-weight: 600;">{label}</div>
            <div style="color: #232F3E; font-size: 2em; font-weight: 600; margin-top: 5px;">{value}</div>
            {delta_html}
        </div>
        """
        st.markdown(html, unsafe_allow_html=True)
    
    @staticmethod
    def aws_info_box(content: str, icon: str = "🔶"):
        """AWS info box - renders directly"""
        html = f"""
        <div style="
            background-color: #FFF8E7;
            border-left: 4px solid #FF9900;
            padding: 15px 20px;
            border-radius: 5px;
            color: #232F3E;
        ">
            <span style="font-size: 1.2em; margin-right: 10px;">{icon}</span>
            {content}
        </div>
        """
        st.markdown(html, unsafe_allow_html=True)
