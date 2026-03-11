import streamlit as st
import pandas as pd

from data_cleaner import clean_data
from chart_selector import choose_chart
from visualizer import generate_chart
from trend_detector import detect_trend
from insight_agent import generate_insight
from pdf_report import generate_pdf
from ppt_report import create_ppt

st.title("AI Data Analyst Agent")

file = st.file_uploader("Upload CSV Dataset")

if file is not None:

    # Read dataset
    df = pd.read_csv(file)

    st.subheader("Original Data")
    st.dataframe(df)

    # Step 1: Clean Data
    cleaned_df = clean_data(df)

    st.subheader("Cleaned Data")
    st.dataframe(cleaned_df)

    # Step 2: Chart Selection
    chart_type = choose_chart(cleaned_df)

    # Step 3: Visualization
    chart = generate_chart(cleaned_df, chart_type)

    st.subheader("Data Visualization")
    st.image(chart)

    # Step 4: Trend Detection
    trends = detect_trend(cleaned_df)

    st.subheader("Detected Trends")
    st.write(trends)
    # Step 4.5: Highest and Lowest values

    top_values = cleaned_df.max(numeric_only=True)
    low_values = cleaned_df.min(numeric_only=True)

    st.subheader("Highest Values")
    st.write(top_values)

    st.subheader("Lowest Values")
    st.write(low_values)
    # Step 5: AI Insights
    summary = f"""
    Dataset Columns: {list(cleaned_df.columns)}

    Dataset Shape: {cleaned_df.shape}

    Statistics:
    {cleaned_df.describe().to_string()}

    Highest Values:
    {top_values.to_string()}

    Lowest Values:
    {low_values.to_string()}
    """
    insight = generate_insight(summary)

    st.subheader("AI Generated Insights")
    st.write(insight)

    # Step 6: Generate PDF
    pdf = generate_pdf(insight)

    st.download_button(
        label="Download PDF Report",
        data=open(pdf, "rb"),
        file_name="AI_Report.pdf"
    )

    # Step 7: Generate PowerPoint
    ppt = create_ppt(insight)

    st.download_button(
        label="Download PowerPoint Report",
        data=open(ppt, "rb"),
        file_name="AI_Report.pptx"
    )