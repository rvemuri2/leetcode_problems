import streamlit as st # type: ignore
import pandas as pd # type: ignore

def load_csv(uploaded_file):
    df = pd.read_csv(uploaded_file)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

def detect_high_transaction_amount(df, threshold=500):
    return df[df['amount'] > threshold]

def detect_rapid_transactions(df, time_window_seconds=3000):
    df = df.sort_values(by=['user_id', 'timestamp'])
    df['time_diff'] = df.groupby('user_id')['timestamp'].diff().dt.total_seconds()
    return df[df['time_diff'] <= time_window_seconds]

def detect_excessive_transactions(df, transaction_limit=10):
     df = df.sort_values(by=['user_id', 'timestamp'])
    
     results = []

    # Iterate over each user group
     for user_id, group in df.groupby('user_id', group_keys=False):  # Avoid re-adding group keys
        group = group.set_index('timestamp')  # Set timestamp as index
        group['transaction_count'] = group.rolling('1d').count()['user_id']  # Use rolling count
        group = group.reset_index()  # Reset index to align with the original DataFrame
        group['user_id'] = user_id  # Explicitly re-add user_id column
        results.append(group)

    # Concatenate results for all users
     df = pd.concat(results)

    # Filter rows where the transaction count exceeds the limit
     flagged = df[df['transaction_count'] > transaction_limit]

     return flagged

def detect_near_duplicate_transactions(df, time_delta_seconds=60):
    df = df.sort_values(by=['user_id', 'timestamp'])
    df['time_diff'] = df.groupby(['user_id', 'merchant_name', 'amount'])['timestamp'].diff().dt.total_seconds()
    duplicates = df[df['time_diff'].abs() <= time_delta_seconds]
    return duplicates

def detect_near_threshold_transactions(df, threshold=500, delta=30):
    lower_limit = threshold - delta
    flagged = df[(df['amount'] >= lower_limit) & (df['amount'] < threshold)]
    return flagged

def main():
    st.title("Fraud Detection: Transaction Monitoring Rules")
    st.write("Upload a transaction CSV file to analyze it for potential fraud patterns.")

    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file:
        # Load and display the CSV
        df = load_csv(uploaded_file)
        st.write("### Uploaded Data:")
        st.dataframe(df)

        st.write("## Flagged Transactions:")

        # Rule 1: High Transaction Amounts
        threshold = 500
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

        #Rule 3: Transaction limits
        transaction_limit = 10
        excessive_transactions = detect_excessive_transactions(df, transaction_limit)
        st.write(f"### 3. Excessive Transactions in 24-Hour Window (Limit > {transaction_limit})")
        if not excessive_transactions.empty:
            st.dataframe(excessive_transactions)
        else:
            st.write("No users flagged for excessive transactions.")
        
        #Rule 4: Detecting duplicate transactions
        duplicate_transactions = detect_near_duplicate_transactions(df, 60)
        st.write("### 4.Duplicate Transactions") 
        if not duplicate_transactions.empty:
            st.dataframe(duplicate_transactions)
        else:
            st.write("No users flagged for duplicate transactions")
        
        # Rule 5: Near-Threshold Transactions
        delta = 30
        near_threshold_transactions = detect_near_threshold_transactions(df, threshold, delta)
        st.write(f"### 5. Near-Threshold Transactions")
        if not near_threshold_transactions.empty:
            st.dataframe(near_threshold_transactions)
        else:
            st.write("No near-threshold transactions flagged.")


if __name__ == "__main__":
    main()
