import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Employee Attrition Dashboard",
    page_icon="📊",
    layout="wide"
)

df = pd.read_csv("Palo Alto Networks.csv")

st.title("📊 Employee Attrition Analysis Dashboard")
st.write("Workforce Attrition Patterns and Risk Hotspot Analysis")

total = len(df)
left = (df["Attrition"] == 1).sum()
rate = round((left / total) * 100, 2)

col1, col2, col3 = st.columns(3)

col1.metric("Total Employees", total)
col2.metric("Employees Who Left", left)
col3.metric("Attrition Rate", f"{rate}%")

st.header("Department-wise Attrition")

dept = df.groupby("Department")["Attrition"].agg(
    Total_Employees="count",
    Employees_Left="sum"
)

dept["Attrition_Rate"] = (
    dept["Employees_Left"] / dept["Total_Employees"] * 100
).round(2)

st.dataframe(dept)
st.bar_chart(dept["Attrition_Rate"])

st.header("Job Role-wise Attrition")
role = df.groupby("JobRole")["Attrition"].mean() * 100
st.bar_chart(role)

st.header("Age-wise Attrition")
age = df.groupby("Age")["Attrition"].mean() * 100
st.line_chart(age)

st.header("Overtime Analysis")
overtime = df.groupby("OverTime")["Attrition"].mean() * 100
st.bar_chart(overtime)

st.header("Work-Life Balance Analysis")
balance = df.groupby("WorkLifeBalance")["Attrition"].mean() * 100
st.bar_chart(balance)

st.success("Dashboard loaded successfully!")
