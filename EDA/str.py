# %%
# import the packages needed for streamlit
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# %%
# import the packages needed for the model
from sklearn.model_selection import train_test_split
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
st.write("The model is built by using Logistic Regression.")
st.write(
    "The model is trained by using the training dataset, and the model is tested by using the testing dataset."
)
st.write("The model is evaluated by using the testing dataset.")
st.write("The model is deployed by using streamlit.")

# read the dataset
df = pd.read_csv("./Training cleaned/Daily_train_cleaned.csv")

# show the dataset
st.subheader("Dataset")
st.write(df)

# show the dataset description
st.subheader("Dataset Description")
st.write(df.describe())

# show the dataset shape
st.subheader("Dataset Shape")
st.write(df.shape)

# show the dataset columns
st.subheader("Dataset Columns")
st.write(df.columns)

sns.distplot(df["Daily transactions Count"])
# put the plot into streamlit
st.pyplot()

# show the dataset correlation
st.subheader("Dataset Correlation")
st.write(df.corr())


# show the dataset correlation heatmap
st.subheader("Dataset Correlation Heatmap")
sns.heatmap(df.corr(), annot=True)
st.pyplot()


# plot the dataset correlation heatmap with user input
st.subheader("Dataset Correlation Heatmap with User Input")
st.write("Please input the column name you want to see the correlation heatmap.")
st.write(
    'For example, you can input "Daily transactions Count" to see the correlation heatmap of "Daily transactions Count".'
)
st.write(
    'You can also input "Daily transactions Amount" to see the correlation heatmap of "Daily transactions Amount".'
)
st.write(
    'You can also input "Daily transactions Count" and "Daily transactions Amount" to see the correlation heatmap of "Daily transactions Count" and "Daily transactions Amount".'
)

# get the user input
user_input = st.text_input(
    "Please input the column name you want to see the correlation heatmap."
)

# plot the dataset correlation heatmap with user input
if user_input:
    sns.heatmap(df[user_input].corr(), annot=True)
    st.pyplot()


# show the dataset correlation heatmap with user input
st.subheader("Dataset Correlation with User Input")
st.write("Please input the column name you want to see the correlation.")
st.write(
    'For example, you can input "Daily transactions Count" to see the correlation of "Daily transactions Count".'
)
st.write(
    'You can also input "Daily transactions Amount" to see the correlation of "Daily transactions Amount".'
)

# %%
