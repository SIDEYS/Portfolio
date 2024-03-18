import streamlit as st
from PIL import Image

st.set_page_config(page_title='Projects', page_icon='📂' )


st.title('Projects')

with st.container():
  col1,col2 = st.columns((1, 2))
#   with col1:
#     st.image(Image.open('./img/p6.png'))
  with col2:
    st.subheader("Real-vs-FakeImg")
    st.write("""
    Deep Learning models made using Convolutional Neural Nets and Tranfer Learning for classification of images generated using AI.
             """)

    st.markdown('`Transfer Learning`, `VGG16`, `Tensorflow`, `CNN`')

    Project1 = '[GitHub](https://github.com/SIDEYS/Real-vs-FakeImg/tree/main)'
    st.markdown(Project1)

st.write('---')

with st.container():
  col1,col2 = st.columns((1, 2))
#   with col1:
#     st.image(Image.open('./img/p2.png'))
  with col2:
    st.subheader("SpamSlueth")
    st.write("""
    SpamSleuth: Unveiling Deceptive Opinion Spam Welcome to SpamSleuth, your trusted ally in the battle against deceptive opinion spam! This repository hosts some powerful models designed to detect and expose misleading opinions circulating online.
             """)

    st.markdown('`Natural Languaage Processing`, `CNN`, `LSTM\'s`, `EDA`, `Textual Preprocessing`, `colab`, `RNN` ,`Spacy`, `Attention Models`, `Glove`')

    Project2 = '[GitHub](https://github.com/SIDEYS/SpamSleuth/tree/main)'
    st.markdown(Project2)

st.write('---')

with st.container():
  col3,col4 = st.columns((1, 2))
#   with col3:
#     st.image(Image.open('./img/p5.png'))
  with col4:
    st.subheader("ML-Projects")
    st.write("""Diverse machine learning projects, encompassing regression, classification, and clustering models. . Achieved impactful results through data-driven insights and innovative problem-solving techniques..""")

    st.markdown('`Pandas`, `Numpy`, `Clustering`, `EDA`, `Matplotib`, `Seaborn`, `colab` ')

    Project3 = '[GitHub](https://github.com/SIDEYS/ML-Projects)'
    st.markdown(Project3)

st.write('---')

# with st.container():
#   col5,col6 = st.columns((1, 2))
# #   with col5:
# #     st.image(Image.open('./img/p1.png'))
#   with col6:
#     st.subheader("Olympic Data Analysis Web Application")
#     st.write("""
#     This analysis will provide detailed and accurate information regarding various factors which leads to the evolution of Olympic Games and improvement of Countries/Players over the time in visual format.
#     """)

#     st.markdown('`EDA`, `Streamlit`, `pandas`, `matplotlib`, `plotly`, `seaborn`')

#     g3 = '[GitHub](https://github.com/mayuras7685/Olympics-data-analysis)'
#     st.markdown(g3)

# st.write('---')

with st.container():
  col7,col8 = st.columns((1, 2))
#   with col7:
#     st.image(Image.open('./img/p4.png'))
  with col8:
    st.subheader("Fake News Classifier")
    st.write("""Developed a Fake News Classifier using natural language processing and Bidirectional Recurrent neural networks to identify and mitigate misinformation, promoting media literacy and fostering informed decision-making""")

    st.markdown('`NLP`, `Bi-Directional RNN`, `pandas`')

    Project4 = '[GitHub](https://github.com/SIDEYS/FakeNewsClassifier/tree/main)'
    st.markdown(Project4)

st.write('---')

with st.container():
  col9,col10 = st.columns((1, 2))
#   with col9:
#     st.image(Image.open('./img/p3.png'))
  with col10:
    st.subheader("Portfolio Website Using Streamlit")
    st.write("""The Streamlit Portfolio app is an immersive web application created with the Streamlit library, designed specifically to exhibit my professional portfolio, projects, and proficiencies. This multifaceted Streamlit web app delivers an interactive platform for displaying my capabilities and past works. """)

    st.markdown('`Python`, `Streamlit`')

    Project5 = '[GitHub](https://github.com/SIDEYS/Portfolio)'
    st.markdown(Project5)
