# my_functions.py
import pandas as pd

## Agg functions
def agg_by_data_type(df, column_name):
    # Check if the column is numeric
    if df[column_name].dtypes in ('int64', 'float64'):
        # Perform operation for numeric columns
        return df[column_name].mean()  # take the mean value for numeric variation
    else:
        # Perform operation for non-numeric columns
        return df[column_name].iloc[0]  # Select the first value

def livea_agg(df):
    col_names = list(df.columns)
    results = {}
    for col in col_names:
        # Drop NaN values
        df_dropped = df.dropna(subset = [col])

        # Filter rows where 'livea_match_cd' is "E"
        filtered_rows = df_dropped[df_dropped['livea_match_cd'] == 'E']
        
        # If there are any such rows let's use them
        if len(filtered_rows) > 0:
            results[col] = agg_by_data_type(filtered_rows, col)
        elif len(df_dropped) > 0:
            results[col] = agg_by_data_type(df_dropped, col)
        else:
            results[col] = None
    return pd.Series(results)

def apply_livea_agg(df):
    return df.groupby(["cust_email_addr", "year"]).apply(livea_agg)