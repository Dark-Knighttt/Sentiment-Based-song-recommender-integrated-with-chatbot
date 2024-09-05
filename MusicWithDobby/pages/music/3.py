import streamlit as st

def main():
    st.title("Clickable Objects in Streamlit")
    
    st.write("This is a link that opens in a new tab when clicked:")
    st.write("[Open Google](https://www.google.com)", unsafe_allow_html=True)

if __name__ == "__main__":
    main()