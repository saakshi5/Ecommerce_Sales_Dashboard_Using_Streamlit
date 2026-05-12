from ml import customer_segmentation
import streamlit as st
import pandas as pd
import plotly.express as px
import os

# ================= PAGE CONFIG =================
st.set_page_config(page_title="Ecommerce Dashboard", layout="wide")

# ================= UI =================
st.markdown("""
<style>
            
/* ================= SIDEBAR TOGGLE BUTTON ================= */

/* FORCE sidebar toggle visibility */
button[data-testid="baseButton-header"] svg {
    fill: white !important;
    color: white !important;
}

/* fallback for newer versions */
[data-testid="stAppViewContainer"] header svg {
    color: white !important;
}

/* Ensure visibility on dark header */
header[data-testid="stHeader"] {
    background: transparent !important;
}
            
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #1e293b, #0f172a);
    color: white;
}

[data-testid="stSidebar"] {
    background: #111827;
}

/* Sidebar text (keep white) */
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: white !important;
}

/* ONLY input fields text black */
[data-testid="stSidebar"] input,
[data-testid="stSidebar"] textarea {
    color: black !important;
    background-color: white !important;
}

/* Multiselect selected values (placeholder area) */
[data-baseweb="select"] span {
    color: black !important;
}

/* Dropdown menu options */
[data-baseweb="menu"] div {
    color: black !important;
}

/* Fix calendar popup */
[data-baseweb="input"] input {
    color: black !important;
}

/* Remove red border / error highlight */
[data-baseweb="select"] div {
    border: none !important;
    box-shadow: none !important;
}

/* Main headings */
h1, h2, h3 {
    color: #facc15;
}

/* KPI */
.kpi {
    background: linear-gradient(135deg, #2563eb, #9333ea);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    color: white;
}

/* Charts */
.chart-box {
    background: #1f2937;
    padding: 15px;
    border-radius: 15px;
    margin-bottom: 20px;
}
            
            /* ML section box */
.ml-box {
    background: #0f172a;
    padding: 20px;
    border-radius: 15px;
    margin-top: 20px;
    border: 1px solid #334155;
}
            
</style>
""", unsafe_allow_html=True)

# ================= TITLE =================
st.title("📊 E-Commerce Sales Dashboard")

# ================= LOAD DATA =================
@st.cache_data
def load_data():
    base_path = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_path, 'data', 'online_retail.xlsx')

    df = pd.read_excel(file_path)
    df.columns = df.columns.str.strip().str.replace(' ', '')

    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce')
    df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

    df['TotalPrice'] = df['Quantity'] * df['Price']
    df['Month'] = df['InvoiceDate'].dt.to_period('M').astype(str)

    df.dropna(inplace=True)
    return df

# ================= SIDEBAR =================
df = load_data()
st.sidebar.markdown("## 🎛️ Filters")

countries = st.sidebar.multiselect(
    "🌍 Country",
    df['Country'].unique(),
    default=df['Country'].unique()
)

# ================= PRODUCT FILTER =================
product_list = sorted(df['Description'].dropna().unique().tolist())

product_options = ["Select All"] + product_list

selected_products = st.sidebar.multiselect(
    "📦 Select Product",
    options=product_options,
    default=["Select All"]
)

if "Select All" in selected_products:
    products = product_list
else:
    products = selected_products
if not products:
    products = df['Description'].unique()

min_date = df['InvoiceDate'].min().date()
max_date = df['InvoiceDate'].max().date()

date_range = st.sidebar.date_input("📅 Date Range", (min_date, max_date))
start_date, end_date = date_range

price_range = st.sidebar.slider(
    "💰 Sales Range",
    float(df['TotalPrice'].min()),
    float(df['TotalPrice'].max()),
    (float(df['TotalPrice'].min()), float(df['TotalPrice'].max()))
)

# ================= FILTER =================
filtered_df = df[
    (df['Country'].isin(countries)) &
    (df['Description'].isin(products)) &   # ✅ ADD THIS
    (df['InvoiceDate'] >= pd.to_datetime(start_date)) &
    (df['InvoiceDate'] <= pd.to_datetime(end_date)) &
    (df['TotalPrice'].between(price_range[0], price_range[1]))
]

if filtered_df.empty:
    st.warning("No data → showing full dataset")
    filtered_df = df.copy()

# ================= KPI =================
st.subheader("📌 Key Metrics")

c1, c2, c3, c4 = st.columns(4)

c1.markdown(f"<div class='kpi'><h3>💰 Sales</h3><h2>${filtered_df['TotalPrice'].sum():,.0f}</h2></div>", unsafe_allow_html=True)
c2.markdown(f"<div class='kpi'><h3>🧾 Orders</h3><h2>{filtered_df['Invoice'].nunique()}</h2></div>", unsafe_allow_html=True)
c3.markdown(f"<div class='kpi'><h3>👥 Customers</h3><h2>{filtered_df['CustomerID'].nunique()}</h2></div>", unsafe_allow_html=True)
c4.markdown(f"<div class='kpi'><h3>📦 Quantity</h3><h2>{int(filtered_df['Quantity'].sum())}</h2></div>", unsafe_allow_html=True)

