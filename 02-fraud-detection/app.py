import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

st.set_page_config(page_title='Fraud Detection', page_icon='🛡️', layout='wide')
st.title('🛡️ Transaction Fraud Detection')
st.caption('Machine-learning MVP with synthetic training data and explainable transaction inputs.')

@st.cache_resource
def train():
    n=1500; rng=pd.Series(range(n))
    df=pd.DataFrame({'amount':((rng*37)%1000+20).astype(float),'hour':(rng*7)%24,'velocity':(rng*3)%12,'foreign':(rng%7==0).astype(int),'device_change':(rng%11==0).astype(int)})
    df['fraud']=((df.amount>800)&(df.velocity>7) | (df.foreign==1)&(df.device_change==1)).astype(int)
    X=df.drop(columns='fraud'); y=df.fraud
    Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.2,random_state=42,stratify=y)
    model=RandomForestClassifier(n_estimators=160,random_state=42,class_weight='balanced'); model.fit(Xtr,ytr)
    return model, classification_report(yte,model.predict(Xte),output_dict=True)

model, report=train()
with st.sidebar:
    st.header('Transaction')
    amount=st.number_input('Amount',20.0,10000.0,750.0)
    hour=st.slider('Hour',0,23,22)
    velocity=st.slider('Transactions in last hour',0,30,8)
    foreign=st.checkbox('Foreign transaction')
    device=st.checkbox('New device')
if st.button('Check transaction',type='primary'):
    row=pd.DataFrame([{'amount':amount,'hour':hour,'velocity':velocity,'foreign':int(foreign),'device_change':int(device)}])
    prob=model.predict_proba(row)[0,1]
    st.metric('Fraud probability',f'{prob:.1%}')
    if prob>=.5: st.error('High-risk transaction — send for manual review.')
    else: st.success('Low-risk transaction.')
st.subheader('Model performance')
acc=report['accuracy']; st.metric('Validation accuracy',f'{acc:.1%}')
st.dataframe(pd.DataFrame(report).T.round(3),use_container_width=True)
