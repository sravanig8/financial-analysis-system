"""
Professional Financial Intelligence Dashboard
Multi-Agent AI System for Stock Analysis

Run with: streamlit run app.py
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import os
from datetime import datetime

# Import agents
from agents.market_agent import get_market_data
from agents.news_agent import get_news
from agents.sentiment_agent import analyze_sentiment
from agents.analysis_agent import analyze_trend
from agents.report_agent import generate_financial_report


# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="Financial AI Dashboard",
    layout="wide",
    page_icon="📊",
    initial_sidebar_state="expanded"
)

# Professional CSS styling
st.markdown("""
    <style>
    /* Main container */
    .main {
        padding: 2rem;
    }
    
    /* KPI styling */
    .kpi-container {
        padding: 1.5rem;
        border-radius: 10px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Headline box */
    .headline-box {
        padding: 1rem;
        border-left: 4px solid #667eea;
        background-color: #f8f9fa;
        border-radius: 5px;
        margin: 0.5rem 0;
    }
    
    /* Section header */
    .section-header {
        font-size: 1.5rem;
        font-weight: bold;
        color: #1f77b4;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def create_price_chart(historical_data, symbol="Stock"):
    """
    Create an interactive Plotly price chart.
    
    Args:
        historical_data: List of closing prices
        symbol: Stock symbol for title
    
    Returns:
        plotly Figure object
    """
    if not historical_data or len(historical_data) == 0:
        return None
    
    # Create dataframe with dates
    dates = pd.date_range(end=datetime.now(), periods=len(historical_data), freq='D')
    df = pd.DataFrame({
        'Date': dates,
        'Price': historical_data
    })
    
    # Create Plotly figure
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=df['Date'],
        y=df['Price'],
        mode='lines+markers',
        name='Stock Price',
        line=dict(color='#667eea', width=2),
        fill='tozeroy',
        fillcolor='rgba(102, 126, 234, 0.1)',
        hovertemplate='<b>%{x|%B %d}</b><br>Price: $%{y:.2f}<extra></extra>'
    ))
    
    fig.update_layout(
        title=f'📈 {symbol} - 30-Day Price Movement',
        title_font_size=16,
        xaxis_title='Date',
        yaxis_title='Price ($)',
        hovermode='x unified',
        template='plotly_white',
        height=400,
        margin=dict(l=0, r=0, t=40, b=0),
        showlegend=False,
        font=dict(size=11)
    )
    
    return fig


