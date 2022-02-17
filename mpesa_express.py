import streamlit as st 

header = st.container()
body1 = st.container()
body2 = st.container()

with header:
	st.title('Lipa na Mpesa')
	st.subheader('Mpesa Express API')
	st.text('Merchant initiated online payment')

with body1:
	with st.form(key='stk_push'):
		st.markdown('Mpesa STK Push')
		amount = st.text_input(label='amount')
		phone = st.text_input(label='phone number')
		submit = st.form_submit_button(label='proceed payment')


with body2:
	col1, col2 = st.columns(2)

	with col1:
		with st.form(key='buygoodsonline'):
			st.markdown('Buy Goods Online')
			st.write('Till number	234189')
			amount = st.text_input(label='amount')
			phone = st.text_input(label='phone number')
			submit = st.form_submit_button(label='proceed payment')

	with col2:
		with st.form(key='paybillonline'):
			st.markdown('Paybill Online')
			st.write('Business no. 	206206')
			amount = st.text_input(label='amount')
			phone = st.text_input(label='phone number')
			submit = st.form_submit_button(label='proceed payment')		

