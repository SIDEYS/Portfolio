import streamlit as st

import streamlit as st

st.set_page_config(page_title='Experience', page_icon='💼' )

st.title('Experience')
st.write("In theory there is no difference between theory and practice. In practice there is. ― Yogi Berra")

with st.container():
   emptyBlock1, emptyBlock2 = st.columns((2,2))
   with emptyBlock1:
      st.write('')
   with emptyBlock2:
      st.write('')

with st.container():
   emptyBlock1, emptyBlock2 = st.columns((2,2))
   with emptyBlock1:
      st.write('')
   with emptyBlock2:
      st.write('')



with st.container():
    block1, block2, block3 =st.columns((2, 5, 2))
    with block1:
        st.image('./Images/iiitsuratlogo.jpeg')
    with block2:
        st.subheader('Indian Institute of Infromation Technology, Surat')
        st.write('Machine Learning Intern')
        st.markdown('''
        - Learned Web Scraping of Reviews, Tweets using Selenium for Making Datasets
        - Data Pre-processing
        - Feature Extraction From textual data, Data Visualization
        - Learned building Machine Learning Models and Evaluation Metrics
        - Learned about Neural Networks and Pre-trained Embedding.
        ''')
    with block3:
       st.markdown('<small>Jun 2023 - Aug 2023</small>', unsafe_allow_html=True)



with st.container():
   emptyBlock1, emptyBlock2 = st.columns((2,2))
   with emptyBlock1:
      st.write('')
   with emptyBlock2:
      st.write('')

with st.container():
   emptyBlock1, emptyBlock2 = st.columns((2,2))
   with emptyBlock1:
      st.write('')
   with emptyBlock2:
      st.write('')

st.write('---')

with st.container():
   emptyBlock1, emptyBlock2 = st.columns((2,2))
   with emptyBlock1:
      st.write('')
   with emptyBlock2:
      st.write('')

with st.container():
   emptyBlock1, emptyBlock2 = st.columns((2,2))
   with emptyBlock1:
      st.write('')
   with emptyBlock2:
      st.write('')



with st.container():
    block3, block4, block5 =st.columns((2, 5, 2))
    with block3:
        st.image('./Images/teconicopvtltd_logo.jpeg')
    with block4:
        st.subheader('TecoNico Pvt. Ltd')
        st.write('Backend Developer')
        st.markdown('''
         - Worked on making new Admin panel.
         - Developed apis for different modules and microservices.
         - Used mongoDb pipelinnes for data aggregation.
         - Implemented different levels of authorization to access website. eg:- superadmin, admin etc.
        ''')
        with block5:
          st.markdown('<small>Oct 2023 - Feb 2024</small>', unsafe_allow_html=True)