def display_headline(headline, sentiment_score=None):
    """
    Display a headline in a styled box.
    
    Args:
        headline: Headline text
        sentiment_score: Optional sentiment score
    """
    # Emoji based on sentiment
    if sentiment_score is not None:
        emoji = "📈" if sentiment_score > 0.1 else "📉" if sentiment_score < -0.1 else "📊"
    else:
        emoji = "📰"
    
    st.markdown(
        f"""
        <div class="headline-box">
        <b>{emoji} {headline}</b>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================================
# MAIN APPLICATION
# ============================================================================

def main():
    """Main Streamlit application."""
    
    # ========================================================================
    # HEADER
    # ========================================================================
    
    st.title("📊 Multi-Agent Financial Intelligence Dashboard")
    st.markdown("*Real-time stock analysis using AI agents*")
    st.markdown("---")
    
    # ========================================================================
    # SIDEBAR CONTROLS
    # ========================================================================
    
    with st.sidebar:
        st.header("🎛️ Stock Controls")
        
        # Stock symbol input
        stock_symbol = st.text_input(
            "Stock Symbol",
            value="AAPL",
            placeholder="Enter symbol (e.g., AAPL, TSLA, MSFT)",
            help="Enter a valid stock ticker"
        ).upper().strip()
        
        # Buttons
        col1, col2 = st.columns(2)
        with col1:
            analyze_button = st.button(
                "▶️ Run Analysis",
                width='stretch',
                type="primary"
            )
        
        with col2:
            st.button(
                "Clear Cache",
                width='stretch',
                on_click=lambda: st.cache_data.clear()
            )
        
        st.divider()
        
        # API Status
        st.markdown("### 📌 System Status")
        
        # Try to get API keys from Streamlit secrets first, then environment variables
        try:
            gemini_key = st.secrets.get("GEMINI_API_KEY", os.environ.get('GEMINI_API_KEY'))
            gnews_key = st.secrets.get("GNEWS_API_KEY", os.environ.get('GNEWS_API_KEY'))
        except:
            gemini_key = os.environ.get('GEMINI_API_KEY')
            gnews_key = os.environ.get('GNEWS_API_KEY')
        
        if gemini_key:
            st.success("✅ Gemini API: Ready")
        else:
            st.error("❌ Gemini API: Not found")
        
        if gnews_key and gnews_key != "your-gnews-api-key":
            st.success("✅ GNEWS API: Ready")
        else:
            st.info("ℹ️ GNEWS API: Using samples")
        
        st.divider()
        
        # About
        st.markdown("### 🤖 Multi-Agent System")
        st.markdown("""
        1. **📈 Market Agent** - Real-time prices
        2. **📰 News Agent** - Headlines
        3. **😊 Sentiment Agent** - Analysis
        4. **📊 Analysis Agent** - Trends
        5. **🧠 Report Agent** - AI insights
        """)
        
        st.markdown("---")
        st.markdown("*Powered by Multi-Agent AI*")
    
    # ========================================================================
    # MAIN CONTENT
    # ========================================================================
    
    if analyze_button:
        if not stock_symbol:
            st.error("❌ Please enter a valid stock symbol.")
            return
        
        # Perform analysis with spinner
        with st.spinner("🔄 Analyzing stock using AI agents..."):
            
            # Fetch market data
            price, historical_data = get_market_data(stock_symbol)
            
            if price is None:
                st.error(f"❌ Invalid stock symbol: {stock_symbol}")
                st.info("💡 Make sure the symbol is correct (e.g., AAPL, MSFT, TSLA)")
                return
            
            # Fetch news
            headlines = get_news(stock_symbol)
            if not headlines:
                st.warning("⚠️ No headlines found. Continuing...")
                headlines = ["Latest stock news", "Market update"]
            
            # Analyze sentiment
            sentiment_result = analyze_sentiment(headlines)
            if sentiment_result.get('error'):
                sentiment_label = "Neutral"
                sentiment_score = 0.0
                individual_scores = []
            else:
                sentiment_label = sentiment_result.get('sentiment_label', 'Neutral')
                sentiment_score = sentiment_result.get('sentiment_score', 0.0)
                individual_scores = sentiment_result.get('individual_scores', [])
            
            # Analyze trends
            trend, short_ma, long_ma = analyze_trend(historical_data)
            if trend is None:
                st.error("❌ Error analyzing trend.")
                return
            
            # Generate report
            report = generate_financial_report(
                symbol=stock_symbol,
                price=price,
                trend=trend,
                sentiment_label=sentiment_label,
                sentiment_score=sentiment_score,
                headlines=headlines[:5]
            )
            
            if report.get('error'):
                st.error(f"❌ Error generating report: {report.get('message')}")
                st.info("💡 Check your GEMINI_API_KEY setting.")
                return
        
        # Success message
        st.success("✅ Analysis Complete!")
        st.markdown("---")
        
        # ====================================================================
        # KPI CARDS
        # ====================================================================
        
        st.markdown("### 📊 Key Metrics")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                label="💰 Current Price",
                value=f"${price:.2f}",
                delta=None
            )
        
        with col2:
            trend_emoji = "🟢" if trend == "Bullish" else "🔴" if trend == "Bearish" else "🟡"
            st.metric(
                label="📈 Market Trend",
                value=f"{trend_emoji} {trend}",
                delta=None
            )
        
        with col3:
            sentiment_emoji = "🟢" if sentiment_label == "Positive" else "🔴" if sentiment_label == "Negative" else "🟡"
            st.metric(
                label="😊 Sentiment",
                value=f"{sentiment_emoji} {sentiment_label}",
                delta=f"Score: {sentiment_score:.3f}"
            )
        
        st.markdown("---")
        
        # ====================================================================
        # CHARTS & HEADLINES
        # ====================================================================
        
        st.markdown("### 📈 Market Analysis")
        
        col_chart, col_headlines = st.columns([0.70, 0.30])
        
        # Price chart
        with col_chart:
            price_fig = create_price_chart(historical_data, stock_symbol)
            if price_fig:
                st.plotly_chart(price_fig, width='stretch')
        
        # Headlines
        with col_headlines:
            st.markdown("### 📰 Top Headlines")
            
            if individual_scores:
                for item in individual_scores[:5]:
                    headline = item.get('headline', '')
                    score = item.get('score', 0)
                    display_headline(headline, score)
            else:
                for headline in headlines[:5]:
                    display_headline(headline)
        
        st.markdown("---")
        
        # ====================================================================
        # AI INSIGHTS
        # ====================================================================
        
        st.markdown("### 🧠 AI Financial Insights")
        
        with st.expander("📄 View Detailed Report", expanded=True):
            
            # Insights
            if report.get('insights'):
                st.markdown("#### 📌 Key Insights")
                st.markdown(report.get('insights'))
                st.markdown("")
            
            # Recommendation with colors
            if report.get('recommendation'):
                st.markdown("#### 💡 Investment Recommendation")
                recommendation_text = report.get('recommendation', '')
                
                if "BUY" in recommendation_text.upper():
                    st.success(recommendation_text)
                elif "SELL" in recommendation_text.upper():
                    st.error(recommendation_text)
                else:
                    st.info(recommendation_text)
                
                st.markdown("")
            
            # Summary
            if report.get('summary'):
                st.markdown("#### 📋 Executive Summary")
                st.markdown(report.get('summary'))
        
        st.markdown("---")
        
        # ====================================================================
        # TECHNICAL DETAILS
        # ====================================================================
        
        with st.expander("📊 Technical Details", expanded=False):
            col_tech1, col_tech2, col_tech3 = st.columns(3)
            
            with col_tech1:
                if short_ma:
                    st.metric("7-Day MA", f"${short_ma:.2f}")
            
            with col_tech2:
                if long_ma:
                    st.metric("30-Day MA", f"${long_ma:.2f}")
            
            with col_tech3:
                if historical_data:
                    change = ((historical_data[-1] - historical_data[0]) / historical_data[0]) * 100
                    st.metric("30-Day Change", f"{change:.2f}%")
            
            st.markdown("")
            st.markdown("#### Full Report Text")
            st.text_area(
                "Complete Analysis",
                value=report.get('full_report', 'No report available'),
                height=200,
                disabled=True
            )
        
        st.markdown("---")
        st.caption(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    else:
        # Welcome screen
        col_welcome, col_info = st.columns([0.6, 0.4])
        
        with col_welcome:
            st.markdown("""
            ### 👋 Welcome to Financial Intelligence Dashboard
            
            **What You Can Do:**
            
            🔍 **Real-Time Analysis**
            - Fetch current stock prices
            - View 30-day historical trends
            
            📰 **News Integration**
            - Real headlines from GNEWS API
            - Automatic sentiment analysis
            
            🧠 **AI-Powered Insights**
            - Gemini AI generates professional analysis
            - Buy/Hold/Sell recommendations
            
            📊 **Interactive Visualizations**
            - Professional price charts
            - Color-coded metrics
            - Technical indicators
            
            ### 🚀 Get Started
            
            1. Enter a stock symbol in the sidebar
            2. Click "▶️ Run Analysis"
            3. View comprehensive results
            """)
        
        with col_info:
            st.info("""
            ### 📌 Example Symbols
            
            **Tech:**
            - AAPL (Apple)
            - MSFT (Microsoft)
            - GOOGL (Google)
            - TSLA (Tesla)
            
            **Finance:**
            - JPM (JPMorgan)
            - GS (Goldman Sachs)
            
            **India:**
            - INFY (Infosys)
            - TCS.NS
            - RELIANCE.NS
            """)


# ============================================================================
# RUN APPLICATION
# ============================================================================

if __name__ == '__main__':
    main()
