import streamlit as st

st.set_page_config(
    page_title="Siddharth's Portfolio",
    page_icon="🏚️",
)


with st.container():
    block1,block2 = st.columns((2,1))
    with block1:
        st.title("Hey there, I'm Siddharth! 👋🤖")
        st.subheader(
         """
         AI/ML enthusiast exploring possibilities, solving problems, staying updated. 🌟🚀
         """
        )
    
    with block2:
        st.image("./Images/sidimg.jpeg")

