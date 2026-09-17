import pandas as pd
from synthetic import generate_acv_data

def load_data(path=None):
    df=generate_acv_data() if path is None else pd.read_csv(path)
    df["acv_change"]=df["ending_acv"]-df["starting_acv"]
    df["acv_change_pct"]=df["acv_change"]/df["starting_acv"].replace(0,pd.NA)
    return df

def kpis(df):
    start=df.starting_acv.sum()
    end=df.ending_acv.sum()
    exp=df.expiring_acv.sum()
    return {
        "starting_acv": start,
        "ending_acv": end,
        "net_change": end-start,
        "growth_rate": (end-start)/start if start else 0,
        "expiring_acv": exp,
        "customers": df.customer_id.nunique(),
    }
