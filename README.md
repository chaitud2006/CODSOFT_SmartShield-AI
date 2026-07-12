# 🛡️ SmartShield AI: Enterprise Spam Detection System

SmartShield AI is an intelligent, real-time message analysis platform designed for enterprise-grade spam detection. It transforms raw message input into actionable security intelligence with high accuracy and low latency.

## 🚀 Key Features

* **Intelligent Detection:** Uses a machine learning pipeline with **TF-IDF vectorization** to classify SMS messages as SAFE or SPAM.
* **Explainable AI (XAI):** Not just a "black box"—the system identifies and displays the top keywords contributing to a spam classification, helping users understand *why* a message was flagged.
* **Command Center UI:** A high-contrast, professional dark-mode dashboard built for security operations.
* **Enterprise Telemetry:** Real-time system monitoring including **Latency tracking** and **Spam trend visualization**.
* **Auditability:** Built-in transaction logging with one-click **CSV Export** functionality for security reporting and compliance.

## 🛠️ Tech Stack

* **Framework:** [Streamlit](https://streamlit.io/) (Customized with CSS/Glassmorphism)
* **ML Engine:** [Scikit-learn](https://scikit-learn.org/) (Joblib, TfidfVectorizer)
* **Visualization:** [Plotly](https://plotly.com/) (Dynamic time-series analysis)
* **Data Handling:** Pandas & NumPy

## 📈 Dashboard Preview
The dashboard provides a real-time view of detection trends, enabling security teams to monitor spam volume and system performance at a glance.

*(Optional: Add a screenshot of your dashboard here using: ![Dashboard](path_to_your_image.png))*

## 📦 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/SmartShield-AI.git](https://github.com/yourusername/SmartShield-AI.git)
   cd SmartShield-AI
