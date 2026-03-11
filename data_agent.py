import ollama

def generate_insights(summary):

    prompt = f"""
    You are a senior data analyst.

    Analyze the dataset summary below and provide a clear report.

    Dataset Summary:
    {summary}
    

    Write insights in simple language including:

    1. Average performance
    2. Highest values
    3. Lowest values
    4. Important trends
    5. Final conclusion

    Write the report like a professional data analysis report.
    """

    response = ollama.generate(
        model="llama3.2:1b",
        prompt=prompt
    )

    return response["response"]