import streamlit as st
import sys
import os
import pandas as pd
import numpy as np
from datetime import datetime

# Add the parent directory to the path to import utils
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.supabase import is_authenticated, get_current_user
from utils.quotes import get_random_quote
from utils.financial_data import get_all_assets, get_market_trends

st.set_page_config(
    page_title="Skyra AI Powered Investor - Home",
    page_icon="",
    layout="wide"
)

# Minimalist color scheme
theme_colors = {
    'primary': '#2563EB',  # Blue
    'secondary': '#10B981',  # Green
    'accent': '#F59E0B',  # Amber
    'text': '#1F2937',  # Dark gray
    'text_secondary': '#6B7280',  # Medium gray
    'border': '#E5E7EB',  # Light gray
    'background': '#FFFFFF'  # White
}

# Add Font Awesome for icons
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">', unsafe_allow_html=True)

# Minimalist CSS
st.markdown(f"""
<style>
    /* Global styles */
    body {{
        background-color: {theme_colors['background']} !important;
    }}
    
    .main .block-container {{
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }}

    /* Typography */
    h1, h2, h3, h4, h5, h6 {{
        font-family: 'Inter', Arial, sans-serif;
        font-weight: 600;
        color: {theme_colors['text']};
    }}

    p, div, span, li {{
        font-family: 'Inter', Arial, sans-serif;
        color: {theme_colors['text_secondary']};
    }}

    /* Cards */
    .card {{
        background-color: {theme_colors['background']};
        border-radius: 8px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        border: 1px solid {theme_colors['border']};
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
    }}

    .metric-card {{
        display: flex;
        align-items: center;
        padding: 1.25rem;
    }}

    .metric-icon {{
        font-size: 1.5rem;
        margin-right: 1rem;
        color: {theme_colors['primary']};
        width: 48px;
        height: 48px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 8px;
        background-color: rgba(37, 99, 235, 0.1);
    }}

    /* Buttons */
    .btn {{
        background-color: {theme_colors['primary']};
        color: white;
        border: none;
        padding: 0.75rem 1.5rem;
        border-radius: 6px;
        font-weight: 500;
        cursor: pointer;
        transition: all 0.2s;
        text-align: center;
        display: inline-flex;
        align-items: center;
        justify-content: center;
    }}

    .btn:hover {{
        background-color: #1D4ED8;
        transform: translateY(-1px);
    }}

    .btn-outline {{
        background-color: transparent;
        border: 1px solid {theme_colors['primary']};
        color: {theme_colors['primary']};
    }}

    .btn-outline:hover {{
        background-color: rgba(37, 99, 235, 0.05);
    }}

    /* Navigation */
    .nav-link {{
        color: {theme_colors['text_secondary']};
        text-decoration: none;
        margin-right: 1.5rem;
        font-weight: 500;
        transition: color 0.2s;
    }}

    .nav-link:hover {{
        color: {theme_colors['primary']};
    }}

    /* Dividers */
    .divider {{
        height: 1px;
        background-color: {theme_colors['border']};
        margin: 2rem 0;
        border: none;
    }}

    /* Badges */
    .badge {{
        display: inline-block;
        padding: 0.25rem 0.5rem;
        border-radius: 4px;
        font-size: 0.75rem;
        font-weight: 500;
    }}

    .badge-primary {{
        background-color: rgba(37, 99, 235, 0.1);
        color: {theme_colors['primary']};
    }}

    /* Utility classes */
    .flex {{
        display: flex;
    }}

    .items-center {{
        align-items: center;
    }}

    .justify-between {{
        justify-content: space-between;
    }}
</style>
""", unsafe_allow_html=True)

# Header section
st.markdown("""
<div class="flex justify-between" style="margin-bottom: 2rem;">
    <div class="flex items-center">
        <span style="font-size: 1.8rem; margin-right: 10px;"></span>
        <h1 style="margin: 0;">Skyra AI Powered Investor</h1>
    </div>
    <div class="flex items-center">
        <a href="/" class="nav-link"><i class="fas fa-home"></i> Home</a>
        <a href="/ESG_Education" class="nav-link"><i class="fas fa-graduation-cap"></i> ESG Education</a>
        <a href="/Market_Explorer" class="nav-link"><i class="fas fa-chart-line"></i> Markets</a>
        <a href="/Portfolio_Manager" class="nav-link"><i class="fas fa-briefcase"></i> Portfolio</a>
        <a href="/AI_Recommendations" class="nav-link"><i class="fas fa-robot"></i> AI Advisor</a>
""", unsafe_allow_html=True)

