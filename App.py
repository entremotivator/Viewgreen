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
    
    /* CTA Buttons */
    .cta-button {
        background: linear-gradient(45deg, var(--matrix-dark-green), var(--matrix-green), var(--matrix-bright-green));
        color: #000000 !important;
        border: none !important;
        border-radius: 50px !important;
        padding: 20px 40px !important;
        font-family: 'Orbitron', monospace !important;
        font-weight: 700 !important;
        font-size: 1.2rem !important;
        text-transform: uppercase !important;
        letter-spacing: 2px !important;
        box-shadow: 0 10px 30px rgba(0,255,65,0.5) !important;
        transition: all 0.3s ease !important;
        position: relative !important;
        overflow: hidden !important;
        cursor: pointer !important;
    }
    
    .cta-button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
        transition: left 0.5s ease;
    }
    
    .cta-button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 15px 40px rgba(0,255,65,0.7) !important;
        background: linear-gradient(45deg, var(--matrix-green), var(--matrix-bright-green), var(--matrix-neon-blue)) !important;
    }
    
    .cta-button:hover::before {
        left: 100%;
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
    
    /* Enhanced sidebar */
    .css-1d391kg, .css-1cypcdb, .css-17eq0hr {
        background: linear-gradient(180deg, #000000 0%, #0a0a0a 50%, #1a0a1a 100%) !important;
        border-right: 3px solid var(--matrix-green) !important;
        box-shadow: 10px 0 30px rgba(0,255,65,0.3) !important;
    }
    
    /* Floating elements */
    .floating-element {
        position: fixed;
        font-size: 20px;
        color: var(--matrix-green);
        text-shadow: 0 0 10px var(--matrix-green);
        animation: float-across 10s linear infinite;
        pointer-events: none;
        z-index: -1;
    }
    
    @keyframes float-across {
        0% {
            transform: translateX(-100px) translateY(0px);
            opacity: 0;
        }
        10% {
            opacity: 1;
        }
        90% {
            opacity: 1;
        }
        100% {
            transform: translateX(calc(100vw + 100px)) translateY(-50px);
            opacity: 0;
        }
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
    
    .terminal-line {
        margin: 5px 0;
        animation: typing 0.5s ease-in-out;
    }
    
    @keyframes typing {
        from { width: 0; opacity: 0; }
        to { width: 100%; opacity: 1; }
    }
    
    /* Glitch effect */
    .glitch {
        animation: glitch 2s linear infinite;
    }
    
    @keyframes glitch {
        0%, 90%, 100% {
            transform: translate(0);
        }
        91% {
            transform: translate(-2px, -1px);
        }
        92% {
            transform: translate(2px, 1px);
        }
        93% {
            transform: translate(-1px, 2px);
        }
        94% {
            transform: translate(1px, -2px);
        }
        95% {
            transform: translate(-2px, 1px);
        }
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
        
        // Create floating elements
        function createFloatingElement() {
            const symbols = ['◉', '◎', '●', '○', '◐', '◑', '◒', '◓'];
            const element = document.createElement('div');
            element.className = 'floating-element';
            element.textContent = symbols[Math.floor(Math.random() * symbols.length)];
            element.style.top = Math.random() * window.innerHeight + 'px';
            document.body.appendChild(element);
            
            setTimeout(() => {
                if (element.parentNode) {
                    element.parentNode.removeChild(element);
                }
            }, 10000);
        }
        
        // Initialize effects
        for (let i = 0; i < columns; i++) {
            setTimeout(() => createColumn(i * 20), Math.random() * 2000);
        }
        
        // Create floating elements periodically
        setInterval(createFloatingElement, 3000);
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
            🤖 Advanced AI-Powered Communication Hub | 24/7 Neural Interface | Quantum Response Technology
        </p>
        <div style="margin-top: 40px;">
            <button class="cta-button" onclick="window.scrollTo(0, 500);">
                🚀 CONNECT NOW
            </button>
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_services_section():
    """Create services showcase"""
    st.markdown("""
    <div style="text-align: center; margin: 50px 0;">
        <h2 style="font-family: 'Orbitron', monospace; color: #39ff14; font-size: 2.5rem; text-shadow: 0 0 20px #00ff41;">
            🌐 NEURAL SERVICES
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
                <li>Natural Language Processing</li>
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
            ⚡ SYSTEM PERFORMANCE MATRIX
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
    
    # Services section
    create_services_section()
    
    # Stats section
    create_stats_section()
    
    # Live terminal feed
    st.markdown("""
    <div style="margin: 50px 0;">
        <h3 style="color: #39ff14; font-family: 'Orbitron', monospace; text-align: center; margin-bottom: 30px;">
            💻 LIVE SYSTEM FEED
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    terminal_output = [
        "[SYSTEM] AI Call Center Neural Network initialized...",
        "[INFO] Loading customer service protocols...",
        "[SUCCESS] Voice recognition modules online",
        "[ANALYTICS] Processing 1,247 concurrent calls",
        "[AI-AGENT-001] Customer satisfaction: 98.7%",
        "[AI-AGENT-002] Average response time: 0.2s",
        "[SECURITY] Encryption protocols active",
        "[MONITOR] System performance optimal",
        "[NEURAL-NET] Learning from 50,000+ interactions daily",
        "[STATUS] All systems operational - Standing by..."
    ]
    
    terminal_html = '<div class="terminal">'
    for i, line in enumerate(terminal_output):
        color = "#00ff41"
        if "[ERROR]" in line: color = "#ff4141"
        elif "[WARNING]" in line: color = "#ffff41"
        elif "[SUCCESS]" in line: color = "#39ff14"
        elif "[ANALYTICS]" in line: color = "#00ffff"
        elif "[AI-AGENT" in line: color = "#9d4edd"
        
        terminal_html += f'<div class="terminal-line" style="color: {color}; animation-delay: {i*0.1}s;">{line}</div>'
    
    terminal_html += '</div>'
    st.markdown(terminal_html, unsafe_allow_html=True)
    
    # Action buttons
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("🔊 START CALL"):
            st.success("🤖 AI Agent connected - How may I assist you?")
    
    with col2:
        if st.button("📞 QUEUE STATUS"):
            st.info(f"📊 Current queue: {random.randint(5, 25)} calls | Avg wait: {random.randint(10, 45)}s")
    
    with col3:
        if st.button("🎯 PERFORMANCE"):
            st.metric("System Load", f"{random.randint(45, 85)}%", f"{random.randint(-5, 5)}%")
    
    with col4:
        if st.button("🚨 ALERT STATUS"):
            st.warning("⚠️ High call volume detected - Auto-scaling initiated")

def call_analytics_page():
    st.markdown("""
    <div class="hero-section" style="margin-bottom: 40px;">
        <h1 style="color: #39ff14; font-size: 2.5rem;">📊 CALL ANALYTICS</h1>
        <p style="color: #00ffff; font-size: 1.2rem;">Real-time Call Center Performance Matrix</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Real-time metrics dashboard
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        current_calls = random.randint(800, 1200)
        st.metric("🔴 Active Calls", f"{current_calls:,}", f"↑ {random.randint(10, 50)}")
    
    with col2:
        avg_time = random.uniform(0.2, 0.8)
        st.metric("⚡ Avg Response", f"{avg_time:.2f}s", f"↓ 0.1s")
    
    with col3:
        satisfaction = random.uniform(92, 99)
        st.metric("😊 Satisfaction", f"{satisfaction:.1f}%", f"↑ {random.uniform(0.5, 2.0):.1f}%")
    
    with col4:
        resolution = random.uniform(85, 95)
        st.metric("✅ Resolution Rate", f"{resolution:.1f}%", f"↑ {random.uniform(1, 3):.1f}%")
    
    with col5:
        agents = random.randint(150, 200)
        st.metric("🤖 AI Agents", f"{agents}", f"↑ {random.randint(5, 15)}")
    
    st.markdown("---")
    
    # Call volume trends
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="matrix-container">
            <h3 style="color: #39ff14;">📈 CALL VOLUME TRENDS</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Generate sample call data
        hours = list(range(24))
        call_volume = [random.randint(200, 800) + 300 * np.sin(h/24 * 2 * np.pi) for h in hours]
        
        fig = px.line(x=hours, y=call_volume, 
                     title="24-Hour Call Volume Pattern",
                     labels={"x": "Hour of Day", "y": "Call Volume"})
        
        fig.update_traces(line_color='#00ff41', line_width=3)
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0.9)',
            paper_bgcolor='rgba(0,0,0,0.9)',
            font_color='#00ff41',
            title_font_color='#39ff14',
            xaxis=dict(gridcolor='rgba(0,255,65,0.3)', showgrid=True),
            yaxis=dict(gridcolor='rgba(0,255,65,0.3)', showgrid=True)
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("""
        <div class="matrix-container">
            <h3 style="color: #00ffff;">🎯 RESPONSE TIME DISTRIBUTION</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Response time histogram
        response_times = np.random.gamma(2, 0.2, 1000)
        
        fig = px.histogram(x=response_times, nbins=30,
                          title="AI Response Time Distribution",
                          labels={"x": "Response Time (seconds)", "y": "Frequency"})
        
        fig.update_traces(marker_color='#00ffff')
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0.9)',
            paper_bgcolor='rgba(0,0,0,0.9)',
            font_color='#00ff41',
            title_font_color='#00ffff'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Agent performance matrix
    st.markdown("""
    <div class="matrix-container">
        <h3 style="color: #9d4edd;">🤖 AI AGENT PERFORMANCE MATRIX</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Generate agent performance data
    agent_data = []
    for i in range(10):
        agent_data.append({
            'Agent_ID': f'AI-{1000+i:04d}',
            'Status': random.choice(['ACTIVE', 'TRAINING', 'STANDBY']),
            'Calls_Handled': random.randint(50, 200),
            'Avg_Response_Time': round(random.uniform(0.1, 0.5), 2),
            'Satisfaction_Score': round(random.uniform(90, 99), 1),
            'Success_Rate': round(random.uniform(85, 98), 1),
            'Learning_Progress': round(random.uniform(75, 100), 1)
        })
    
    agent_df = pd.DataFrame(agent_data)
    st.dataframe(agent_df, use_container_width=True)
    
    # Sentiment analysis
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="matrix-container">
            <h3 style="color: #39ff14;">😊 SENTIMENT ANALYSIS</h3>
        </div>
        """, unsafe_allow_html=True)
        
        sentiments = ['Positive', 'Neutral', 'Negative']
        sentiment_counts = [random.randint(60, 80), random.randint(15, 25), random.randint(5, 15)]
        
        fig = px.pie(values=sentiment_counts, names=sentiments,
                    title="Customer Sentiment Distribution",
                    color_discrete_sequence=['#00ff41', '#ffff41', '#ff4141'])
        
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0.9)',
            paper_bgcolor='rgba(0,0,0,0.9)',
            font_color='#00ff41',
            title_font_color='#39ff14'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("""
        <div class="matrix-container">
            <h3 style="color: #00ffff;">📊 CALL CATEGORIES</h3>
        </div>
        """, unsafe_allow_html=True)
        
        categories = ['Technical Support', 'Billing', 'Sales', 'General Inquiry', 'Complaint']
        category_counts = [random.randint(20, 40) for _ in categories]
        
        fig = px.bar(x=categories, y=category_counts,
                    title="Call Categories Breakdown",
                    color=category_counts,
                    color_continuous_scale='Greens')
        
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0.9)',
            paper_bgcolor='rgba(0,0,0,0.9)',
            font_color='#00ff41',
            title_font_color='#00ffff',
            xaxis_tickangle=-45
        )
        st.plotly_chart(fig, use_container_width=True)

def ai_neural_control_page():
    st.markdown("""
    <div class="hero-section" style="margin-bottom: 40px;">
        <h1 style="color: #9d4edd; font-size: 2.5rem;">🧠 NEURAL CONTROL CENTER</h1>
        <p style="color: #00ffff; font-size: 1.2rem;">AI Agent Training & Management Protocol</p>
    </div>
    """, unsafe_allow_html=True)
    
    # AI Agent configuration
    st.markdown("""
    <div class="matrix-container">
        <h3 style="color: #39ff14;">⚙️ AI AGENT CONFIGURATION</h3>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### 🤖 Neural Network Settings")
        layers = st.slider("Hidden Layers", 5, 20, 12, key="layers")
        neurons = st.slider("Neurons per Layer", 64, 512, 256, key="neurons")
        learning_rate = st.select_slider("Learning Rate", 
                                       options=[0.0001, 0.001, 0.01, 0.1],
                                       value=0.001, key="lr")
    
    with col2:
        st.markdown("#### 🎯 Response Parameters")
        response_speed = st.slider("Response Speed (ms)", 50, 1000, 200, key="speed")
        context_window = st.slider("Context Window", 1000, 10000, 4000, key="context")
        temperature = st.slider("Creativity Level", 0.1, 2.0, 0.7, key="temp")
    
    with col3:
        st.markdown("#### 🛡️ Safety & Monitoring")
        safety_level = st.select_slider("Safety Filter Level", 
                                      options=["Low", "Medium", "High", "Maximum"],
                                      value="High", key="safety")
        monitoring = st.checkbox("Real-time Monitoring", True, key="monitor")
        auto_learning = st.checkbox("Auto-Learning Mode", True, key="auto_learn")
    
    # Neural network training interface
    st.markdown("---")
    st.markdown("""
    <div class="matrix-container">
        <h3 style="color: #00ffff;">🚀 NEURAL TRAINING INTERFACE</h3>
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
        st.markdown("#### 📊 Current Model Performance")
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
            st.warning("⏸️ Training paused - Model state saved")
    
    with col3:
        if st.button("🔄 RESET MODEL", key="reset_model"):
            st.error("🔄 Model reset - All progress cleared")
    
    with col4:
        if st.button("💾 SAVE MODEL", key="save_model"):
            st.success("💾 Model saved successfully!")
    
    # Live neural network visualization
    if st.button("🧠 VISUALIZE NEURAL NETWORK", key="viz_neural"):
        visualize_neural_network(layers, neurons)

def start_neural_training(epochs, batch_size):
    """Simulate neural network training"""
    st.markdown("""
    <div class="terminal">
        <div style="color: #39ff14; font-weight: bold;">🤖 INITIATING NEURAL TRAINING PROTOCOL...</div>
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
    
    st.success("🎉 NEURAL TRAINING COMPLETE! Model performance optimized.")
    st.balloons()

def visualize_neural_network(layers, neurons):
    """Create neural network visualization"""
    st.markdown("""
    <div class="matrix-container">
        <h4 style="color: #9d4edd;">🧠 NEURAL NETWORK ARCHITECTURE</h4>
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
    
    # Enhanced sidebar with call center branding
    st.sidebar.markdown("""
    <div style="text-align: center; padding: 30px 0; border-bottom: 2px solid #00ff41; margin-bottom: 30px;">
        <h1 style="color: #39ff14; text-shadow: 0 0 20px #00ff41; font-size: 2rem; font-family: 'Orbitron', monospace;">🤖</h1>
        <h2 style="color: #00ff41; text-shadow: 0 0 15px #00ff41; font-family: 'Orbitron', monospace; margin: 10px 0;">AI CALL CENTER</h2>
        <p style="color: #00ffff; font-size: 0.9em; font-family: 'Share Tech Mono', monospace;">Neural Interface v4.0</p>
        <p style="color: #008f11; font-size: 0.8em;">Advanced Communication Hub</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation menu
    pages = {
        "🏠 Command Center": home_page,
        "📊 Call Analytics": call_analytics_page,
        "🧠 Neural Control": ai_neural_control_page
    }
    
    selected_page = st.sidebar.selectbox("🌐 Navigate Hub", list(pages.keys()))
    
    # Enhanced operator profile
    st.sidebar.markdown("""
    <div class="matrix-container" style="margin: 20px 0; padding: 20px;">
        <h4 style="text-align: center; color: #39ff14; margin-bottom: 15px;">👤 OPERATOR STATUS</h4>
        <div style="text-align: center;">
            <p><strong>ID:</strong> ADMIN-7734</p>
            <p><strong>Clearance:</strong> <span style="color: #39ff14;">NEURAL-MAX</span></p>
            <p><strong>Session:</strong> Active</p>
            <p><strong>Location:</strong> Control Room Alpha</p>
            <p><strong>Access Level:</strong> <span style="color: #00ffff;">Full Control</span></p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Real-time system monitoring
    st.sidebar.markdown("### 📊 LIVE SYSTEM STATUS")
    
    # Dynamic metrics that update
    current_time = datetime.now()
    active_calls = random.randint(800, 1500)
    system_load = random.randint(45, 85)
    
    st.sidebar.metric("🔴 Active Calls", f"{active_calls:,}", f"↑ {random.randint(50, 150)}")
    st.sidebar.metric("💽 System Load", f"{system_load}%", f"{'↑' if system_load > 70 else '↓'} {random.randint(1, 5)}%")
    st.sidebar.metric("🤖 AI Agents", f"{random.randint(180, 220)}", "→ Stable")
    st.sidebar.metric("⚡ Response Time", f"{random.uniform(0.1, 0.5):.2f}s", "↓ Optimal")
    
    # Quick system controls
    st.sidebar.markdown("### ⚡ QUICK CONTROLS")
    
    if st.sidebar.button("🚨 EMERGENCY STOP", key="emergency"):
        st.sidebar.error("🚨 Emergency protocol activated!")
    
    if st.sidebar.button("🔄 SYSTEM RESTART", key="restart"):
        st.sidebar.warning("🔄 System restart initiated...")
    
    if st.sidebar.button("📊 EXPORT LOGS", key="export"):
        st.sidebar.success("📊 System logs exported successfully")
    
    if st.sidebar.button("🛡️ SECURITY SCAN", key="security"):
        st.sidebar.info("🛡️ Security scan in progress...")
    
    # System alerts
    st.sidebar.markdown("### 🚨 SYSTEM ALERTS")
    alerts = [
        "🟢 All systems operational",
        "🟡 High call volume detected",
        "🟢 AI training completed",
        "🔵 New agents deployed"
    ]
    
    for alert in alerts:
        st.sidebar.markdown(f"<small>{alert}</small>", unsafe_allow_html=True)
    
    # Execute selected page
    pages[selected_page]()
    
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
    main()
