import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob

# Set Streamlit theme
st.set_page_config(page_title="Kindle Sentiment Analysis", page_icon="📚", layout="wide")
st.markdown("""
<style>
body {
    background-color: #1e1e2f;
    font-family: 'Arial', sans-serif;
    color: #ffffff;
}
h1 {
    color: #ffa500;
    text-align: center;
    font-weight: bold;
}
h2, h3 {
    color: #00c8ff;
    font-weight: bold;
}
.sidebar .sidebar-content {
    background-color: #282c34;
    color: #ffffff;
}
button {
    background-color: #00c8ff;
    border: none;
    color: white;
    padding: 10px 20px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 4px;
}
</style>
""", unsafe_allow_html=True)

# Title and Description
st.title("📚 Kindle Sentiment Analysis")
st.markdown("""
<div style="text-align: center; font-size: 18px;">
This app performs sentiment analysis on Kindle reviews.<br>
Upload your dataset, visualize trends, and analyze custom text.
</div>
---
""", unsafe_allow_html=True)

# Main Section
st.write("Welcome to the **Kindle Sentiment Analysis** app!")
st.markdown("""
- **Upload a dataset** to analyze sentiment trends from a CSV file.
- **Analyze individual text** directly below.
""")
st.image("https://via.placeholder.com/800x400/282c34/ffa500?text=Kindle+Sentiment+Analysis", use_container_width=True)

# Upload Dataset
st.header("📂 Upload Dataset")
uploaded_file = st.file_uploader("📁 Upload a CSV file with Kindle reviews", type="csv")
if uploaded_file:
    # Load data
    data = pd.read_csv(uploaded_file)
    st.write("### 📊 Dataset Preview")
    st.dataframe(data.head())

    # Ensure the necessary column exists
    if 'review' in data.columns:
        # Sentiment Analysis Function
        def analyze_sentiment(text):
            blob = TextBlob(text)
            return blob.sentiment.polarity

        # Apply Sentiment Analysis
        data['sentiment'] = data['review'].apply(analyze_sentiment)

        # Display Sentiment Data
        st.write("### 📈 Sentiment Analysis Results")
        st.dataframe(data[['review', 'sentiment']].head())

        # Visualization
        st.write("### 🎨 Sentiment Distribution")
        fig, ax = plt.subplots()
        sns.set_theme(style="darkgrid")
        sns.histplot(data['sentiment'], bins=20, kde=True, ax=ax, color='cyan')
        ax.set_title('Sentiment Polarity Distribution', fontsize=16, color='#ffa500')
        ax.set_xlabel('Polarity', fontsize=12, color='#00c8ff')
        ax.set_ylabel('Frequency', fontsize=12, color='#00c8ff')
        st.pyplot(fig)
    else:
        st.error("The dataset must contain a 'review' column.")
else:
    st.info("Please upload a CSV file to begin.")

# Custom Text Analysis
st.header("📝 Custom Analysis")
custom_text = st.text_area("Enter text for sentiment analysis")
if custom_text:
    def analyze_sentiment(text):
        blob = TextBlob(text)
        return blob.sentiment.polarity
    
    custom_sentiment = analyze_sentiment(custom_text)
    st.success(f"📊 Sentiment Polarity: {custom_sentiment}")


