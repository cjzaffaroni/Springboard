import pandas as pd
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns

# Setup Seaborn
sns.set_style("whitegrid")
sns.set_context("poster")

df_offers = pd.read_excel("./WineKMC.xlsx", sheet_name=0)

df_offers.columns = ["offer_id", "campaign", "varietal", "min_qty", "discount", "origin", "past_peak"]

df_transactions = pd.read_excel("./WineKMC.xlsx", sheet_name=1)
df_transactions.columns = ["customer_name", "offer_id"]
df_transactions['n'] = 1

# Think about calling merge() on df_transactions and df_offers
merged = pd.merge(df_transactions, df_offers)

# We now want to make a pivot table
pivoted = merged.pivot_table(index='customer_name', columns='offer_id', values='n', fill_value=0)

from sklearn.cluster import KMeans
import numpy as np

# Make an empty list
ss = []

# Make an empty dictionary called assignments
assignments = {}

# Cast your table 'pivoted' as a matrix with to_numpy(), and store it in a variable X
X = pivoted.to_numpy()

model = KMeans(n_clusters= 3)

model.fit(X)

assigned_cluster = model.predict(X)

print(assigned_cluster)