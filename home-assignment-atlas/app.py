import streamlit as st # type: ignore
import pandas as pd # type: ignore

# App title
st.title("CSV File Uploader and Viewer")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the uploaded CSV file
    try:
        df = pd.read_csv(uploaded_file)

        flagged_high_transactions = df[df['amount'] > 300]
        
        # Display the dataframe
        st.write("### Flagged Transactions:")
        st.dataframe(flagged_high_transactions)
        
    except Exception as e:
        st.error(f"An error occurred while processing the file: {e}")
else:
    st.info("Awaiting file upload. Please drag and drop a CSV file above.")
