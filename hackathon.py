import streamlit as st
import pandas as pd
import googleaistudio
import os

googleaistudio.api_key = os.getenv("AIzaSyB8I5-0vxwpba6Yf6H5i-GXRcdmKYlyA8o")

# Streamlit app title
st.title("DataQueryAI")

# File upload section
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
df = None

if uploaded_file is not None:
    # Read the uploaded CSV file
    df = pd.read_csv(uploaded_file)
    st.write("### Preview of Uploaded Data")
    st.write(df.head())

    # Show column names
    st.write("### Column Names")
    st.write(list(df.columns))

# Query input section
if df is not None:
    query = st.text_input("Ask a question about your data:")
    
    if query:
        try:
            # Use OpenAI to interpret the query
            prompt = f"You are a data analyst. Given a dataset with columns: {list(df.columns)}, how would you analyze it to answer: '{query}'? Provide Python code."
            response =googleaistudio.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=150
            )
            analysis_instructions = response.choices[0].text.strip()
            st.write("### Analysis Instructions")
            st.code(analysis_instructions)

            # Execute the generated code (simplified for demonstration)
            if "mean" in analysis_instructions:
                result = df.mean()
            elif "sum" in analysis_instructions:
                result = df.sum()
            else:
                result = "Analysis not supported in this demo."

            st.write("### Result")
            st.write(result)
        except Exception as e:
            st.error(f"An error occurred: {e}")
 