# Authentication section
if not is_authenticated():
    st.markdown("""
        <a href="/Authentication" target="_self" style="text-decoration: none;">
            <button class="btn">
                <i class="fas fa-user" style="margin-right: 8px;"></i> Sign In
            </button>
        </a>
    </div>
</div>

<div class="card" style="margin-bottom: 3rem;">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div style="max-width: 60%;">
            <h2 style="margin: 0; margin-bottom: 1rem;">Sustainable investing for a better future</h2>
            <p style="margin-bottom: 1.5rem;">Our AI-powered platform helps you build profitable portfolios while making a positive impact on the planet.</p>
            <div style="display: flex; gap: 1rem; margin-top: 1rem; flex-wrap: wrap;">
                <div class="flex items-center">
                    <i class="fas fa-check-circle" style="color: #10B981; margin-right: 8px;"></i>
                    <span>ESG-focused investments</span>
                </div>
                <div class="flex items-center">
                    <i class="fas fa-check-circle" style="color: #2563EB; margin-right: 8px;"></i>
                    <span>AI-powered recommendations</span>
                </div>
                <div class="flex items-center">
                    <i class="fas fa-check-circle" style="color: #F59E0B; margin-right: 8px;"></i>
                    <span>Real-time analytics</span>
                </div>
            </div>
        </div>
        <div>
            <a href="/Authentication" target="_self" style="text-decoration: none;">
                <button class="btn">
                    <i class="fas fa-rocket" style="margin-right: 10px;"></i> Get Started
                </button>
            </a>
        </div>
    </div>
</div>
    """, unsafe_allow_html=True)
else:
    user = get_current_user()
    st.markdown(f"""
        <div class="flex items-center">
            <span style="margin-right: 1rem;">Welcome, {user['full_name']}</span>
            <a href="/User_Profile" style="text-decoration: none;">
                <button class="btn-outline">
                    <i class="fas fa-user-circle" style="margin-right: 6px;"></i> Profile
                </button>
            </a>
        </div>
    </div>
</div>

<div class="card" style="margin-bottom: 2rem;">
    <div class="flex items-center">
        <div class="metric-icon">
            <i class="fas fa-chart-line"></i>
        </div>
        <div>
            <h2 style="margin: 0; margin-bottom: 0.25rem;">Welcome back, {user['full_name'].split()[0]}</h2>
            <p style="margin: 0; color: {theme_colors['text_secondary']};">Your sustainable investment dashboard</p>
        </div>
    </div>
</div>
    """, unsafe_allow_html=True)

    # Metrics row
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div class="card metric-card">
            <div class="metric-icon">
                <i class="fas fa-leaf"></i>
            </div>
            <div>
                <p style="margin: 0; font-size: 0.875rem; color: {theme_colors['text_secondary']};">ESG Impact</p>
                <p style="margin: 0; font-size: 1.25rem; font-weight: 600;">High</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="card metric-card">
            <div class="metric-icon" style="color: {theme_colors['secondary']}; background-color: rgba(16, 185, 129, 0.1);">
                <i class="fas fa-chart-pie"></i>
            </div>
            <div>
                <p style="margin: 0; font-size: 0.875rem; color: {theme_colors['text_secondary']};">Portfolio Value</p>
                <p style="margin: 0; font-size: 1.25rem; font-weight: 600;">$24,680</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="card metric-card">
            <div class="metric-icon" style="color: {theme_colors['accent']}; background-color: rgba(245, 158, 11, 0.1);">
                <i class="fas fa-trend-up"></i>
            </div>
            <div>
                <p style="margin: 0; font-size: 0.875rem; color: {theme_colors['text_secondary']};">Performance</p>
                <p style="margin: 0; font-size: 1.25rem; font-weight: 600; color: #10B981;">+12.4%</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Quote section
quote = get_random_quote()
st.markdown(f"""
<div class="card" style="margin: 2rem 0; padding-left: 1.5rem; border-left: 3px solid {theme_colors['primary']};">
    <p style="font-style: italic; margin-bottom: 0.5rem;">"{quote['quote']}"</p>
    <p style="font-weight: 500; color: {theme_colors['text_secondary']};">— {quote['author']}</p>
</div>
""", unsafe_allow_html=True)

# Features section
st.markdown("### Key Features")
st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

feat_col1, feat_col2, feat_col3 = st.columns(3)

