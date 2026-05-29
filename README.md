## 📊 E-Commerce Sales Analysis Dashboard

## 🚀 Project Overview
This project focuses on analyzing e-commerce sales data to extract meaningful insights using **Data Analysis, Visualization, and Machine Learning**.
An interactive dashboard is built to help users understand:

* Sales trends 📈
* Customer behavior 🧑‍🤝‍🧑
* Product performance 📦
* Regional distribution 🌍

The project also includes **customer segmentation using K-Means clustering** to identify different types of customers.

## 🛠️ Tech Stack

* Python 🐍
* Pandas & NumPy (Data Processing)
* Plotly (Visualization)
* Streamlit (Web Dashboard)
* Scikit-learn (Machine Learning)


## 📁 Project Structure

ecommerce-sales-analysis/
│
├── data/
│   └── online_retail.xlsx
│
├── notebook/
│   └── eda_analysis.ipynb
│
├── app/
│   ├── app.py          # Main Streamlit dashboard
│   ├── ml.py           # Machine Learning (K-Means)
│   └── utils.py        # Data loading & preprocessing
│
├── requirements.txt
└── README.md


## 📊 Features

### 🔹 Data Analysis

* Monthly & daily sales trends
* Top-selling products
* Country-wise sales analysis

### 🔹 Interactive Dashboard

* Filters:

  * Country 🌍
  * Product 📦
  * Date Range 📅
  * Sales Range 💰
* Real-time updates

### 🔹 Visualizations

* Line charts (Sales trends)
* Bar charts (Top products, countries)
* Pie & Donut charts
* Stacked bar charts

### 🔹 Machine Learning

* Customer segmentation using K-Means
* Clusters:

  * 🟢 Low Value Customers
  * 🔵 Medium Value Customers
  * 🔴 High Value (VIP) Customers

## 📷 Dashboard Preview
<img width="1906" height="960" alt="Screenshot 2026-05-03 214723 - Copy" src="https://github.com/user-attachments/assets/9bbbd067-981d-45d8-b165-b97409b95706" />
<img width="1919" height="801" alt="Screenshot 2026-05-03 214754 - Copy" src="https://github.com/user-attachments/assets/45ecd6d2-13cf-4b38-ae84-fd6b0eeda21a" />
<img width="1882" height="741" alt="Screenshot 2026-05-03 214817 - Copy" src="https://github.com/user-attachments/assets/4148121f-ecda-4fda-8bd5-69694da9547d" />
<img width="1915" height="894" alt="Screenshot 2026-05-03 214828" src="https://github.com/user-attachments/assets/b1a1d9d1-5d35-4367-9474-081215aaa0e6" />
<img width="1898" height="947" alt="Screenshot 2026-05-03 214846 - Copy" src="https://github.com/user-attachments/assets/b8be92b3-0230-40a5-b5a5-29e9b9434d71" />
<img width="1912" height="955" alt="Screenshot 2026-05-03 214906" src="https://github.com/user-attachments/assets/522a5e3d-8d46-4746-8cc9-00de27408cfa" />
<img width="1443" height="675" alt="Screenshot 2026-05-03 215040" src="https://github.com/user-attachments/assets/ecb9f43d-bb03-490e-bece-b4fe677031c0" />
<img width="1877" height="608" alt="Screenshot 2026-05-03 225615" src="https://github.com/user-attachments/assets/e53d9e40-98d0-44c5-a1f6-300273cf37ea" />
<img width="1882" height="906" alt="Screenshot 2026-05-03 225636" src="https://github.com/user-attachments/assets/4da46e15-8f4b-4954-9037-8fb042d221d7" />
<img width="1795" height="926" alt="Screenshot 2026-05-03 225656" src="https://github.com/user-attachments/assets/706808cd-7891-4655-a434-e7d7e556b264" />


## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/ecommerce-sales-analysis.git
cd ecommerce-sales-analysis
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

### 3️⃣ Activate Environment

```bash
# Windows
.venv\Scripts\activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Run Application

```bash
streamlit run app/app.py
```

## 📌 Dataset

* Source: Kaggle (Online Retail Dataset)
* Contains:
  * Invoice details
  * Product descriptions
  * Quantity & pricing
  * Customer and country data
  * 

## 🤖 Machine Learning Approach

We used **K-Means Clustering** to segment customers based on:

* Total Spend 💰
* Number of Orders 🧾
* Quantity Purchased 📦

This helps in identifying:

* High-value customers
* Regular customers
* Low-value customers

## 📈 Key Insights

* A small number of customers generate most revenue
* Few products dominate total sales
* Sales are concentrated in specific regions
* Customer segmentation helps targeted marketing

## 🎯 Future Improvements

* Add recommendation system
* Deploy dashboard online (Streamlit Cloud)
* Use advanced ML models
* Add real-time data integration

## 👨‍💻 Author

**Sakshi Vijay Sataye**
📧 sakshisataye2003@gmail.com
🔗 LinkedIn:[www.linkedin.com/in/sakshi-sataye](https://www.linkedin.com/in/sakshi-sataye )



