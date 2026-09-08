import streamlit as st
import pandas as pd

st.set_page_config(page_title='Blood Donation Platform',page_icon='🩸',layout='wide')
st.title('🩸 Smart Blood Donation Platform')
st.caption('Donor directory and blood-request matching MVP.')

if 'donors' not in st.session_state:
    st.session_state.donors=pd.DataFrame([
      {'Name':'Amin','Blood':'A+','City':'Dhaka','Available':True},
      {'Name':'Nadia','Blood':'O+','City':'Gazipur','Available':True},
      {'Name':'Rahim','Blood':'B+','City':'Uttara','Available':False},
      {'Name':'Sadia','Blood':'AB+','City':'Dhaka','Available':True}])

blood=st.selectbox('Required blood group',['A+','A-','B+','B-','AB+','AB-','O+','O-']); city=st.text_input('Preferred city')
if st.button('Find compatible donors',type='primary'):
    d=st.session_state.donors[(st.session_state.donors.Blood==blood)&(st.session_state.donors.Available)]
    if city.strip(): d=d[d.City.str.contains(city.strip(),case=False,na=False)]
    st.success(f'{len(d)} matching donor(s) found'); st.dataframe(d,use_container_width=True,hide_index=True)

with st.expander('Register as donor'):
    name=st.text_input('Name'); bg=st.selectbox('Your blood group',['A+','A-','B+','B-','AB+','AB-','O+','O-']); c=st.text_input('City'); available=st.checkbox('Available to donate',True)
    if st.button('Register donor'):
        if name and c:
            st.session_state.donors=pd.concat([st.session_state.donors,pd.DataFrame([{'Name':name,'Blood':bg,'City':c,'Available':available}])],ignore_index=True); st.rerun()

st.subheader('Privacy & safety')
st.warning('This MVP does not verify medical eligibility or identity. Production deployments should use consent, verification, secure authentication and health-data safeguards.')
