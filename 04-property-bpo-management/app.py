import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title='Property & BPO Management',page_icon='🏢',layout='wide')
st.title('🏢 Property & BPO Management System')
st.caption('Operations dashboard for work orders, vendors, properties and SLA tracking.')

if 'jobs' not in st.session_state:
    st.session_state.jobs=pd.DataFrame([
      {'ID':'JOB-1001','Property':'Austin Residence','Service':'Lawn care','Vendor':'GreenPro','Status':'Assigned','SLA days':2},
      {'ID':'JOB-1002','Property':'Dallas Condo','Service':'Inspection','Vendor':'SafeCheck','Status':'In Progress','SLA days':1},
      {'ID':'JOB-1003','Property':'Houston Home','Service':'Board-up','Vendor':'SecureFix','Status':'Completed','SLA days':0}])

c1,c2,c3=st.columns(3); c1.metric('Total jobs',len(st.session_state.jobs)); c2.metric('Open jobs',int((st.session_state.jobs.Status!='Completed').sum())); c3.metric('Completed',int((st.session_state.jobs.Status=='Completed').sum()))
st.subheader('Work orders')
st.dataframe(st.session_state.jobs,use_container_width=True,hide_index=True)
with st.expander('Create work order'):
    a,b=st.columns(2); prop=a.text_input('Property'); service=b.text_input('Service'); vendor=a.text_input('Vendor'); status=b.selectbox('Status',['New','Assigned','In Progress','Completed']); sla=a.number_input('SLA days',0,30,2)
    if st.button('Add work order'):
        if prop and service:
            new=pd.DataFrame([{'ID':f'JOB-{1000+len(st.session_state.jobs)+1}','Property':prop,'Service':service,'Vendor':vendor,'Status':status,'SLA days':sla}]); st.session_state.jobs=pd.concat([st.session_state.jobs,new],ignore_index=True); st.rerun()
st.subheader('Operational notes')
st.info('Production upgrade: PostgreSQL database, role-based access, document uploads, vendor contracts, automated SLA alerts and REST API.')
