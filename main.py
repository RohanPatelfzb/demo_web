import streamlit as st
data1=st.text_input("enter your name:")
data2=st.text_input("enter your father name:")
data3=st.text_area("enter your address:")
classdata=st.selectbox("enter your class:",(1,2,3,4,5))
btn=st.button("done")
if btn:
    st.markdown(F"""
    Name:{data1}
    Father name:{data2}
    Address:{data3}
    class:{classdata}
""")