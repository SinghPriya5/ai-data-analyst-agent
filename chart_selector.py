def choose_chart(df):

    numeric_cols = df.select_dtypes(include=['int','float']).columns

    if len(numeric_cols) >= 3:
        return "correlation"

    elif len(numeric_cols) == 2:
        return "scatter"

    else:
        return "bar"