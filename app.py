import streamlit as st
def main():
    st.set_page_config(page_title="Chat with PDF using Gemini💁")
    st.header("Chat with PDF using Gemini💁")

    st.header("Enter User Details")
    user_id = st.text_input("User ID")
    user_name = st.text_input("User Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    ml_completion = st.slider("ML Course Completion (%)", 0, 100)
    dl_completion = st.slider("DL Course Completion (%)", 0, 100)
    quant_completion = st.slider("Quant Course Completion (%)", 0, 100)
    sql_completion = st.slider("SQL Course Completion (%)", 0, 100)
    python_completion = st.slider("Python Course Completion (%)", 0, 100)
    weekly_tests = st.number_input("No. of Weekly Tests", min_value=0)
    avg_weekly_marks = st.slider("Average Weekly Test Marks", 0, 100)
    sectional_tests = st.number_input("No. of Sectional Tests", min_value=0)
    avg_sectional_marks = st.slider("Average Sectional Marks", 0, 100)

    st.header("Upload PDF for Knowledge Base")
    pdf_docs = st.file_uploader("Upload your PDF Files", accept_multiple_files=True)
    
    knowledge_base = ""

    if st.button("Process PDF"):
        if pdf_docs:
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                get_vector_store(text_chunks)
                knowledge_base = raw_text
                st.success("Knowledge base created successfully!")
                st.write("Knowledge Base Content:")
                st.write(knowledge_base)
        else:
            st.warning("Please upload at least one PDF file.")

    if st.button("Generate Feedback"):
        with st.spinner("Generating feedback..."):
            user_data = {
                "user_id": user_id,
                "user_name": user_name,
                "email": email,
                "phone": phone,
                "ml_completion": ml_completion,
                "dl_completion": dl_completion,
                "quant_completion": quant_completion,
                "sql_completion": sql_completion,
                "python_completion": python_completion,
                "weekly_tests": weekly_tests,
                "avg_weekly_marks": avg_weekly_marks,
                "sectional_tests": sectional_tests,
                "avg_sectional_marks": avg_sectional_marks
            }
            feedback = generate_feedback(user_data, knowledge_base)
            st.write("Feedback: ", feedback)