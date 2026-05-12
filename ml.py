import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def customer_segmentation(df):

    # ================= CLEAN DATA =================

    # Remove negative quantities (VERY IMPORTANT)
    df = df[df['Quantity'] > 0]

    # Remove missing CustomerID
    df = df.dropna(subset=['CustomerID'])

    # ================= CREATE CUSTOMER DATA =================

    customer_df = df.groupby('CustomerID').agg({
        'TotalPrice': 'sum',
        'Invoice': 'nunique',
        'Quantity': 'sum'
    }).reset_index()

    customer_df.columns = ['CustomerID', 'TotalSpend', 'Orders', 'Quantity']

    # Extra safety cleanup
    customer_df = customer_df[customer_df['Quantity'] > 0]

    # ================= SCALING =================

    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(
        customer_df[['TotalSpend', 'Orders', 'Quantity']]
    )

    # ================= K-MEANS MODEL =================

    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    customer_df['Cluster'] = kmeans.fit_predict(scaled_data)

    return customer_df