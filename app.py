import streamlit as st
import plotly.express as px
from core import load_data,kpis

st.set_page_config(page_title="Enterprise ACV Intelligence",layout="wide")
st.title("Enterprise ACV & Revenue Intelligence")
st.caption("Synthetic demonstration of recurring-revenue semantic modeling and executive analytics.")
df=load_data()
regs=st.sidebar.multiselect("Region",sorted(df.region.unique()),default=sorted(df.region.unique()))
prods=st.sidebar.multiselect("Product",sorted(df.product_suite.unique()),default=sorted(df.product_suite.unique()))
f=df[df.region.isin(regs)&df.product_suite.isin(prods)]
m=kpis(f)
cols=st.columns(5)
cols[0].metric("Starting ACV",f"${m['starting_acv']/1e6:,.1f}M")
cols[1].metric("Ending ACV",f"${m['ending_acv']/1e6:,.1f}M")
cols[2].metric("Net ACV Change",f"${m['net_change']/1e6:,.1f}M",f"{m['growth_rate']:+.1%}")
cols[3].metric("Expiring ACV",f"${m['expiring_acv']/1e6:,.1f}M")
cols[4].metric("Customers",f"{m['customers']:,}")
byreg=f.groupby("region",as_index=False)[["starting_acv","ending_acv","bookings"]].sum()
st.plotly_chart(px.bar(byreg,x="region",y=["starting_acv","ending_acv"],barmode="group",title="ACV by region"),use_container_width=True)
moves=f.groupby("movement",as_index=False)["starting_acv"].sum()
st.plotly_chart(px.pie(moves,names="movement",values="starting_acv",title="Recurring revenue movement mix"),use_container_width=True)
st.subheader("Customer-level movement")
st.dataframe(f.sort_values("starting_acv",ascending=False),use_container_width=True)
