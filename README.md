# 🚀 DataInsight AI

### AI-Powered Business Intelligence Platform

DataInsight AI is a modern, AI-powered business intelligence application built with **Python**, **Streamlit**, **Pandas**, **Plotly**, and **Google Gemini AI**. It enables users to upload datasets, clean and preprocess data, generate interactive visualizations, and ask natural language questions to receive AI-generated business insights.

---

## ✨ Features

### 📂 Dataset Upload
- Upload CSV datasets instantly
- Automatic dataset preview
- Session-based data storage
- Displays dataset shape and basic information

### 🧹 Data Cleaning & Preprocessing
- Handle missing values
- Remove duplicate records
- Rename columns
- Drop unnecessary columns
- Convert data types
- Preview cleaned dataset
- Download cleaned dataset

### 📊 Interactive Visual Analytics
Generate interactive charts with customizable options:

- 📊 Bar Plot
- 📦 Box Plot
- 📈 Histogram
- 🥧 Pie Chart
- 🔵 Scatter Plot
- 🔥 Correlation Heatmap

Additional customization includes:

- Custom chart title
- Multiple color themes
- Adjustable chart height
- Interactive Plotly visualizations

### 🤖 AI-Powered Business Insights

Powered by **Google Gemini 3.5 Flash**

Ask business questions in natural language, such as:

- Which product performs best?
- What sales trends do you observe?
- What are the major business insights?
- Which variables are highly correlated?
- What recommendations would improve performance?

The AI analyzes:

- Dataset structure
- Dataset statistics
- Sample records
- User question

and generates:

- Direct answers
- Business insights
- Trend analysis
- Actionable recommendations
- Limitations (when applicable)

### 📄 AI Report Download

Generate and download a complete AI Business Report including:

- Dataset summary
- AI-generated insights
- Recommendations

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Backend |
| Streamlit | Web Application |
| Pandas | Data Processing |
| Plotly Express | Interactive Charts |
| Plotly Figure Factory | Correlation Heatmap |
| Google Gemini API | AI Business Insights |

---

# 📂 Project Structure

```
DataInsight-AI/
│
├── Home.py
│
├── pages/
│   ├── 1_📂 Upload CSV Dataset.py
│   ├── 2_🧹 Data Cleaning.py
│   ├── 3_📈 Visual Analytics.py
│   └── 4_🧠 AI Business Insights.py
│
├── .streamlit/
│   └── secrets.toml
│
├── requirements.txt
├── README.md
└── assets/
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/DataInsight-AI.git
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

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

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

# 🔑 Gemini API Configuration

Create a file named:

```
.streamlit/secrets.toml
```

Add your API key:

```toml
GEMINI_API_KEY = "YOUR_API_KEY"
```

---


# 🎯 Project Highlights

- Multi-page Streamlit application
- AI-powered business analysis
- Interactive Plotly dashboards
- Data preprocessing pipeline
- Downloadable AI reports
- Clean and modern user interface
- Session state management
- Responsive layout

---

# 🔮 Future Improvements

- PDF report generation
- Excel report export
- Additional chart types
- Dashboard templates
- User authentication
- Cloud deployment
- Database integration
- Conversational AI chat interface
- Time-series forecasting
- Machine Learning predictions

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push your branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Developer

**Shivendra Mahato**

Python Developer | Data Analytics Enthusiast | AI & Machine Learning Learner

---
