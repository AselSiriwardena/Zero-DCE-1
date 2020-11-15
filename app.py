import streamlit as st
from zero_dce.streamlit_app import train_app_module


def demo_app():
    st.markdown('# Zero-DCE')
    st.markdown('Zero-Reference Deep Curve Estimation for Low-Light Image Enhancement')
    st.markdown('<hr />', unsafe_allow_html=True)
    option = st.selectbox(
        'Select your action:', (
            '', 'Train a Low-Light Image Enhancement Model',
            'Infer from a Low-Light Image Enhancement Model'
        )
    )
    if option == 'Train a Low-Light Image Enhancement Model':
        train_app_module()
    elif option == 'Infer from a Low-Light Image Enhancement Model':
        st.warning('Under Development')
    elif option != '':
        st.error('Garbar Ghotala!!!')


if __name__ == '__main__':
    demo_app()
