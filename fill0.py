# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 11:32:37 2023

@author: ryan.nugraha
"""

import pandas as pd
import numpy as np
import streamlit as st
import io

st.write("DB username:", st.secrets["DB_USERNAME"])
st.write("DB password:", st.secrets["DB_PASSWORD"])
st.write("KEY:", st.secrets["1234"])

# And the root-level secrets are also accessible as environment variables:

import os

st.write(
    "Has environment variables been set:",
    os.environ["DB_USERNAME"] == st.secrets["DB_USERNAME"],
)

def main():
    st.title("FILL NaN with 0")

    # File Upload
    uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        st.dataframe(df)

        # Fill NaN values with 0
        df_filled = df.fillna(0)

        # Download button
        output_buffer = io.BytesIO()
        df_filled.to_excel(output_buffer, index=False)
        st.download_button("Download filled DataFrame as Excel", data=output_buffer.getvalue(), file_name="output.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

if __name__ == "__main__":
    main()
