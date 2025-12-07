"""
Azure Theme - Microsoft Azure Styling
Professional Azure-branded theme with Microsoft Azure color palette
"""

import streamlit as st

class AzureTheme:
    """Azure theme with Microsoft Azure colors and styling"""
    
    # Azure Color Palette
    AZURE_BLUE = "#0078D4"  # Primary Azure Blue
    AZURE_DARK_BLUE = "#004E8C"  # Dark Blue
    AZURE_LIGHT_BLUE = "#50E6FF"  # Light Blue
    AZURE_PURPLE = "#5E5E5E"  # Azure Purple accent
    AZURE_GREEN = "#107C10"  # Success green
    AZURE_ORANGE = "#D83B01"  # Warning orange
    AZURE_RED = "#C50F1F"  # Error red
    AZURE_GRAY = "#F3F2F1"  # Background gray
    
    @staticmethod
    def apply_azure_theme():
        """Apply Azure-themed CSS styling"""
        
        st.markdown("""
        <style>
        /* Azure Global Styles */
        .stApp {
            background: linear-gradient(135deg, #FFFFFF 0%, #E8F4F8 100%);
        }
        
        /* Azure Headers */
        h1, h2, h3 {
            color: #0078D4 !important;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
            font-weight: 600 !important;
        }
        
        /* Azure Buttons */
        .stButton > button {
            background: linear-gradient(135deg, #0078D4 0%, #004E8C 100%) !important;
            color: white !important;
            border: none !important;
            border-radius: 4px !important;
            padding: 12px 24px !important;
            font-weight: 600 !important;
            font-family: 'Segoe UI', sans-serif !important;
            box-shadow: 0 2px 4px rgba(0, 120, 212, 0.3) !important;
            transition: all 0.3s ease !important;
        }
        
        .stButton > button:hover {
            background: linear-gradient(135deg, #004E8C 0%, #0078D4 100%) !important;
            box-shadow: 0 4px 8px rgba(0, 120, 212, 0.4) !important;
            transform: translateY(-2px) !important;
        }
        
        /* Azure Primary Button */
        .stButton > button[kind="primary"] {
            background: linear-gradient(135deg, #0078D4 0%, #50E6FF 100%) !important;
            box-shadow: 0 4px 8px rgba(0, 120, 212, 0.5) !important;
        }
        
        /* Azure Secondary Button */
        .stButton > button[kind="secondary"] {
            background: linear-gradient(135deg, #F3F2F1 0%, #E1DFDD 100%) !important;
            color: #0078D4 !important;
            border: 2px solid #0078D4 !important;
        }
        
        /* Azure Metrics */
        [data-testid="stMetricValue"] {
            color: #0078D4 !important;
            font-size: 2.5rem !important;
            font-weight: 700 !important;
        }
        
        [data-testid="stMetricLabel"] {
            color: #004E8C !important;
            font-weight: 600 !important;
            font-size: 1rem !important;
        }
        
        /* Azure Sidebar */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0078D4 0%, #004E8C 100%) !important;
        }
        
        [data-testid="stSidebar"] * {
            color: white !important;
        }
        
        [data-testid="stSidebar"] .stSelectbox label,
        [data-testid="stSidebar"] .stRadio label {
            color: white !important;
            font-weight: 600 !important;
        }
        
        /* Azure Info/Success/Warning/Error Boxes */
        .stAlert {
            border-radius: 8px !important;
            border-left: 4px solid #0078D4 !important;
            background: #E8F4F8 !important;
        }
        
        .stSuccess {
            border-left-color: #107C10 !important;
            background: #DFF6DD !important;
        }
        
        .stWarning {
            border-left-color: #D83B01 !important;
            background: #FFF4CE !important;
        }
        
        .stError {
            border-left-color: #C50F1F !important;
            background: #FDE7E9 !important;
        }
        
        /* Azure Tables */
        .stDataFrame {
            border: 2px solid #0078D4 !important;
            border-radius: 8px !important;
        }
        
        /* Azure Tabs */
        .stTabs [data-baseweb="tab-list"] {
            background: linear-gradient(135deg, #F3F2F1 0%, #E1DFDD 100%) !important;
            border-radius: 8px !important;
            padding: 8px !important;
        }
        
        .stTabs [data-baseweb="tab"] {
            color: #004E8C !important;
            font-weight: 600 !important;
            border-radius: 6px !important;
        }
        
        .stTabs [aria-selected="true"] {
            background: #0078D4 !important;
            color: white !important;
        }
        
        /* Azure Expander */
        .streamlit-expanderHeader {
            background: linear-gradient(135deg, #E8F4F8 0%, #D6EAF8 100%) !important;
            color: #0078D4 !important;
            border: 2px solid #0078D4 !important;
            border-radius: 8px !important;
            font-weight: 600 !important;
        }
        
        /* Azure Input Fields */
        .stTextInput > div > div > input,
        .stSelectbox > div > div > select,
        .stTextArea > div > div > textarea {
            border: 2px solid #0078D4 !important;
            border-radius: 4px !important;
            background: white !important;
        }
        
        .stTextInput > div > div > input:focus,
        .stSelectbox > div > div > select:focus,
        .stTextArea > div > div > textarea:focus {
            border-color: #50E6FF !important;
            box-shadow: 0 0 0 2px rgba(0, 120, 212, 0.2) !important;
        }
        
        /* Azure Cards */
        div.element-container {
            border-radius: 8px;
        }
        
        /* Azure Progress Bar */
        .stProgress > div > div > div {
            background: linear-gradient(90deg, #0078D4 0%, #50E6FF 100%) !important;
        }
        
        /* Azure Scrollbar */
        ::-webkit-scrollbar {
            width: 12px;
            height: 12px;
        }
        
        ::-webkit-scrollbar-track {
            background: #F3F2F1;
            border-radius: 10px;
        }
        
        ::-webkit-scrollbar-thumb {
            background: linear-gradient(135deg, #0078D4 0%, #004E8C 100%);
            border-radius: 10px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: #0078D4;
        }
        </style>
        """, unsafe_allow_html=True)
    
    @staticmethod
    def azure_header(title: str, subtitle: str = ""):
        """Render Azure-styled header"""
        
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #0078D4 0%, #004E8C 100%);
            padding: 30px;
            border-radius: 12px;
            margin-bottom: 30px;
            box-shadow: 0 4px 6px rgba(0, 120, 212, 0.3);
        ">
            <h1 style="
                color: white !important;
                margin: 0;
                font-size: 2.5rem;
                font-weight: 700;
                font-family: 'Segoe UI', sans-serif !important;
            ">
                {title}
            </h1>
            {f'<p style="color: #50E6FF; margin: 10px 0 0 0; font-size: 1.1rem; font-weight: 500;">{subtitle}</p>' if subtitle else ''}
        </div>
        """, unsafe_allow_html=True)
    
    @staticmethod
    def azure_metric_card(label: str, value: str, icon: str = "", delta: str = None):
        """Render Azure-styled metric card"""
        
        delta_html = ""
        if delta:
            delta_color = "#107C10" if delta.startswith("+") else "#C50F1F"
            delta_html = f"""
            <div style="
                color: {delta_color};
                font-size: 14px;
                font-weight: 600;
                margin-top: 8px;
            ">
                {delta}
            </div>
            """
        
        return st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #FFFFFF 0%, #E8F4F8 100%);
            border: 3px solid #0078D4;
            border-radius: 12px;
            padding: 24px;
            box-shadow: 0 4px 8px rgba(0, 120, 212, 0.2);
            min-height: 150px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        ">
            <div style="
                color: #0078D4;
                font-size: 14px;
                font-weight: 700;
                text-transform: uppercase;
                letter-spacing: 1.5px;
                margin-bottom: 14px;
                font-family: 'Segoe UI', sans-serif;
            ">
                <span style="font-size: 24px; margin-right: 10px;">{icon}</span>
                {label}
            </div>
            <div style="
                color: #004E8C;
                font-size: 48px;
                font-weight: 800;
                line-height: 1;
                font-family: 'Segoe UI', sans-serif;
            ">
                {value}
            </div>
            {delta_html}
        </div>
        """, unsafe_allow_html=True)
    
    @staticmethod
    def azure_info_box(title: str, content: str, icon: str = "ℹ️"):
        """Render Azure-styled info box"""
        
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #E8F4F8 0%, #D6EAF8 100%);
            border-left: 5px solid #0078D4;
            border-radius: 8px;
            padding: 20px;
            margin: 20px 0;
        ">
            <div style="
                color: #004E8C;
                font-size: 18px;
                font-weight: 700;
                margin-bottom: 10px;
                font-family: 'Segoe UI', sans-serif;
            ">
                <span style="font-size: 24px; margin-right: 10px;">{icon}</span>
                {title}
            </div>
            <div style="
                color: #323130;
                font-size: 14px;
                line-height: 1.6;
                font-family: 'Segoe UI', sans-serif;
            ">
                {content}
            </div>
        </div>
        """, unsafe_allow_html=True)
