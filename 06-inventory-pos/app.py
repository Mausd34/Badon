import streamlit as st
import pandas as pd

st.set_page_config(page_title='Inventory & POS',page_icon='🛒',layout='wide')
st.title('🛒 Inventory & POS Management')
st.caption('Sales, stock and low-inventory dashboard MVP.')

if 'products' not in st.session_state:
    st.session_state.products=pd.DataFrame([
      {'SKU':'P001','Product':'Keyboard','Price':1800.0,'Stock':18},
      {'SKU':'P002','Product':'Mouse','Price':900.0,'Stock':7},
      {'SKU':'P003','Product':'Monitor','Price':18500.0,'Stock':4}])

st.subheader('Inventory')
st.dataframe(st.session_state.products,use_container_width=True,hide_index=True)
low=st.session_state.products[st.session_state.products.Stock<5]
st.warning(f'{len(low)} product(s) have low stock.') if len(low) else st.success('Stock levels look healthy.')

st.subheader('Point of Sale')
product=st.selectbox('Product',st.session_state.products.Product); qty=st.number_input('Quantity',1,100,1)
row=st.session_state.products[st.session_state.products.Product==product].iloc[0]
total=float(row.Price)*qty; st.metric('Total',f'৳{total:,.2f}')
if st.button('Complete sale',type='primary'):
    idx=st.session_state.products.index[st.session_state.products.Product==product][0]
    if st.session_state.products.at[idx,'Stock']>=qty:
        st.session_state.products.at[idx,'Stock']-=qty; st.success('Sale completed and inventory updated.'); st.rerun()
    else: st.error('Insufficient stock.')

with st.expander('Add product'):
    sku=st.text_input('SKU'); name=st.text_input('Product name'); price=st.number_input('Price',0.0); stock=st.number_input('Opening stock',0,10000,10)
    if st.button('Add product') and sku and name:
        st.session_state.products=pd.concat([st.session_state.products,pd.DataFrame([{'SKU':sku,'Product':name,'Price':price,'Stock':stock}])],ignore_index=True); st.rerun()
