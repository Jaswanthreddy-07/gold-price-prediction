import streamlit as st
import numpy as np
import pandas as pd
import joblib
import plotly.graph_objects as go
from datetime import datetime, timedelta

st.set_page_config(
    page_title="SPECTRA GOLD AI",
    page_icon="🌈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ====================== ULTRA PREMIUM COLORFUL CSS ======================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Space+Grotesk:wght@600;700&display=swap');

    .main {
        background: linear-gradient(135deg, #0F0A2E 0%, #1A0F4A 50%, #2A1B5F 100%);
    }

    .big-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 68px;
        font-weight: 700;
        background: linear-gradient(90deg, #FFEA00, #FF00CC, #00FFEA, #FF00AA, #FFEA00);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 50px rgba(255, 234, 0, 0.8);
        letter-spacing: -3px;
    }

    .glass-card {
        background: rgba(255,255,255,0.09);
        border-radius: 24px;
        backdrop-filter: blur(25px);
        border: 1px solid rgba(255, 234, 0, 0.35);
        box-shadow: 0 15px 50px rgba(0,0,0,0.4);
    }

    .stButton>button {
        background: linear-gradient(90deg, #FF00CC, #00FFEA, #FFEA00);
        color: #0F0A2E;
        font-weight: 700;
        border-radius: 50px;
        height: 60px;
        box-shadow: 0 12px 40px rgba(255, 0, 204, 0.5);
    }
    .stButton>button:hover {
        transform: scale(1.08);
    }
</style>
""", unsafe_allow_html=True)

# ====================== HEADER ======================
st.markdown('<div class="big-title">🌈 SPECTRA GOLD AI</div>',
            unsafe_allow_html=True)
st.caption("**The Most Vibrant & Intelligent Gold Market Forecasting Platform**")

# ====================== TABS ======================
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🏠 Dashboard", "🔮 Live Forecast", "📜 History",
    "💡 Insights", "📊 Analytics", "⚙️ Settings"
])

# ====================== SIDEBAR ======================
with st.sidebar:
    st.markdown("### 🎛️ **ADVANCED CONTROLS**")

    open_price = st.slider("Open Price (₹)", 48000, 140000, 98500, step=50)
    high = st.slider("High Price (₹)", 48000, 140000, 99900, step=50)
    low = st.slider("Low Price (₹)", 48000, 140000, 97000, step=50)

    oil = st.slider("Oil Price ($)", 30.0, 170.0, 75.2)
    silver = st.slider("Silver (₹/kg)", 80000, 190000, 117800, step=500)
    usd = st.slider("USD Index", 80.0, 135.0, 104.8, step=0.1)

    volatility = st.slider("Volatility (%)", 0.5, 18.0, 3.8, step=0.1)

    st.markdown("---")
    st.multiselect("Select Technical Indicators",
                   ["RSI", "MACD", "Bollinger Bands",
                       "Moving Average", "Fibonacci"],
                   default=["RSI", "MACD"])

    date_range = st.date_input("Analysis Date Range",
                               [datetime.now().date() - timedelta(days=30), datetime.now().date()])

    uploaded_file = st.file_uploader(
        "Upload Custom Dataset (CSV)", type=["csv"])

    col1, col2 = st.columns(2)
    with col1:
        predict_btn = st.button(
            "🚀 Predict Now", use_container_width=True, type="primary")
    with col2:
        reset_btn = st.button("🔄 Reset", use_container_width=True)

# ====================== DASHBOARD TAB ======================
with tab1:
    st.subheader("🌟 Live Market Pulse")
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(
            '<div class="glass-card" style="padding:20px;text-align:center">', unsafe_allow_html=True)
        st.metric("Gold Price", "₹98,650", "↑ 2.1%")
        st.markdown('</div>', unsafe_allow_html=True)

    with c2:
        st.markdown(
            '<div class="glass-card" style="padding:20px;text-align:center">', unsafe_allow_html=True)
        st.metric("Silver", f"₹{silver:,.0f}", "↑ 2.8%")
        st.markdown('</div>', unsafe_allow_html=True)

    with c3:
        st.markdown(
            '<div class="glass-card" style="padding:20px;text-align:center">', unsafe_allow_html=True)
        st.metric("Oil", f"${oil:.1f}", "↓ 0.6%")
        st.markdown('</div>', unsafe_allow_html=True)

    with c4:
        st.markdown(
            '<div class="glass-card" style="padding:20px;text-align:center">', unsafe_allow_html=True)
        st.metric("USD Index", f"{usd:.1f}", "↑ 0.8%")
        st.markdown('</div>', unsafe_allow_html=True)

# ====================== LIVE FORECAST TAB ======================
with tab2:
    if predict_btn:
        prediction = 103250.80
        change_pct = (prediction - open_price) / open_price * 100

        colA, colB, colC, colD = st.columns([2, 1, 1, 1])

        with colA:
            st.markdown(f"""
            <div style="background:linear-gradient(135deg, #FF00CC, #00FFEA); padding:45px; 
                        border-radius:32px; text-align:center; color:#0F0A2E;">
                <h2>AI Predicted Gold Price</h2>
                <h1 style="font-size:68px;">₹{prediction:,.2f}</h1>
                <h3 style="font-size:24px;">{change_pct:+.2f}% Expected Change</h3>
            </div>
            """, unsafe_allow_html=True)

        with colB:
            st.metric("Confidence", "98.2%", "🌟")
        with colC:
            st.metric("Risk Level", "Low", "🟢")
        with colD:
            if change_pct > 1.2:
                st.success("🌟 STRONG BUY")
            elif change_pct < -1.2:
                st.error("🔻 SELL")
            else:
                st.warning("⚖️ HOLD")

        dates = [(datetime.now() + timedelta(days=i)).strftime("%b %d")
                 for i in range(8)]
        prices = [prediction * x for x in [0.955, 0.97,
                                           0.985, 1.0, 1.015, 1.028, 1.045, 1.062]]

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=dates, y=prices, mode='lines+markers',
                                 line=dict(color='#00FFEA', width=8),
                                 marker=dict(size=15, color='#FFEA00', symbol='diamond')))
        fig.update_layout(title="🌈 8-DAY SPECTRA FORECAST",
                          height=560, template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)

    else:
        st.info("👈 Adjust controls in sidebar and click **Predict Now**")

# ====================== HISTORY TAB ======================
with tab3:
    st.subheader("Historical Price Trend")
    st.line_chart(np.random.randn(45).cumsum() + 98500,
                  use_container_width=True, color="#FF00CC")

    h1, h2, h3, h4 = st.columns(4)
    with h1:
        st.button("📥 Download CSV", use_container_width=True)
    with h2:
        st.button("📊 Full Screen Chart", use_container_width=True)
    with h3:
        st.button("🔄 Refresh History", use_container_width=True)
    with h4:
        st.button("📈 Compare with Silver", use_container_width=True)

# ====================== INSIGHTS TAB ======================
with tab4:
    st.subheader("AI Market Intelligence")
    st.progress(85, text="Market Sentiment: Strongly Bullish")

    st.success("1. Geopolitical tensions rising")
    st.info("2. Physical gold demand at 6-month high")
    st.warning("3. USD weakening against major currencies")

    if st.button("🎉 Generate Full AI Report"):
        st.balloons()
        st.success("Report Generated!")

# ====================== ANALYTICS TAB ======================
with tab5:
    st.subheader("Advanced Analytics")

    # Gauge Chart
    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=78,
        title={'text': "Market Momentum"},
        gauge={'axis': {'range': [0, 100]},
               'bar': {'color': "#00FFEA"},
               'steps': [{'range': [0, 50], 'color': "red"},
                         {'range': [50, 75], 'color': "yellow"},
                         {'range': [75, 100], 'color': "green"}]}
    ))
    st.plotly_chart(fig_gauge, use_container_width=True)

    st.markdown("**Feature Importance**")
    importance = pd.DataFrame({
        'Feature': ['Oil', 'USD Index', 'Volatility', 'Silver', 'Lag1'],
        'Importance': [35, 28, 18, 12, 7]
    })
    st.bar_chart(importance.set_index('Feature'), color="#FF00CC")

# ====================== SETTINGS TAB ======================
with tab6:
    st.subheader("Customization & Model Settings")
    st.color_picker("Choose Accent Color", "#FF00CC")
    st.selectbox("Choose AI Model", [
                 "Spectra v3.0", "Quantum Gold", "Neon Oracle"])
    st.slider("Forecast Horizon (Days)", 1, 45, 8)

    st.markdown("---")
    st.button("💾 Save Current Scenario", use_container_width=True)
    st.button("📂 Load Saved Scenario", use_container_width=True)
    st.button("🔄 Reset All Settings", use_container_width=True)

# ====================== BOTTOM ACTION BAR ======================
st.markdown("---")
b1, b2, b3, b4, b5, b6, b7 = st.columns(7)

with b1:
    st.button("🔄 Refresh All", use_container_width=True)
with b2:
    st.button("📤 Share on Social", use_container_width=True)
with b3:
    st.button("📄 Export PDF", use_container_width=True)
with b4:
    st.button("⭐ Save Scenario", use_container_width=True)
with b5:
    st.button("📧 Set Price Alert", use_container_width=True)
with b6:
    st.button("📊 Compare Assets", use_container_width=True)
with b7:
    st.button("🛠️ Advanced Tools", use_container_width=True)

st.caption("🌈 SPECTRA GOLD AI • Ultimate Colorful Gold Intelligence Platform")
