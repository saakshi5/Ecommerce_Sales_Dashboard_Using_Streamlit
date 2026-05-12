import pandas as pd
import os

def load_data():
    base_path = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_path, 'data', 'online_retail.xlsx')
    
    df = pd.read_excel(file_path)

    # Clean column names
    df.columns = df.columns.str.strip().str.replace(' ', '')

    # 🔥 FIX ALL PROBLEMATIC COLUMNS
    df['StockCode'] = df['StockCode'].astype(str)
    
    # Handle both possible names
    if 'Invoice' in df.columns:
        df['Invoice'] = df['Invoice'].astype(str)
    elif 'Invoice' in df.columns:
        df['Invoice'] = df['Invoice'].astype(str)

    # Core processing
    df.dropna(inplace=True)
    df['TotalPrice'] = df['Quantity'] * df['Price']
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['Month'] = df['InvoiceDate'].dt.month

    return df