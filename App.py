import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import time
import random

# Enhanced Matrix AI Call Center theme
def apply_matrix_theme():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Share+Tech+Mono:wght@400&display=swap');
    
    /* Matrix AI Call Center Variables */
    :root {
        --matrix-green: #00ff41;
        --matrix-bright-green: #39ff14;
        --matrix-dark-green: #008f11;
        --matrix-neon-blue: #00ffff;
        --matrix-purple: #9d4edd;
        --matrix-black: #000000;
        --matrix-dark: #0a0a0a;
        --matrix-darker: #050505;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {visibility: hidden;}
    
    /* Main app styling */
    .stApp {
        background: linear-gradient(135deg, #000000 0%, #0a0a0a 30%, #1a0a1a 60%, #050505 100%);
        color: var(--matrix-green);
        font-family: 'Orbitron', 'Share Tech Mono', monospace;
        overflow-x: hidden;
    }
    
    /* Animated background grid */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            linear-gradient(rgba(0,255,65,0.03) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0,255,65,0.03) 1px, transparent 1px);
        background-size: 50px 50px;
        animation: grid-move 20s linear infinite;
        z-index: -2;
    }
    
    @keyframes grid-move {
        0% { transform: translate(0, 0); }
        100% { transform: translate(50px, 50px); }
    }
    
    /* Matrix rain enhanced */
    .matrix-bg {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100vh;
        z-index: -1;
        overflow: hidden;
        background: transparent;
        pointer-events: none;
    }
    
    .matrix-rain {
        position: absolute;
        color: var(--matrix-green);
        font-family: 'Share Tech Mono', monospace;
        font-size: 12px;
        line-height: 14px;
        text-shadow: 0 0 10px var(--matrix-green);
        white-space: nowrap;
        opacity: 0;
        animation: rain linear infinite;
    }
    
    .matrix-rain:nth-child(odd) {
        color: var(--matrix-neon-blue);
        text-shadow: 0 0 10px var(--matrix-neon-blue);
    }
    
    @keyframes rain {
        0% {
            opacity: 0;
            transform: translateY(-100px);
        }
        5% {
            opacity: 1;
        }
        95% {
            opacity: 1;
        }
        100% {
            opacity: 0;
            transform: translateY(calc(100vh + 100px));
        }
    }
    
    /* Hero section styling */
    .hero-section {
        background: linear-gradient(135deg, rgba(0,0,0,0.95) 0%, rgba(26,10,26,0.9) 50%, rgba(0,0,0,0.95) 100%);
        border: 3px solid var(--matrix-green);
        border-radius: 20px;
        padding: 50px 30px;
        margin: 30px 0;
        text-align: center;
        position: relative;
        overflow: hidden;
        box-shadow: 
            0 0 50px rgba(0,255,65,0.4),
            inset 0 0 50px rgba(0,255,65,0.1),
            0 0 100px rgba(157,78,221,0.2);
        animation: hero-pulse 4s ease-in-out infinite alternate;
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent 30%, rgba(0,255,65,0.1) 50%, transparent 70%);
        animation: hero-sweep 8s linear infinite;
        pointer-events: none;
    }
    
    @keyframes hero-pulse {
        0% { 
            box-shadow: 0 0 50px rgba(0,255,65,0.4), inset 0 0 50px rgba(0,255,65,0.1), 0 0 100px rgba(157,78,221,0.2);
        }
        100% { 
            box-shadow: 0 0 80px rgba(0,255,65,0.6), inset 0 0 80px rgba(0,255,65,0.2), 0 0 150px rgba(157,78,221,0.4);
        }
    }
    
    @keyframes hero-sweep {
        0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
        100% { transform: translateX(100%) translateY(100%) rotate(45deg); }
    }
    
    /* Enhanced headers */
    .hero-title {
        font-family: 'Orbitron', monospace !important;
        font-size: 4rem !important;
        font-weight: 900 !important;
        background: linear-gradient(45deg, var(--matrix-bright-green), var(--matrix-neon-blue), var(--matrix-purple));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-shadow: 0 0 30px var(--matrix-green);
        margin-bottom: 20px !important;
        animation: title-glow 3s ease-in-out infinite alternate;
        position: relative;
        z-index: 1;
    }
    
    .hero-subtitle {
        font-family: 'Share Tech Mono', monospace !important;
        font-size: 1.5rem !important;
        color: var(--matrix-neon-blue) !important;
        text-shadow: 0 0 20px var(--matrix-neon-blue);
        margin-bottom: 30px !important;
        animation: subtitle-flicker 2s linear infinite;
    }
    
    @keyframes title-glow {
        0% { text-shadow: 0 0 30px var(--matrix-green), 0 0 60px var(--matrix-green); }
        100% { text-shadow: 0 0 50px var(--matrix-bright-green), 0 0 100px var(--matrix-bright-green); }
    }
    
    @keyframes subtitle-flicker {
        0%, 98% { opacity: 1; }
        99% { opacity: 0.8; }
        100% { opacity: 1; }
    }
    
    /* Enhanced Sidebar Menu Boxes */
    .sidebar-menu-box {
        background: linear-gradient(135deg, rgba(0,0,0,0.95) 0%, rgba(0,143,17,0.1) 100%);
        border: 2px solid var(--matrix-green);
        border-radius: 15px;
        padding: 20px;
        margin: 15px 0;
        position: relative;
        overflow: hidden;
        box-shadow: 
            0 5px 25px rgba(0,255,65,0.3),
            inset 0 1px 0 rgba(255,255,255,0.1);
        transition: all 0.3s ease;
    }
    
    .sidebar-menu-box::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(0,255,65,0.2), transparent);
        transition: left 0.6s ease;
    }
    
    .sidebar-menu-box:hover {
        border-color: var(--matrix-bright-green);
        box-shadow: 
            0 8px 35px rgba(0,255,65,0.5),
            inset 0 1px 0 rgba(255,255,255,0.2);
        transform: translateY(-2px);
    }
    
    .sidebar-menu-box:hover::before {
        left: 100%;
    }
    
    .sidebar-menu-title {
        color: var(--matrix-bright-green) !important;
        font-family: 'Orbitron', monospace !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        text-align: center !important;
        margin-bottom: 15px !important;
        text-shadow: 0 0 10px var(--matrix-green);
        border-bottom: 1px solid var(--matrix-green);
        padding-bottom: 8px;
    }
    
    /* Enhanced sidebar navigation buttons */
    div[data-testid="stSidebar"] .stButton > button {
        width: 100% !important;
        margin: 6px 0 !important;
        background: linear-gradient(45deg, rgba(0,0,0,0.9), rgba(0,143,17,0.2)) !important;
        border: 2px solid var(--matrix-green) !important;
        border-radius: 12px !important;
        padding: 12px 18px !important;
        font-family: 'Orbitron', monospace !important;
        font-weight: 600 !important;
        font-size: 0.85rem !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        color: var(--matrix-green) !important;
        text-shadow: 0 0 8px var(--matrix-green) !important;
        box-shadow: 
            0 4px 15px rgba(0,255,65,0.3),
            inset 0 1px 0 rgba(255,255,255,0.1) !important;
        transition: all 0.3s ease !important;
        position: relative !important;
        overflow: hidden !important;
    }
    
    div[data-testid="stSidebar"] .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(0,255,65,0.4), transparent);
        transition: left 0.6s ease;
    }
    
    div[data-testid="stSidebar"] .stButton > button:hover {
        background: linear-gradient(45deg, rgba(0,143,17,0.6), rgba(0,255,65,0.4)) !important;
        color: #000000 !important;
        text-shadow: 0 0 8px #000000 !important;
        box-shadow: 
            0 6px 25px rgba(0,255,65,0.6),
            inset 0 1px 0 rgba(255,255,255,0.2) !important;
        transform: translateY(-3px) scale(1.02) !important;
        border-color: var(--matrix-bright-green) !important;
    }
    
    div[data-testid="stSidebar"] .stButton > button:hover::before {
        left: 100%;
    }
    
    /* Horizontal Navigation Menu */
    .horizontal-nav {
        background: linear-gradient(135deg, rgba(0,0,0,0.9) 0%, rgba(0,20,0,0.8) 100%);
        border: 2px solid var(--matrix-green);
        border-radius: 15px;
        padding: 20px;
        margin: 20px 0;
        position: relative;
        overflow: hidden;
        box-shadow: 0 10px 30px rgba(0,255,65,0.3);
    }
    
    .horizontal-nav::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(0,255,65,0.1), transparent);
        animation: nav-sweep 8s linear infinite;
        pointer-events: none;
    }
    
    @keyframes nav-sweep {
        0% { left: -100%; }
        100% { left: 100%; }
    }
    
    .horizontal-nav-title {
        color: var(--matrix-neon-blue) !important;
        font-family: 'Orbitron', monospace !important;
        font-weight: 700 !important;
        font-size: 1.2rem !important;
        text-align: center !important;
        margin-bottom: 20px !important;
        text-shadow: 0 0 15px var(--matrix-neon-blue);
        position: relative;
        z-index: 1;
    }
    
    .nav-button {
        background: linear-gradient(45deg, rgba(0,0,0,0.8), rgba(0,143,17,0.3)) !important;
        color: var(--matrix-green) !important;
        border: 2px solid var(--matrix-green) !important;
        border-radius: 10px !important;
        padding: 12px 20px !important;
        font-family: 'Orbitron', monospace !important;
        font-weight: 600 !important;
        font-size: 0.9rem !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        text-shadow: 0 0 8px var(--matrix-green) !important;
        box-shadow: 0 4px 15px rgba(0,255,65,0.3) !important;
        transition: all 0.3s ease !important;
        position: relative !important;
        overflow: hidden !important;
        margin: 0 10px !important;
        cursor: pointer !important;
        min-width: 120px !important;
    }
    
    .nav-button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(0,255,65,0.4), transparent);
        transition: left 0.6s ease;
    }
    
    .nav-button:hover {
        background: linear-gradient(45deg, rgba(0,143,17,0.6), rgba(0,255,65,0.4)) !important;
        color: #000000 !important;
        text-shadow: 0 0 8px #000000 !important;
        box-shadow: 0 6px 25px rgba(0,255,65,0.6) !important;
        transform: translateY(-3px) scale(1.05) !important;
        border-color: var(--matrix-bright-green) !important;
    }
    
    .nav-button:hover::before {
        left: 100%;
    }
    
    .nav-button.active {
        background: linear-gradient(45deg, rgba(0,255,65,0.3), rgba(0,255,255,0.2)) !important;
        color: #000000 !important;
        border-color: var(--matrix-neon-blue) !important;
        box-shadow: 0 0 25px rgba(0,255,65,0.8) !important;
        text-shadow: 0 0 8px #000000 !important;
    }
    
    /* Service cards */
    .service-card {
        background: linear-gradient(135deg, rgba(0,0,0,0.9) 0%, rgba(0,20,0,0.8) 100%);
        border: 2px solid var(--matrix-green);
        border-radius: 15px;
        padding: 30px 20px;
        margin: 20px 10px;
        text-align: center;
        position: relative;
        overflow: hidden;
        transition: all 0.4s ease;
        box-shadow: 0 10px 30px rgba(0,255,65,0.3);
        cursor: pointer;
    }
    
    .service-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(0,255,65,0.2), transparent);
        transition: left 0.6s ease;
    }
    
    .service-card:hover {
        transform: translateY(-10px) scale(1.02);
        border-color: var(--matrix-neon-blue);
        box-shadow: 
            0 20px 50px rgba(0,255,65,0.5),
            0 0 50px rgba(0,255,255,0.3);
    }
    
    .service-card:hover::before {
        left: 100%;
    }
    
    .service-icon {
        font-size: 3rem;
        margin-bottom: 20px;
        display: block;
        text-shadow: 0 0 20px currentColor;
        animation: icon-float 3s ease-in-out infinite;
    }
    
    @keyframes icon-float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    /* Enhanced sidebar */
    .css-1d391kg, .css-1cypcdb, .css-17eq0hr {
        background: linear-gradient(180deg, #000000 0%, #0a0a0a 50%, #1a0a1a 100%) !important;
        border-right: 3px solid var(--matrix-green) !important;
        box-shadow: 10px 0 30px rgba(0,255,65,0.3) !important;
    }
    
    /* Stats section */
    .stats-container {
        background: rgba(0,0,0,0.8);
        border: 2px solid var(--matrix-purple);
        border-radius: 15px;
        padding: 30px;
        margin: 30px 0;
        box-shadow: 0 0 30px rgba(157,78,221,0.4);
    }
    
    .stat-item {
        text-align: center;
        padding: 20px;
    }
    
    .stat-number {
        font-family: 'Orbitron', monospace !important;
        font-size: 3rem !important;
        font-weight: 900 !important;
        color: var(--matrix-neon-blue) !important;
        text-shadow: 0 0 20px var(--matrix-neon-blue);
        display: block;
        margin-bottom: 10px;
        animation: number-count 2s ease-out;
    }
    
    @keyframes number-count {
        from { transform: scale(0); opacity: 0; }
        to { transform: scale(1); opacity: 1; }
    }
    
    /* Enhanced buttons */
    .stButton > button {
        background: linear-gradient(45deg, rgba(0,0,0,0.8), rgba(0,143,17,0.4)) !important;
        color: var(--matrix-bright-green) !important;
        border: 2px solid var(--matrix-green) !important;
        border-radius: 12px !important;
        font-family: 'Orbitron', monospace !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        padding: 15px 30px !important;
        text-shadow: 0 0 10px var(--matrix-green) !important;
        box-shadow: 0 0 20px rgba(0,255,65,0.3) !important;
        transition: all 0.3s ease !important;
        position: relative !important;
        overflow: hidden !important;
    }
    
    .stButton > button:hover {
        background: linear-gradient(45deg, rgba(0,143,17,0.6), rgba(0,255,65,0.4)) !important;
        color: #000000 !important;
        box-shadow: 0 0 40px var(--matrix-bright-green) !important;
        transform: translateY(-2px) !important;
    }
    
    /* Terminal styling */
    .terminal {
        background: rgba(0,0,0,0.95);
        border: 2px solid var(--matrix-green);
        border-radius: 10px;
        padding: 20px;
        font-family: 'Share Tech Mono', monospace;
        color: var(--matrix-green);
        text-shadow: 0 0 5px var(--matrix-green);
        box-shadow: 
            0 0 20px rgba(0,255,65,0.4),
            inset 0 0 20px rgba(0,255,65,0.1);
        margin: 20px 0;
    }
    
    /* Matrix container styling */
    .matrix-container {
        background: linear-gradient(135deg, rgba(0,0,0,0.9) 0%, rgba(0,20,0,0.8) 100%);
        border: 2px solid var(--matrix-green);
        border-radius: 15px;
        padding: 25px;
        margin: 20px 0;
        position: relative;
        overflow: hidden;
        box-shadow: 0 10px 30px rgba(0,255,65,0.3);
    }
    
    .matrix-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(0,255,65,0.1), transparent);
        animation: container-sweep 6s linear infinite;
        pointer-events: none;
    }
    
    @keyframes container-sweep {
        0% { left: -100%; }
        100% { left: 100%; }
    }
    </style>
    """, unsafe_allow_html=True)

def matrix_rain_effect():
    """Enhanced Matrix rain effect with multiple layers"""
    rain_script = """
    <script>
    function createEnhancedMatrixRain() {
        const matrixContainer = document.getElementById('matrix-bg');
        if (!matrixContainer) {
            const bgDiv = document.createElement('div');
            bgDiv.id = 'matrix-bg';
            bgDiv.className = 'matrix-bg';
            document.body.appendChild(bgDiv);
        }
        
        const container = document.getElementById('matrix-bg');
        const characters = '01ﾊﾐﾋｰｳｼﾅﾓﾆｻﾜﾂｵﾘｱﾎﾃﾏｹﾒｴｶｷﾑﾕﾗｾﾈｽﾀﾇﾍABCDEFGHIJKLMNOPQRSTUVWXYZ';
        const columns = Math.floor(window.innerWidth / 20);
        
        function createColumn(x) {
            const column = document.createElement('div');
            column.className = 'matrix-rain';
            column.style.left = x + 'px';
            column.style.animationDuration = (Math.random() * 4 + 3) + 's';
            column.style.animationDelay = Math.random() * 3 + 's';
            
            let text = '';
            const length = Math.random() * 30 + 15;
            for (let i = 0; i < length; i++) {
                text += characters.charAt(Math.floor(Math.random() * characters.length)) + '<br>';
            }
            column.innerHTML = text;
            
            container.appendChild(column);
            
            setTimeout(() => {
                if (column.parentNode) {
                    column.parentNode.removeChild(column);
                }
            }, 8000);
        }
        
        // Initialize effects
        for (let i = 0; i < columns; i++) {
            setTimeout(() => createColumn(i * 20), Math.random() * 2000);
        }
    }
    
    // Initialize enhanced effects
    setTimeout(createEnhancedMatrixRain, 1000);
    setInterval(() => {
        const container = document.getElementById('matrix-bg');
        if (container) {
            const columns = Math.floor(window.innerWidth / 20);
            for (let i = 0; i < Math.min(5, columns); i++) {
                setTimeout(() => {
                    const x = Math.random() * window.innerWidth;
                    const column = document.createElement('div');
                    column.className = 'matrix-rain';
                    column.style.left = x + 'px';
                    column.style.animationDuration = (Math.random() * 4 + 3) + 's';
                    
                    let text = '';
                    const length = Math.random() * 30 + 15;
                    const chars = '01ﾊﾐﾋｰｳｼﾅﾓﾆｻﾜﾂｵﾘｱﾎﾃﾏｹﾒｴｶｷﾑﾕﾗｾﾈｽﾀﾇﾍABCDEFGHIJKLMNOPQRSTUVWXYZ';
                    for (let j = 0; j < length; j++) {
                        text += chars.charAt(Math.floor(Math.random() * chars.length)) + '<br>';
                    }
                    column.innerHTML = text;
                    
                    container.appendChild(column);
                    
                    setTimeout(() => {
                        if (column.parentNode) {
                            column.parentNode.removeChild(column);
                        }
                    }, 8000);
                }, Math.random() * 500);
            }
        }
    }, 300);
    </script>
    """
    st.components.v1.html(rain_script, height=0)

def create_hero_section():
    """Create website-style hero section"""
    st.markdown("""
    <div class="hero-section">
        <h1 class="hero-title">AI CALL CENTER</h1>
        <p class="hero-subtitle">Neural Network Customer Service Protocol</p>
        <p style="color: #00ff41; font-size: 1.2rem; margin-bottom: 30px; font-family: 'Share Tech Mono', monospace;">
            Advanced AI-Powered Communication Hub | 24/7 Neural Interface | Quantum Response Technology
        </p>
    </div>
    """, unsafe_allow_html=True)

def create_horizontal_nav(current_tab, tabs, tab_key):
    """Create horizontal navigation menu for pages"""
    st.markdown(f"""
    <div class="horizontal-nav">
        <h3 class="horizontal-nav-title">NAVIGATION MATRIX</h3>
        <div style="display: flex; justify-content: center; flex-wrap: wrap; gap: 10px; position: relative; z-index: 1;">
    """, unsafe_allow_html=True)
    
    # Create navigation buttons
    cols = st.columns(len(tabs))
    for i, (tab_name, tab_display) in enumerate(tabs.items()):
        with cols[i]:
            active_class = "active" if current_tab == tab_name else ""
            if st.button(tab_display, key=f"{tab_key}_{tab_name}", 
                        help=f"Navigate to {tab_display}"):
                return tab_name
    
    st.markdown("</div></div>", unsafe_allow_html=True)
    return current_tab

def create_services_section():
    """Create services showcase"""
    st.markdown("""
    <div style="text-align: center; margin: 50px 0;">
        <h2 style="font-family: 'Orbitron', monospace; color: #39ff14; font-size: 2.5rem; text-shadow: 0 0 20px #00ff41;">
            NEURAL SERVICES
        </h2>
        <p style="color: #00ffff; font-size: 1.2rem; margin-bottom: 40px;">
            Advanced AI-Powered Communication Solutions
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="service-card">
            <span class="service-icon" style="color: #00ff41;">🤖</span>
            <h3 style="color: #39ff14; margin-bottom: 15px;">AI VOICE AGENTS</h3>
            <p style="color: #00ff41; margin-bottom: 15px;">
                Advanced neural network voice processing with real-time sentiment analysis
            </p>
            <ul style="color: #008f11; text-align: left; font-size: 0.9rem;">
                <li>Call Quality Analysis</li>
                <li>Performance Metrics</li>
                <li>Predictive Analytics</li>
                <li>Custom Reporting</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="service-card">
            <span class="service-icon" style="color: #9d4edd;">🧠</span>
            <h3 style="color: #9d4edd; margin-bottom: 15px;">NEURAL TRAINING</h3>
            <p style="color: #00ff41; margin-bottom: 15px;">
                Continuous AI model training and optimization protocols
            </p>
            <ul style="color: #008f11; text-align: left; font-size: 0.9rem;">
                <li>Machine Learning Models</li>
                <li>Adaptive Responses</li>
                <li>Performance Optimization</li>
                <li>Custom Training Data</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

