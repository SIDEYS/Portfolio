import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title='About', page_icon='👨‍💻' )


def txt(x, y):
  Block1, Block2 = st.columns([4,1])
  with Block1:
    st.markdown(x)
  with Block2:
    st.markdown(y)

def txt3(x, y):
  Block1, Block2 = st.columns([1,2])
  with Block1:
    st.markdown(x)
  with Block2:
    st.markdown(y)


with st.container():
   Block1, Block2 = st.columns([5, 1])
   with Block1:
      st.title('About 👨‍💻')



with st.container():
      st.write('My name is Siddharth Bhangale, Currently I am pursuing ***Computer Science and Engineering*** from Indian Institute of Information Technology, Surat. I am in the pre final year of .')

      st.write('I am an individual with diverse interests, passionate about learning and exploring new ideas. I enjoy connecting with people, fostering creativity, and making a positive impact on the world around me. I am a Backend Developer and a AI/ML enthusiast')
        

st.title('Education 📖')


txt('**Bachelors in Technology(BTech)** (Computer Science and Engineering), *Indian Institute of Information Technology*, Surat',
'2021-2025')
st.markdown('''
- CGPA: `8.11`

''')

st.write('-----')

txt('**HSC (Class XII)**, *ASM(CSIT)College of commerce, science and Information Technology, Pimpri*, Pune',
'2021')
st.markdown('''
- Percentage: `88.00`

''')

st.write('-----')

txt('**CBSE (Class X)**, *Mount St Ann High school, Talegaon Dabhade*, Pune',
'2019')
st.markdown('''
- Percentage: `92.40`
''')


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


st.title('Skills & Tools ⚒️')

txt3('Programming', '`C`,`C++`,`Javascript`,`Python`')
txt3('Data processing/wrangling', '`pandas`, `numpy`')
txt3('Database', '`Mysql`, `Mongodb`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`, `Keras`,`NLP`')
txt3('Web development', '`HTML`, `CSS`,`Node.js`,`Express.js`')
txt3('Tools', '`Power Bi`,`Colab`')
txt3('Version Control', '`git`,`Github`')
txt3('Model deployment', '`streamlit`, `Heroku`')

with st.container():
   emptyBlock3, emptyBlock4 = st.columns((2,2))
   with emptyBlock3:
      st.write('')
   with emptyBlock4:
      st.write('')

with st.container():
   emptyBlock3, emptyBlock4 = st.columns((2,2))
   with emptyBlock3:
      st.write('')
   with emptyBlock4:
      st.write('')

#resume 
pdfFileObj = open('Sidd_resume_updated.pdf', 'rb')
with st.container():
   block1,block2 = st.columns((2,3))
   with block2:
      st.download_button('Download Resume',pdfFileObj,file_name='Sidd_resume_updated.pdf',mime='pdf')

