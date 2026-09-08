import io
import re
import streamlit as st
from pypdf import PdfReader

st.set_page_config(page_title='AI Resume Analyzer', page_icon='📄', layout='wide')
st.title('📄 AI Resume Analyzer')
st.caption('Resume-to-job matching MVP using NLP-style skill extraction and scoring.')

SKILLS = ['python','django','fastapi','flask','react','javascript','typescript','java','c#','sql','postgresql','mongodb','docker','git','aws','machine learning','deep learning','pytorch','tensorflow','pandas','scikit-learn','nlp','rest api','html','css','power bi','excel']

def extract_text(upload):
    reader = PdfReader(io.BytesIO(upload.read()))
    return '\n'.join(page.extract_text() or '' for page in reader.pages)

def skills(text):
    low = text.lower()
    return sorted({s for s in SKILLS if re.search(r'(?<![a-z])'+re.escape(s)+r'(?![a-z])', low)})

resume = st.file_uploader('Upload resume PDF', type='pdf')
job = st.text_area('Paste job description', height=220, placeholder='Python, Django, PostgreSQL, Docker...')
if st.button('Analyze', type='primary'):
    if not resume or not job.strip():
        st.warning('Upload a resume and enter a job description.')
    else:
        text = extract_text(resume)
        rskills, jskills = skills(text), skills(job)
        matched = sorted(set(rskills) & set(jskills)); missing = sorted(set(jskills)-set(rskills))
        score = round(100*len(matched)/max(1,len(set(jskills))), 1)
        c1,c2,c3 = st.columns(3)
        c1.metric('Match score', f'{score}%'); c2.metric('Matched skills', len(matched)); c3.metric('Missing skills', len(missing))
        st.subheader('Matched skills'); st.write(', '.join(matched) or 'None detected')
        st.subheader('Skills to improve'); st.write(', '.join(missing) or 'Great coverage!')
        st.subheader('Resume insights')
        st.write(f'Detected {len(rskills)} skills in the resume. For a stronger application, quantify achievements and tailor keywords to the target role.')
