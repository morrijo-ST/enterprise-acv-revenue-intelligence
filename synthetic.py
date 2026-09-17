import numpy as np
import pandas as pd

def generate_acv_data(seed=42,n_customers=400):
    rng=np.random.default_rng(seed)
    regions=["North America","Europe","Asia Pacific","Middle East & Africa"]
    products=["Core","Analytics","Operations","Optimization"]
    rows=[]
    for i in range(1,n_customers+1):
        c=f"CUST-{i:04d}"; reg=rng.choice(regions,p=[.42,.25,.22,.11]); prod=rng.choice(products)
        start=float(rng.uniform(25000,450000))
        move=rng.choice(["renew_flat","expansion","contraction","churn"],p=[.58,.20,.14,.08])
        if move=="renew_flat": end=start*rng.normal(1,.015)
        elif move=="expansion": end=start*rng.uniform(1.08,1.45)
        elif move=="contraction": end=start*rng.uniform(.55,.92)
        else: end=0
        booking=max(end-start,0)+rng.uniform(0,50000); expiring=start*rng.uniform(.2,1.0)
        term=int(rng.choice([12,24,36]))
        rows.append([c,reg,prod,start,end,booking,expiring,term,move])
    return pd.DataFrame(rows,columns=["customer_id","region","product_suite","starting_acv","ending_acv","bookings","expiring_acv","contract_term_months","movement"])