with feat_col1:
    st.markdown(f"""
    <div class="card" style="height: 100%;">
        <h3 style="margin-top: 0; display: flex; align-items: center;">
            <i class="fas fa-chart-bar" style="color: {theme_colors['primary']}; margin-right: 10px;"></i>
            Market Analytics
        </h3>
        <p style="margin-bottom: 1.5rem;">Comprehensive ESG ratings and financial metrics for all assets.</p>
        <a href="/Market_Explorer" target="_self" style="text-decoration: none;">
            <button class="btn" style="width: 100%;">
                Explore <i class="fas fa-arrow-right" style="margin-left: 8px;"></i>
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

with feat_col2:
    st.markdown(f"""
    <div class="card" style="height: 100%;">
        <h3 style="margin-top: 0; display: flex; align-items: center;">
            <i class="fas fa-briefcase" style="color: {theme_colors['secondary']}; margin-right: 10px;"></i>
            Portfolio Manager
        </h3>
        <p style="margin-bottom: 1.5rem;">Build and track portfolios aligned with your values.</p>
        <a href="/Portfolio_Manager" target="_self" style="text-decoration: none;">
            <button class="btn" style="width: 100%; background-color: {theme_colors['secondary']};">
                Manage <i class="fas fa-arrow-right" style="margin-left: 8px;"></i>
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

with feat_col3:
    st.markdown(f"""
    <div class="card" style="height: 100%;">
        <h3 style="margin-top: 0; display: flex; align-items: center;">
            <i class="fas fa-robot" style="color: {theme_colors['accent']}; margin-right: 10px;"></i>
            AI Advisor
        </h3>
        <p style="margin-bottom: 1.5rem;">Personalized recommendations based on your profile.</p>
        <a href="/AI_Recommendations" target="_self" style="text-decoration: none;">
            <button class="btn" style="width: 100%; background-color: {theme_colors['accent']};">
                Get Advice <i class="fas fa-arrow-right" style="margin-left: 8px;"></i>
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

# Market trends section
st.markdown("### Market Trends")
st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

market_trends = get_market_trends()
trend_col1, trend_col2, trend_col3 = st.columns(3)

for i, trend in enumerate(market_trends[:3]):
    with [trend_col1, trend_col2, trend_col3][i]:
        impact_color = "#10B981" if "positive" in trend['impact'].lower() else "#EF4444" if "negative" in trend['impact'].lower() else "#F59E0B"
        st.markdown(f"""
        <div class="card">
            <div class="flex justify-between items-center" style="margin-bottom: 0.8rem;">
                <h4 style="margin: 0; font-size: 1.1rem;">{trend['title']}</h4>
                <span class="badge badge-primary">Confidence: {trend['confidence']}%</span>
            </div>
            <p style="margin-bottom: 1rem;">{trend['description']}</p>
            <div class="flex items-center">
                <span style="font-weight: 600; margin-right: 0.5rem;">Impact:</span>
                <span style="color: {impact_color};">{trend['impact']}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Top assets section
st.markdown("### Top Performing Assets")
st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

all_assets = get_all_assets()
top_assets = sorted(all_assets, key=lambda x: x['roi_1y'], reverse=True)[:8]

asset_row1 = st.columns(4)
asset_row2 = st.columns(4)
asset_cols = asset_row1 + asset_row2

for i, asset in enumerate(top_assets):
    with asset_cols[i]:
        price_change = asset['price_change_24h']
        price_color = "#10B981" if price_change > 0 else "#EF4444"
        st.markdown(f"""
        <div class="card">
            <div class="flex justify-between items-center" style="margin-bottom: 0.5rem;">
                <h4 style="margin: 0; font-size: 1rem;">{asset['symbol']}</h4>
                <span style="font-size: 0.8rem; color: {theme_colors['text_secondary']};">{asset['asset_type']}</span>
            </div>
            <p style="margin: 0; font-weight: 500; margin-bottom: 0.5rem;">{asset['name']}</p>
            <div class="flex justify-between" style="margin-bottom: 0.5rem;">
                <span>Price:</span>
                <span>${asset['current_price']:.2f}</span>
            </div>
            <div class="flex justify-between" style="margin-bottom: 0.5rem;">
                <span>24h:</span>
                <span style="color:{price_color};">{price_change:.2f}%</span>
            </div>
            <div class="flex justify-between">
                <span>ESG Score:</span>
                <span>{asset['esg_score']:.1f}/100</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
st.markdown(f"""
<div class="flex justify-between" style="margin-top: 2rem;">
    <div>
        <p style="font-size: 0.875rem; color: {theme_colors['text_secondary']};">© 2025 Skyra AI Powered Investor</p>
    </div>
    <div>
        <a href="#" style="text-decoration: none; margin-left: 1rem; color: {theme_colors['text_secondary']};">Terms</a>
        <a href="#" style="text-decoration: none; margin-left: 1rem; color: {theme_colors['text_secondary']};">Privacy</a>
        <a href="#" style="text-decoration: none; margin-left: 1rem; color: {theme_colors['text_secondary']};">Contact</a>
    </div>
</div>
""", unsafe_allow_html=True)