def create_stats_section():
    """Create statistics showcase"""
    st.markdown("""
    <div class="stats-container">
        <h3 style="text-align: center; color: #9d4edd; font-size: 2rem; margin-bottom: 30px; font-family: 'Orbitron', monospace;">
            SYSTEM PERFORMANCE MATRIX
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="stat-item">
            <span class="stat-number">99.9%</span>
            <p style="color: #00ff41; font-weight: bold;">UPTIME</p>
            <p style="color: #008f11; font-size: 0.8rem;">System Reliability</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stat-item">
            <span class="stat-number">50K+</span>
            <p style="color: #00ff41; font-weight: bold;">CALLS/DAY</p>
            <p style="color: #008f11; font-size: 0.8rem;">Daily Processing</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stat-item">
            <span class="stat-number">0.3s</span>
            <p style="color: #00ff41; font-weight: bold;">RESPONSE</p>
            <p style="color: #008f11; font-size: 0.8rem;">Average Time</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="stat-item">
            <span class="stat-number">95%</span>
            <p style="color: #00ff41; font-weight: bold;">SATISFACTION</p>
            <p style="color: #008f11; font-size: 0.8rem;">Customer Rating</p>
        </div>
        """, unsafe_allow_html=True)

# Page functions
def home_page():
    # Matrix rain effect
    matrix_rain_effect()
    
    # Hero section
    create_hero_section()
    
    # Horizontal navigation for home page sections
    if 'home_tab' not in st.session_state:
        st.session_state.home_tab = "overview"
    
    home_tabs = {
        "overview": "🏠 OVERVIEW",
        "services": "⚙️ SERVICES", 
        "stats": "📊 STATISTICS",
        "status": "💻 STATUS"
    }
    
    st.session_state.home_tab = create_horizontal_nav(
        st.session_state.home_tab, home_tabs, "home"
    )
    
    # Display content based on selected tab
    if st.session_state.home_tab == "overview":
        st.markdown("""
        <div class="matrix-container">
            <h3 style="color: #39ff14; text-align: center;">SYSTEM OVERVIEW</h3>
            <p style="color: #00ffff; text-align: center; font-size: 1.1rem; margin: 20px 0;">
                Welcome to the AI Call Center Neural Interface - your gateway to advanced customer service automation.
            </p>
            <div style="text-align: center; margin: 30px 0;">
                <p style="color: #00ff41;">Current Status: <span style="color: #39ff14; font-weight: bold;">ONLINE</span></p>
                <p style="color: #00ff41;">Active Agents: <span style="color: #39ff14; font-weight: bold;">247</span></p>
                <p style="color: #00ff41;">Queue Status: <span style="color: #39ff14; font-weight: bold;">OPTIMAL</span></p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔊 CONNECT TO AI AGENT", key="connect_overview"):
                st.success("AI Agent ready - Connection established")
        with col2:
            if st.button("📊 VIEW DASHBOARD", key="dashboard_overview"):
                st.info("Opening analytics dashboard...")
    
    elif st.session_state.home_tab == "services":
        create_services_section()
    
    elif st.session_state.home_tab == "stats":
        create_stats_section()
    
    elif st.session_state.home_tab == "status":
        st.markdown("""
        <div class="matrix-container">
            <h3 style="color: #39ff14; text-align: center;">LIVE SYSTEM STATUS</h3>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="terminal">
            <div style="color: #39ff14;">[SYSTEM] AI Call Center online</div>
            <div style="color: #00ffff;">[STATUS] All systems operational</div>
            <div style="color: #39ff14;">[READY] Standing by for connections</div>
            <div style="color: #9d4edd;">[AI] Neural networks active</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="terminal">
            <div style="color: #00ffff;">[LOAD] CPU: 34% | RAM: 67%</div>
            <div style="color: #39ff14;">[NETWORK] Latency: 12ms</div>
            <div style="color: #00ffff;">[AGENTS] 247 active, 0 offline</div>
            <div style="color: #39ff14;">[QUEUE] 23 calls waiting</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="terminal">
            <div style="color: #9d4edd;">[ML] Model accuracy: 94.7%</div>
            <div style="color: #00ffff;">[SECURITY] All shields up</div>
            <div style="color: #39ff14;">[BACKUP] Systems synced</div>
            <div style="color: #00ffff;">[UPDATE] Ready for deployment</div>
            </div>
            """, unsafe_allow_html=True)

def call_analytics_page():
    st.markdown("""
    <div class="hero-section" style="margin-bottom: 40px;">
        <h1 style="color: #39ff14; font-size: 2.5rem;">CALL ANALYTICS</h1>
        <p style="color: #00ffff; font-size: 1.2rem;">Real-time Performance Dashboard</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Horizontal navigation for analytics
    if 'analytics_tab' not in st.session_state:
        st.session_state.analytics_tab = "dashboard"
    
    analytics_tabs = {
        "dashboard": "📊 DASHBOARD",
        "realtime": "⚡ REAL-TIME",
        "reports": "📈 REPORTS",
        "trends": "📉 TRENDS"
    }
    
    st.session_state.analytics_tab = create_horizontal_nav(
        st.session_state.analytics_tab, analytics_tabs, "analytics"
    )
    
    if st.session_state.analytics_tab == "dashboard":
        # Real-time metrics dashboard
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Active Calls", "1,247", "↑ 23")
        with col2:
            st.metric("Avg Response", "0.3s", "↓ 0.1s")
        with col3:
            st.metric("Satisfaction", "96.8%", "↑ 1.2%")
        with col4:
            st.metric("Resolution", "94.5%", "↑ 2.1%")
        
        st.markdown("---")
        
        # Charts section
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Call Volume Trends")
            chart_data = pd.DataFrame({
                'hour': range(24),
                'calls': [300 + 200 * np.sin(h/24 * 2 * np.pi) + np.random.randint(-50, 50) for h in range(24)]
            })
            st.line_chart(chart_data.set_index('hour'))
        
        with col2:
            st.markdown("### Performance Overview")
            performance_data = {
                'Metric': ['Response Time', 'Satisfaction', 'Resolution', 'Efficiency'],
                'Score': [95, 97, 94, 89]
            }
            st.bar_chart(pd.DataFrame(performance_data).set_index('Metric'))
    
    elif st.session_state.analytics_tab == "realtime":
        st.markdown("""
        <div class="matrix-container">
            <h3 style="color: #00ffff;">REAL-TIME MONITORING</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Real-time call monitoring
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Live Call Distribution")
            categories = ['Technical', 'Billing', 'Sales', 'Support', 'General']
            values = [random.randint(10, 50) for _ in categories]
            
            fig = px.pie(values=values, names=categories, 
                        title="Current Call Categories",
                        color_discrete_sequence=['#00ff41', '#00ffff', '#9d4edd', '#39ff14', '#008f11'])
            
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0.9)',
                paper_bgcolor='rgba(0,0,0,0.9)',
                font_color='#00ff41',
                title_font_color='#39ff14'
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("#### Agent Performance")
            agents = [f"Agent-{i:03d}" for i in range(1, 11)]
            performance = [random.randint(80, 100) for _ in agents]
            
            fig = px.bar(x=agents, y=performance,
                        title="Top 10 Agent Performance",
                        color=performance,
                        color_continuous_scale='Greens')
            
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0.9)',
                paper_bgcolor='rgba(0,0,0,0.9)',
                font_color='#00ff41',
                title_font_color='#00ffff',
                xaxis_tickangle=-45
            )
            st.plotly_chart(fig, use_container_width=True)
    
    elif st.session_state.analytics_tab == "reports":
        st.markdown("""
        <div class="matrix-container">
            <h3 style="color: #9d4edd;">ANALYTICS REPORTS</h3>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📊 DAILY REPORT", key="daily_report"):
                st.success("Generating daily analytics report...")
        
        with col2:
            if st.button("📈 WEEKLY SUMMARY", key="weekly_report"):
                st.success("Compiling weekly performance summary...")
        
        with col3:
            if st.button("📉 MONTHLY ANALYSIS", key="monthly_report"):
                st.success("Processing monthly trend analysis...")
        
        # Sample report data
        st.markdown("#### Recent Performance Metrics")
        report_data = pd.DataFrame({
            'Date': pd.date_range('2024-01-01', periods=30, freq='D'),
            'Calls_Handled': np.random.randint(800, 1500, 30),
            'Avg_Response_Time': np.random.uniform(0.2, 0.8, 30),
            'Satisfaction_Score': np.random.uniform(85, 98, 30)
        })
        
        st.dataframe(report_data.tail(10), use_container_width=True)
    
    elif st.session_state.analytics_tab == "trends":
        st.markdown("""
        <div class="matrix-container">
            <h3 style="color: #39ff14;">TREND ANALYSIS</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Generate trend data
        dates = pd.date_range('2024-01-01', periods=90, freq='D')
        trend_data = pd.DataFrame({
            'Date': dates,
            'Call_Volume': 1000 + 200 * np.sin(np.arange(90) * 2 * np.pi / 7) + np.random.normal(0, 50, 90),
            'Response_Time': 0.5 + 0.2 * np.sin(np.arange(90) * 2 * np.pi / 30) + np.random.normal(0, 0.05, 90),
            'Satisfaction': 90 + 5 * np.sin(np.arange(90) * 2 * np.pi / 14) + np.random.normal(0, 2, 90)
        })
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Call Volume Trends (90 Days)")
            fig = px.line(trend_data, x='Date', y='Call_Volume',
                         title="Daily Call Volume")
            fig.update_traces(line_color='#00ff41')
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0.9)',
                paper_bgcolor='rgba(0,0,0,0.9)',
                font_color='#00ff41',
                title_font_color='#39ff14'
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("#### Satisfaction Trends")
            fig = px.line(trend_data, x='Date', y='Satisfaction',
                         title="Customer Satisfaction Score")
            fig.update_traces(line_color='#00ffff')
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0.9)',
                paper_bgcolor='rgba(0,0,0,0.9)',
                font_color='#00ff41',
                title_font_color='#00ffff'
            )
            st.plotly_chart(fig, use_container_width=True)

def ai_neural_control_page():
    st.markdown("""
    <div class="hero-section" style="margin-bottom: 40px;">
        <h1 style="color: #9d4edd; font-size: 2.5rem;">NEURAL CONTROL CENTER</h1>
        <p style="color: #00ffff; font-size: 1.2rem;">AI Agent Training & Management Protocol</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Horizontal navigation for neural control
    if 'neural_tab' not in st.session_state:
        st.session_state.neural_tab = "config"
    
    neural_tabs = {
        "config": "⚙️ CONFIG",
        "training": "🚀 TRAINING",
        "monitoring": "🧠 MONITORING",
        "models": "🤖 MODELS"
    }
    
    st.session_state.neural_tab = create_horizontal_nav(
        st.session_state.neural_tab, neural_tabs, "neural"
    )
    
    if st.session_state.neural_tab == "config":
        # AI Agent configuration
        st.markdown("""
        <div class="matrix-container">
            <h3 style="color: #39ff14;">AI AGENT CONFIGURATION</h3>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("#### Neural Network Settings")
            layers = st.slider("Hidden Layers", 5, 20, 12, key="layers")
            neurons = st.slider("Neurons per Layer", 64, 512, 256, key="neurons")
            learning_rate = st.select_slider("Learning Rate", 
                                           options=[0.0001, 0.001, 0.01, 0.1],
                                           value=0.001, key="lr")
        
        with col2:
            st.markdown("#### Response Parameters")
            response_speed = st.slider("Response Speed (ms)", 50, 1000, 200, key="speed")
            context_window = st.slider("Context Window", 1000, 10000, 4000, key="context")
            temperature = st.slider("Creativity Level", 0.1, 2.0, 0.7, key="temp")
        
        with col3:
            st.markdown("#### Safety & Monitoring")
            safety_level = st.select_slider("Safety Filter Level", 
                                          options=["Low", "Medium", "High", "Maximum"],
                                          value="High", key="safety")
            monitoring = st.checkbox("Real-time Monitoring", True, key="monitor")
            auto_learning = st.checkbox("Auto-Learning Mode", True, key="auto_learn")
    
    elif st.session_state.neural_tab == "training":
        st.markdown("""
        <div class="matrix-container">
            <h3 style="color: #00ffff;">NEURAL TRAINING INTERFACE</h3>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            training_data = st.selectbox("Training Dataset", 
                                       ["Customer Service Calls", "Technical Support", "Sales Inquiries", "Custom Dataset"],
                                       key="training_data")
            
            epochs = st.number_input("Training Epochs", 1, 1000, 100, key="epochs")
            batch_size = st.selectbox("Batch Size", [16, 32, 64, 128, 256], index=2, key="batch")
        
        with col2:
            st.markdown("#### Current Model Performance")
            st.metric("Accuracy", "94.7%", "↑ 2.3%")
            st.metric("Loss", "0.0234", "↓ 0.0045")
            st.metric("F1 Score", "0.923", "↑ 0.015")
        
        # Training controls
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            if st.button("🚀 START TRAINING", key="start_train"):
                start_neural_training(epochs, batch_size)
        
        with col2:
            if st.button("⏸️ PAUSE TRAINING", key="pause_train"):
                st.warning("Training paused - Model state saved")
        
        with col3:
            if st.button("🔄 RESET MODEL", key="reset_model"):
                st.error("Model reset - All progress cleared")
        
        with col4:
            if st.button("💾 SAVE MODEL", key="save_model"):
                st.success("Model saved successfully!")
    
    elif st.session_state.neural_tab == "monitoring":
        st.markdown("""
        <div class="matrix-container">
            <h3 style="color: #9d4edd;">NEURAL NETWORK MONITORING</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Live neural network visualization
        if st.button("🧠 VISUALIZE NEURAL NETWORK", key="viz_neural"):
            visualize_neural_network(12, 256)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="terminal">
            <div style="color: #9d4edd;">[NEURAL] Networks online: 5/5</div>
            <div style="color: #00ffff;">[STATUS] Training active</div>
            <div style="color: #39ff14;">[PERF] Accuracy: 94.7%</div>
            <div style="color: #00ffff;">[LOAD] GPU utilization: 78%</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="terminal">
            <div style="color: #39ff14;">[MODEL] Primary: ACTIVE</div>
            <div style="color: #00ffff;">[BACKUP] Secondary: STANDBY</div>
            <div style="color: #9d4edd;">[SYNC] Models synchronized</div>
            <div style="color: #39ff14;">[UPDATE] Ready for deployment</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="terminal">
            <div style="color: #00ffff;">[MEMORY] Usage: 12.4GB/32GB</div>
            <div style="color: #39ff14;">[CACHE] Hit rate: 94.2%</div>
            <div style="color: #9d4edd;">[LATENCY] Avg: 23ms</div>
            <div style="color: #00ffff;">[THROUGHPUT] 2.1K req/sec</div>
            </div>
            """, unsafe_allow_html=True)
    
    elif st.session_state.neural_tab == "models":
        st.markdown("""
        <div class="matrix-container">
            <h3 style="color: #39ff14;">MODEL MANAGEMENT</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Model comparison table
        model_data = pd.DataFrame({
            'Model': ['GPT-Neo-Customer', 'BERT-Support', 'T5-Sales', 'Custom-Neural'],
            'Version': ['v2.1', 'v1.8', 'v3.0', 'v4.2'],
            'Accuracy': ['94.7%', '92.1%', '96.3%', '95.8%'],
            'Status': ['ACTIVE', 'STANDBY', 'ACTIVE', 'TRAINING'],
            'Last_Updated': ['2024-01-15', '2024-01-10', '2024-01-18', '2024-01-20']
        })
        
        st.dataframe(model_data, use_container_width=True)
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            if st.button("🔄 REFRESH MODELS", key="refresh_models"):
                st.success("Model registry refreshed")
        
        with col2:
            if st.button("📤 DEPLOY MODEL", key="deploy_model"):
                st.success("Model deployment initiated")
        
        with col3:
            if st.button("📥 IMPORT MODEL", key="import_model"):
                st.info("Model import wizard opened")
        
        with col4:
            if st.button("🗑️ CLEANUP OLD", key="cleanup_models"):
                st.warning("Old model versions cleaned up")

def start_neural_training(epochs, batch_size):
    """Simulate neural network training"""
    st.markdown("""
    <div class="terminal">
        <div style="color: #39ff14; font-weight: bold;">INITIATING NEURAL TRAINING PROTOCOL...</div>
    </div>
    """, unsafe_allow_html=True)
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    metrics_placeholder = st.empty()
    
    # Training simulation
    for epoch in range(min(epochs, 20)):  # Limit for demo
        # Simulate training metrics
        accuracy = 0.6 + (epoch / 20) * 0.35 + random.uniform(-0.02, 0.02)
        loss = 1.5 * np.exp(-epoch/8) + random.uniform(-0.1, 0.1)
        f1_score = 0.55 + (epoch / 20) * 0.38 + random.uniform(-0.02, 0.02)
        
        progress = (epoch + 1) / min(epochs, 20)
        progress_bar.progress(progress)
        
        status_text.markdown(f"""
        <div class="terminal">
            <div>Epoch {epoch+1}/{min(epochs, 20)} | Batch Size: {batch_size}</div>
            <div style="color: #00ffff;">Training Loss: {loss:.4f} | Accuracy: {accuracy:.3f}</div>
            <div style="color: #39ff14;">Neural pathways optimizing... {'█' * int(progress * 30)}</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Update metrics
        col1, col2, col3 = metrics_placeholder.columns(3)
        with col1:
            st.metric("Accuracy", f"{accuracy:.1%}", f"{random.uniform(0.5, 2.0):.1f}%")
        with col2:
            st.metric("Loss", f"{loss:.4f}", f"{random.uniform(-0.05, -0.01):.4f}")
        with col3:
            st.metric("F1 Score", f"{f1_score:.3f}", f"{random.uniform(0.005, 0.02):.3f}")
        
        time.sleep(0.3)
    
    st.success("NEURAL TRAINING COMPLETE! Model performance optimized.")
    st.balloons()

def visualize_neural_network(layers, neurons):
    """Create neural network visualization"""
    st.markdown("""
    <div class="matrix-container">
        <h4 style="color: #9d4edd;">NEURAL NETWORK ARCHITECTURE</h4>
    </div>
    """, unsafe_allow_html=True)
    
    # Generate network data
    network_data = []
    for layer in range(layers + 2):  # +2 for input and output
        layer_neurons = neurons if 0 < layer <= layers else max(neurons//4, 8)
        for neuron in range(layer_neurons):
            activation = random.uniform(0.1, 1.0)
            network_data.append({
                'layer': layer,
                'neuron': neuron,
                'activation': activation,
                'size': activation * 15 + 5,
                'layer_type': 'Input' if layer == 0 else 'Output' if layer == layers + 1 else 'Hidden'
            })
    
    network_df = pd.DataFrame(network_data)
    
    # Create visualization
    fig = px.scatter(network_df, x='layer', y='neuron',
                    size='size', color='activation',
                    color_continuous_scale='Viridis',
                    title="AI Neural Network Activation Map",
                    hover_data=['layer_type'])
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0.9)',
        paper_bgcolor='rgba(0,0,0,0.9)',
        font_color='#00ff41',
        title_font_color='#9d4edd',
        xaxis_title="Network Layer",
        yaxis_title="Neuron Index"
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Network stats
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Neurons", f"{len(network_df):,}")
    with col2:
        st.metric("Active Layers", f"{layers + 2}")
    with col3:
        st.metric("Avg Activation", f"{network_df['activation'].mean():.3f}")
    with col4:
        st.metric("Network Efficiency", f"{random.uniform(85, 98):.1f}%")

# Enhanced sidebar with better menu boxes
def create_sidebar():
    """Create enhanced sidebar with menu boxes"""
    st.sidebar.markdown("""
    <div style="text-align: center; padding: 20px 0; border-bottom: 2px solid #00ff41; margin-bottom: 20px;">
        <h1 style="color: #39ff14; text-shadow: 0 0 20px #00ff41; font-size: 1.8rem; font-family: 'Orbitron', monospace;">🤖</h1>
        <h2 style="color: #00ff41; text-shadow: 0 0 15px #00ff41; font-family: 'Orbitron', monospace; margin: 5px 0; font-size: 1.2rem;">AI CALL CENTER</h2>
        <p style="color: #00ffff; font-size: 0.8em; font-family: 'Share Tech Mono', monospace;">Neural Interface v4.0</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation menu box
    st.sidebar.markdown("""
    <div class="sidebar-menu-box">
        <h4 class="sidebar-menu-title">NAVIGATION</h4>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize session state for page selection
    if 'current_page' not in st.session_state:
        st.session_state.current_page = "Command Center"
    
    # Navigation buttons
    nav_buttons = [
        ("🏠 COMMAND CENTER", "Command Center"),
        ("📊 CALL ANALYTICS", "Call Analytics"), 
        ("🧠 NEURAL CONTROL", "Neural Control")
    ]
    
    for button_text, page_key in nav_buttons:
        if st.sidebar.button(button_text, key=f"nav_{page_key}", use_container_width=True):
            st.session_state.current_page = page_key
    
    # System status menu box
    st.sidebar.markdown("""
    <div class="sidebar-menu-box">
        <h4 class="sidebar-menu-title">SYSTEM STATUS</h4>
    </div>
    """, unsafe_allow_html=True)
    
    # Live metrics in columns
    col1, col2 = st.sidebar.columns(2)
    with col1:
        st.metric("Calls", "1.2K", "↑ 150", delta_color="normal")
        st.metric("Load", "67%", "↓ 5%", delta_color="inverse")
    with col2:
        st.metric("Agents", "185", "→", delta_color="off")
        st.metric("Response", "0.3s", "↓ 0.1s", delta_color="inverse")
    
    # Operator profile box
    st.sidebar.markdown("""
    <div class="sidebar-menu-box">
        <h4 class="sidebar-menu-title">OPERATOR PROFILE</h4>
        <div style="text-align: center; font-size: 0.9rem;">
            <p><strong>ID:</strong> ADMIN-7734</p>
            <p><strong>Status:</strong> <span style="color: #39ff14;">ACTIVE</span></p>
            <p><strong>Level:</strong> <span style="color: #00ffff;">MAXIMUM</span></p>
            <p><strong>Sessions:</strong> 1,247</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick actions menu box
    st.sidebar.markdown("""
    <div class="sidebar-menu-box">
        <h4 class="sidebar-menu-title">QUICK ACTIONS</h4>
    </div>
    """, unsafe_allow_html=True)
    
    quick_actions = [
        ("🚨 EMERGENCY", "emergency_action"),
        ("🔄 RESTART", "restart_action"),
        ("📊 EXPORT", "export_action"),
        ("🛡️ SECURITY", "security_action")
    ]
    
    cols = st.sidebar.columns(2)
    for i, (action_text, action_key) in enumerate(quick_actions):
        with cols[i % 2]:
            if st.button(action_text, key=action_key, help=f"Execute {action_text.split()[1].lower()} protocol"):
                if "EMERGENCY" in action_text:
                    st.sidebar.error("🚨 Emergency protocol activated!")
                elif "RESTART" in action_text:
                    st.sidebar.warning("🔄 System restart initiated...")
                elif "EXPORT" in action_text:
                    st.sidebar.success("📊 Data exported")
                elif "SECURITY" in action_text:
                    st.sidebar.info("🛡️ Security scan active")
    
    # Network diagnostics box
    st.sidebar.markdown("""
    <div class="sidebar-menu-box">
        <h4 class="sidebar-menu-title">NETWORK DIAGNOSTICS</h4>
        <div style="font-family: 'Share Tech Mono', monospace; font-size: 0.8rem;">
            <div style="color: #39ff14;">✓ Primary Server: ONLINE</div>
            <div style="color: #39ff14;">✓ Backup Systems: READY</div>
            <div style="color: #00ffff;">⚡ Latency: 12ms</div>
            <div style="color: #00ffff;">📡 Bandwidth: 98% available</div>
            <div style="color: #9d4edd;">🧠 AI Models: 5/5 active</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Main application
def main():
    st.set_page_config(
        page_title="AI Call Center | Neural Interface",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Apply enhanced Matrix theme
    apply_matrix_theme()
    
    # Create enhanced sidebar
    create_sidebar()
    
    # Page mapping
    pages = {
        "Command Center": home_page,
        "Call Analytics": call_analytics_page,
        "Neural Control": ai_neural_control_page
    }
    
    # Execute selected page
    pages[st.session_state.current_page]()
    
    # Enhanced footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 30px 20px; background: rgba(0,0,0,0.8); border-radius: 15px; margin-top: 50px;">
        <h4 style="color: #39ff14; font-family: 'Orbitron', monospace; margin-bottom: 15px;">
            🤖 AI CALL CENTER NEURAL INTERFACE
        </h4>
        <p style="color: #00ffff; font-family: 'Share Tech Mono', monospace; font-size: 0.9em; margin: 10px 0;">
            Advanced Neural Network Communication Hub | Version 4.0
        </p>
        <p style="color: #008f11; font-size: 0.8em; font-style: italic; margin: 5px 0;">
            "The future of customer service is here - powered by artificial intelligence"
        </p>
        <div style="margin-top: 20px; padding-top: 15px; border-top: 1px solid #00ff41;">
            <p style="color: #004408; font-size: 0.7em;">
                © 2024 Neural Systems Corp. | All rights reserved | Powered by Matrix AI
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()Natural Language Processing</li>
                <li>Multi-language Support</li>
                <li>Emotion Recognition</li>
                <li>24/7 Availability</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="service-card">
            <span class="service-icon" style="color: #00ffff;">📊</span>
            <h3 style="color: #00ffff; margin-bottom: 15px;">DATA ANALYTICS</h3>
            <p style="color: #00ff41; margin-bottom: 15px;">
                Real-time call analytics and performance monitoring dashboard
            </p>
            <ul style="color: #008f11; text-align: left; font-size: 0.9rem;">
                <li>
