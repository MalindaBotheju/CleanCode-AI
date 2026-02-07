# 🐍 CleanCode AI: Automated Code Reviewer

**CleanCode AI** is a local developer tool that acts as a Senior Software Engineer. It analyzes Python code for bugs, security risks, and style violations, then automatically refactors it using **Llama 3**.

## 🚀 Features
* **Bug Detection:** Catches syntax errors and logical flaws (e.g., `if x=0`).
* **Auto-Refactoring:** Rewrites code to be PEP-8 compliant and more efficient.
* **Educational:** Explains *why* changes were made to help junior devs learn.
* **100% Local:** Your proprietary code never leaves your machine.

## 🛠️ Tech Stack
* **Python 3.10+**
* **Ollama (Llama 3)** (Logic & Reasoning)
* **Streamlit** (UI)

## 📸 Demo
![App Demo](screenshot-1.png)
*(Note: Rename this if your file uploaded with a different name)*

## 📦 How to Run
1.  Clone the repo:
    ```bash
    git clone [https://github.com/MalindaBotheju/CleanCode-AI.git](https://github.com/MalindaBotheju/CleanCode-AI.git)
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the app:
    ```bash
    streamlit run app.py
    ```
