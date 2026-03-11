import ollama

def generate_insight(summary):

    prompt = f"""
    You are a professional data analyst.

    Analyze the dataset summary below and write a clear report.

    Include:

    1. Average values
    2. Highest values
    3. Lowest values
    4. Important trends
    5. Final conclusion

    Dataset Summary:
    {summary}
    """

    response = ollama.generate(
        model="llama3.2:1b",
        prompt=prompt
    )

    return response["response"]