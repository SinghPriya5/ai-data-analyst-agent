def detect_trend(df):

    numeric = df.select_dtypes(include=['int','float'])

    trends = {}

    for col in numeric.columns:

        trends[col] = {
            "mean": numeric[col].mean(),
            "max": numeric[col].max(),
            "min": numeric[col].min()
        }

    return trends