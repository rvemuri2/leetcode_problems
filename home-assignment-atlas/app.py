import streamlit as st # type: ignore
import pandas as pd # type: ignore

def load_csv(uploaded_file):
    df = pd.read_csv(uploaded_file)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

# Rule 1: High Transaction Amount
def detect_high_transaction_amount(df, threshold=300):
    return df[df['amount'] > threshold]

# Rule 2: Rapid Transactions
def detect_rapid_transactions(df, time_window_seconds=3000):
    df = df.sort_values(by=['user_id', 'timestamp'])
    df['time_diff'] = df.groupby('user_id')['timestamp'].diff().dt.total_seconds()
    return df[df['time_diff'] <= time_window_seconds]

def detect_excessive_transactions(df, transaction_limit=10):
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.sort_values(by=['user_id', 'timestamp'])
    df['transaction_count'] = (
        df.groupby('user_id')['timestamp']
        .transform(lambda x: x.rolling('24h', on=x).count())
    )
    flagged = df[df['transaction_count'] > transaction_limit]
    return flagged

def main():
    st.title("Fraud Detection: Transaction Monitoring Rules")
    st.write("Upload a transaction CSV file to analyze it for potential fraud patterns.")

    # File uploader
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file:
        # Load and display the CSV
        df = load_csv(uploaded_file)
        st.write("### Uploaded Data:")
        st.dataframe(df)

        st.write("## Flagged Transactions:")

        # Rule 1: High Transaction Amounts
        threshold = 300
        high_transactions = detect_high_transaction_amount(df, threshold)
        st.write(f"### 1. High Transaction Amounts (Threshold > {threshold})")
        if not high_transactions.empty:
            st.dataframe(high_transactions)
        else:
            st.write("No high transaction amounts flagged.")

        # Rule 2: Rapid Transactions
        time_window = 3600
        rapid_transactions = detect_rapid_transactions(df, time_window)
        st.write(f"### 2. Rapid Transactions (Time Window ≤ {time_window} seconds)")
        if not rapid_transactions.empty:
            st.dataframe(rapid_transactions)
        else:
            st.write("No rapid transactions flagged.")

        transaction_limit = 10
        excessive_transactions = detect_excessive_transactions(df, transaction_limit)
        st.write(f"### 6. Excessive Transactions in 24-Hour Window (Limit > {transaction_limit})")
        if not excessive_transactions.empty:
            st.dataframe(excessive_transactions)
        else:
            st.write("No users flagged for excessive transactions.")


if __name__ == "__main__":
    main()
