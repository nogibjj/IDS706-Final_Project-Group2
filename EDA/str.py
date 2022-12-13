# %%
# import the packages needed for streamlit
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
from PIL import Image


# %%
# import the packages needed for the model
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import roc_curve, roc_auc_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_recall_curve

# %%
# start to build the streamlit app
st.title("Credit Card Fraud Detection")
st.write(
    "We are going to detect credit card fraud by using machine learning algorithms."
)
st.write("The dataset is from Kaggle: https://www.kaggle.com/mlg-ulb/creditcardfraud")
st.write(
    "The model is trained by using the training dataset, and the model is tested by using the testing dataset."
)
# image = Image.open(
#     "https://raw.githubusercontent.com/belladu0201/Images_Beibei/044a7c9aa4a1d2f6711fcdcef9cb19f1078927e8/111.png"
# )
# st.image(image)
# read the dataset
@st.cache
def load_data():
    df = pd.read_csv("./Training cleaned/Daily_train_cleaned.csv")
    return df


df = load_data()

st.subheader("Dataset Overview")
st.write(df)

# # show the dataset description
# st.subheader("Dataset Description")
# st.write(df.describe())

# show the dataset shape
# st.subheader("Dataset Shape")
# st.write(df.shape)

# show the dataset columns
# st.subheader("Dataset Columns")
# st.write(df.columns)

# sns.distplot(df["Daily transactions Count"])
# # put the plot into streamlit
# st.pyplot()

st.subheader("Dataset Correlation")
st.write(df.corr())


# show the dataset correlation heatmap
# st.subheader("Dataset Correlation Heatmap")
# sns.heatmap(df.corr(), annot=True)
# st.pyplot()


st.subheader(
    "Linear Regression to see the correlation between the columns and Daily transactions Count"
)
st.write("Please input the column name you want to see the linear regression.")

lst = [
    "Daily transactions amount",
    "Daily Fraudulent Transactions",
    "Daily Fraudulent amount",
]
user_input = st.selectbox("Select a category:", lst)
if user_input:
    chart = (
        alt.Chart(df)
        .mark_circle()
        .encode(x=user_input, y="Daily transactions Count")
        .properties(width=800, height=600)
    )
    t = chart.transform_regression(user_input, "Daily transactions Count").mark_line(
        color="red"
    )
    st.altair_chart(chart + t)

st.subheader("Boxplot of Fraud Count by Category")
st.write("Please input the column category to see the Fraud Count.")
df2 = pd.read_csv("./Training cleaned/agg_daily_category_train_cleaned.csv")
category = st.selectbox("Select a category:", df2["category"].unique())

df3 = df2[df2["category"] == category]

brush = alt.selection(type="interval")
chart = (
    alt.Chart(df3)
    .mark_boxplot()
    .encode(x="category", y="Fraud count")
    .properties(selection=brush, width=800, height=600)
)
st.altair_chart(chart)


df4 = pd.read_csv("./Training cleaned/agg_daily_state_train_cleaned.csv")
# provide a user input to select state to see the daily transaction count
st.subheader("Daily transaction count by state")
st.write("Please input the state name you want to see the daily transaction count.")

# get the user input
lst = [
    "CA",
    "TX",
    "FL",
    "NY",
    "IL",
    "PA",
    "OH",
    "GA",
    "NC",
    "MI",
    "NJ",
    "VA",
    "WA",
    "AZ",
    "MA",
    "TN",
    "IN",
    "MO",
    "MD",
    "WI",
    "CO",
    "MN",
    "AL",
    "SC",
    "LA",
    "KY",
    "OR",
    "OK",
    "CT",
    "UT",
    "IA",
    "NV",
    "AR",
    "MS",
    "KS",
    "NM",
    "NE",
    "WV",
    "ID",
    "HI",
    "NH",
    "ME",
    "RI",
    "MT",
    "DE",
    "SD",
    "ND",
    "AK",
    "DC",
    "VT",
    "WY",
]
user_input = st.selectbox("Select a state:", lst)
temp = df4[df4["state"] == user_input]
st.write(temp.head())
if user_input:
    chart = (
        alt.Chart(temp)
        .mark_point()
        .encode(
            y="transactions amount",
            x="Fraud count per state",
            tooltip=["state", "Date"],
        )
        .properties(width=800, height=600)
    )
    t = chart.transform_regression(
        "Fraud count per state", "transactions amount"
    ).mark_line(color="red")
    st.altair_chart(chart + t)

st.write("The state-wise fraud amount in a descending order:")
st.write(
    df4.groupby("state").sum().sort_values(by="Fraud amount per state", ascending=False)
)
# %%
