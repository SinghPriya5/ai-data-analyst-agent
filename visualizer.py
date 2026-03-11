import matplotlib.pyplot as plt
import seaborn as sns

def generate_chart(df, chart_type):

    plt.figure(figsize=(8,5))

    if chart_type == "bar":

        df.mean(numeric_only=True).plot(kind="bar")

    elif chart_type == "scatter":

        cols = df.select_dtypes(include=['int','float']).columns

        plt.scatter(df[cols[0]], df[cols[1]])

    elif chart_type == "correlation":

        sns.heatmap(df.corr(numeric_only=True), annot=True)

    plt.title("AI Data Visualization")

    plt.savefig("chart.png")

    return "chart.png"