import streamlit as st
import ollama

st.set_page_config(page_title="CleanCode AI", page_icon="🐍", layout="wide")

st.title("🐍 CleanCode AI: Your Personal Senior Engineer")
st.markdown("Paste your Python code below. Llama 3 will review it, find bugs, and suggest improvements.")

# Split the screen into two columns
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📥 Input Code")
    code_input = st.text_area("Paste Python Code Here:", height=400, placeholder="def my_function():\n    print('Hello world')")

    analyze_btn = st.button("🔍 Analyze & Refactor")

with col2:
    st.subheader("🤖 AI Feedback")
    
    if analyze_btn and code_input:
        with st.spinner("Analyzing logic and style..."):
            try:
                # Prompt Engineering: Acting as a Senior Dev
                prompt = f"""
                Act as a Senior Python Developer and Code Reviewer.
                Please review the following code snippet:
                
                ```python
                {code_input}
                ```
                
                Provide your output in this exact format:
                1. **Bug Report:** List potential bugs or errors.
                2. **Code Quality:** Rate the style (1-10) and explain why.
                3. **Refactored Code:** Rewrite the code to be Pythonic, efficient, and clean.
                """
                
                response = ollama.chat(model='llama3', messages=[
                    {'role': 'user', 'content': prompt},
                ])
                
                st.markdown(response['message']['content'])
                st.success("Review Complete!")
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
    
    elif analyze_btn and not code_input:
        st.warning("Please paste some code first.")
