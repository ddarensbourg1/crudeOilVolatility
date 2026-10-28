import stremlit as st
import pandas as pd
import numpy as np

st.set_page_config(
  page_title="Crude Oil Volatility Forecaster",
  layout="wide")
st.title("Sentiment-Driven Crude Oil Volatility Forecaster")
st.markdown("AI-powered predictions for next-day crude oil market turbulance.")

st.sidebar.header("Dashboard Controls")
selected_view = st.sidebar.selectbox("Select Module", ["Live Forecaster & Overview" , "Sentiment Analysis", "Model Explainability(SHAP)", "Backtest Results"])
date_range = st.sidebar.date_input("Select Date Range", [])

st.subheader("Next-Day Market Outlook")
col1, col2, col3, col4, = st.columns(4)
with col1:
  st.metric(label="Predicted Volatility Direction", value="--", delta="Pending Model") #-- is a place holder for backend data
with col2:
  st.metric(label="Current OVX Index", value="--",delta="--")
with col3:
  st.metric(label="Daily Sentiment Score",value="-- / 1.0", delta="Neutral")
with col4:
  st.metric(label="Model Accuracy Target", value=">= 55.0%, delta="Backtest")
st.divider()

chart_col, info_col = st.colums([2,1])

with chart_col:
  st.subheader("Market Trends & Sentiment Heatmap")
  st.info("Plotly charts comparing WIT/OVX prices with new sentiment will render here")
  chart_data = pd.DataFrame(np.random.random(20,2), columns =['Oil Price Trend', 'Sentiment Trend'])
#ready for future plotly chart
  st.line_chart(chart_data)     

  with info_col:
    st.subheader("Key Drivers")
    st.write("Top influencing factors from recent GDELT headlines and economic data feeds.")
    st.caption("Awaiting feature pipeline intergration...")

  st.divider()

  st.subheader("XGBooth & SHAP Explainibility Placeholders")
  model_container = st.container(boarder=True)
  with model_container:
    st.warning("Model inference and SHAP feature attribution plots are under development(Phase6-7)")
    st.code("#TODO: Integrate XGBoost prediction output and SHAP waterfall plots here", language="python")
    
