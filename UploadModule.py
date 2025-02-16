import streamlit as st

def main():
    st.title("Data Upload Module")

    uploaded_file = st.file_uploader("File Upload", type=["csv", "xlsx"]) 

    if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        st.write(bytes_data)

        # To convert to a pandas DataFrame:
        import pandas as pd
        df = pd.read_csv(uploaded_file)
        st.write(df)

if __name__ == '__main__':
    main()