import streamlit as st

st.set_page_config(page_title='Contact', page_icon='✉️')

def txt2(x, y):
  block1, block2 = st.columns([1,4])
  with block1:
    st.markdown(f'`{x}`')
  with block2:
    st.markdown(y)

st.header("Get In Touch With Me! :mailbox:")


contact_form = """
<form action="https://formsubmit.co/b149eff04bb46d6ce8a87d8fc8098eef" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)
 

with st.container():
   block3, block4 = st.columns((2,2))
   with block3:
      st.write('')
   with block4:
      st.write('')

st.header('Social Media Links 📱')
txt2('LinkedIn', 'https://www.linkedin.com/in/siddharth-bhangale-0a6661201/')
txt2('Twitter', 'https://twitter.com/Sidey65479535')
txt2('GitHub', 'https://github.com/SIDEYS')
txt2('Instagram', 'https://www.instagram.com/s.i.d.e.y/')

# Using Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("styles/style.css")