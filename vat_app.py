import streamlit as st
st.header(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): **{vat:.2f}** บาท"
price = st.number_input("กรอกราคาสินค้า (บาท):", value=0.0
vat = price * 0.07
net_price = price - vat
st.header(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): **{vat:.2f}** บาท")
st.header(f"• ราคาสุทธิ: {net_price:.2f} บาท")
st.divider()
st.write("นายอาณาจักร รุ่งเรือง เลขที่ 1  ม.4/6")
