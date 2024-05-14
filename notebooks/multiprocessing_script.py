import multiprocessing
import pandas as pd
from my_function import livea_agg

def worker(df):
    return livea_agg(df)

def main(df_list):
    with multiprocessing.Pool() as pool:
        results = pool.map(worker, df_list)
    return pd.concat(results, ignore_index=True)