st.markdown("---")

# ================= CHARTS =================

country_sales = filtered_df.groupby('Country')['TotalPrice'].sum().reset_index()
# 📈 Monthly Sales
monthly = filtered_df.groupby('Month')['TotalPrice'].sum().reset_index()
st.plotly_chart(px.line(monthly, x='Month', y='TotalPrice', title="📈 Monthly Sales"), width="stretch")

# 🥧 Pie Top Countries
top_country = country_sales.sort_values(by='TotalPrice', ascending=False).head(10)
st.plotly_chart(px.pie(top_country, values='TotalPrice', names='Country', title="🌍 Top 10 Countries Sales"), width="stretch")


# 📊 Stacked Bar
stacked = filtered_df.groupby(['Month', 'Country'])['TotalPrice'].sum().reset_index()
st.plotly_chart(px.bar(stacked, x='Month', y='TotalPrice', color='Country', barmode='stack', title="📊 Monthly Country Sales"), width="stretch")

# 📊 Bar: Top Countries Sales
st.plotly_chart(px.bar(top_country, x='Country', y='TotalPrice', title="📊 Sales by Country", color='TotalPrice'), width="stretch")

# 🥧 Pie Top Customers
top_cust = filtered_df.groupby('CustomerID')['TotalPrice'].sum().reset_index().sort_values(by='TotalPrice', ascending=False).head(5)
st.plotly_chart(px.pie(top_cust, values='TotalPrice', names='CustomerID', title="👑 Top 5 Customers"), width="stretch")

# 📊 Bar: Monthly Orders
monthly_orders = (
    filtered_df.groupby('Month')['Invoice']
    .nunique()
    .reset_index()
    .sort_values(by='Invoice')   # 👈 ascending order
)

fig = px.bar(
    monthly_orders,
    x='Month',
    y='Invoice',
    title="🧾 Monthly Orders",
    color='Invoice',          # 👈 Adds color
    color_continuous_scale='viridis'  # 👈 Nice gradient
)
st.plotly_chart(fig, width="stretch")


# 🍩 Donut Chart

st.plotly_chart(px.pie(country_sales, values='TotalPrice', names='Country', hole=0.5, title="🍩 Sales Distribution"), width="stretch")

# 📊 Bar: Quantity by Country
qty_country = filtered_df.groupby('Country')['Quantity'].sum().reset_index().sort_values(by='Quantity', ascending=False).head(10)
st.plotly_chart(px.bar(qty_country, x='Country', y='Quantity', title="📦 Quantity by Country"), width="stretch")


# ================= ML SECTION =================

from ml import customer_segmentation

st.markdown("---")
st.subheader("🤖 Customer Segmentation (Machine Learning)")

# Run ML model
customer_df = customer_segmentation(filtered_df)

# 🔥 ADD THIS HERE (IMPORTANT)
customer_df['Cluster'] = customer_df['Cluster'].map({
    0: "Low Value Customers",
    1: "Medium Value Customers",
    2: "High Value Customers (VIP)"
})

# Remove nulls just in case
customer_df = customer_df.dropna()

region_df = filtered_df.groupby('Country')['CustomerID'].nunique().reset_index()
region_df.columns = ['Country', 'Customers']

fig_region = px.bar(
    region_df.sort_values(by='Customers', ascending=False).head(10),
    x='Country',
    y='Customers',
    title="🌍 Customers by Region",
    color='Customers',
    color_continuous_scale='plasma'
)

st.plotly_chart(fig_region, width="stretch")

# ================= SCATTER PLOT =================
fig_ml1 = px.scatter(
    customer_df,
    x='TotalSpend',
    y='Orders',
    color='Cluster',
    size='Quantity',
    title="🧑‍🤝‍🧑 Customer Segments (K-Means)"
)

st.plotly_chart(fig_ml1, width="stretch")

# ================= PIE CHART =================

cluster_dist = customer_df['Cluster'].value_counts().reset_index()
cluster_dist.columns = ['Cluster', 'Count']

fig_ml2 = px.pie(
    cluster_dist,
    values='Count',
    names='Cluster',
    title="📊 Customer Segments Distribution"
)

st.plotly_chart(fig_ml2, width="stretch")

top_products = filtered_df.groupby('Description')['Quantity'].sum().reset_index()

fig_products = px.bar(
    top_products.sort_values(by='Quantity', ascending=False).head(10),
    x='Description',
    y='Quantity',
    title="📦 Most Bought Products",
    color='Quantity',
    color_continuous_scale='viridis'
)

st.plotly_chart(fig_products, width="stretch")



# ================= DATA TABLE =================
with st.expander("📄 View Customer Segments"):
    st.dataframe(customer_df)

# ================= DATA =================
with st.expander("📄 View Data"):
    st.dataframe(filtered_df.head(50))