# 🚀 DataInsight AI

### AI-Powered Data Analytics & Machine Learning Preparation Platform

DataInsight AI is an AI-powered data analytics application built using **Python**, **Streamlit**, **Pandas**, **Plotly**, and **Groq (Llama 3.3 70B Versatile)**.

It enables users to upload datasets, clean and preprocess data, perform Exploratory Data Analysis (EDA), generate interactive visualizations, and receive AI-powered insights using natural language.

The platform is designed to simplify the complete data preparation workflow before machine learning model development.

---

# 🌐 Live Demo

👉 https://datainsightai.streamlit.app/

---

# ✨ Features

## 📂 Data Processing

Clean and preprocess datasets without writing code.

### Available Operations

- Upload CSV datasets
- Preview uploaded dataset
- Handle missing values
- Remove duplicate records
- Rename columns
- Drop unwanted columns
- Convert data types
- Download cleaned dataset

---

## 📈 Visual Analytics

Generate beautiful interactive visualizations using Plotly.

### Supported Charts

- 📊 Bar Chart
- 📈 Histogram
- 🔵 Scatter Plot
- 🥧 Pie Chart
- 📦 Box Plot
- 🔥 Correlation Heatmap

### Customization Options

- Chart title
- Color themes
- Adjustable chart height
- Interactive zoom and hover

---

## 🧠 AI Insights & Reports

Powered by **Groq Cloud** using **Llama 3.3 70B Versatile**.

Ask questions in natural language such as:

- Summarize this dataset.
- What important patterns do you observe?
- Are there any anomalies?
- Which columns appear highly correlated?
- What preprocessing steps should be performed?
- Is this dataset suitable for Machine Learning?
- Suggest feature engineering ideas.
- Recommend improvements before model training.

The AI analyzes:

- Dataset shape
- Column information
- Data types
- Statistical summary
- Sample records

and generates:

- Executive Summary
- Dataset Interpretation
- Pattern Detection
- Trend Analysis
- Data Quality Assessment
- Actionable Recommendations
- Machine Learning Preparation Suggestions

---

## 📄 AI Report Generation

Generate downloadable AI reports containing:

- Dataset Summary
- User Question
- AI-generated Insights
- Recommendations
- Report Generation Timestamp

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core Programming Language |
| Streamlit | Web application framework |
| Pandas | Data Cleaning & Data Manipulation |
| Plotly | Interactive Data Visualization |
| Groq API | AI Inference |
| Llama 3.3 70B Versatile | Large Language Model |

---

# 📂 Project Structure

```text
DataInsight-AI/
│
├── Home.py
│
├── pages/
│   ├── 1_📂 Data Processing.py
│   ├── 2_📈 Visual Analytics.py
│   └── 3_🧠 AI Insights & Reports.py
│
├── utils/
│
├── assets/
│
├── .streamlit/
│   └── secrets.toml
│
├── .devcontainer/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Shivendra0629/DataInsight-AI.git
```

Move into the project directory

```bash
cd DataInsight-AI
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run Home.py
```

---

# 🔑 API Configuration

Create the following file:

```
.streamlit/secrets.toml
```

Add your Groq API Key:

```toml
GROQ_API_KEY="YOUR_API_KEY"
```

---

# 🎯 Project Highlights

- AI-assisted Dataset Analysis
- Interactive Data Cleaning
- Exploratory Data Analysis (EDA)
- Interactive Plotly Dashboards
- AI-generated Dataset Insights
- Downloadable AI Reports
- Session State Management
- Multi-page Streamlit Application
- Responsive User Interface
- Machine Learning Dataset Preparation

---

# 🔮 Future Improvements

- Automated Feature Engineering
- Machine Learning Model Training
- AutoML Integration
- Feature Importance Analysis
- Outlier Detection Assistant
- Time Series Forecasting
- PDF Report Export
- Excel Report Export
- SQL Database Connectivity
- User Authentication
- Dashboard Sharing

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository.

2. Create a new branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Added new feature"
```

4. Push your branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Developer

## Shivendra Mahato

**Python Developer • Data Analytics Enthusiast • AI & Machine Learning Learner**

---

