import wandb
import streamlit as st
from .. import plot_result, download_dataset, Trainer


def train_app_module():
    initialize_wandb = st.selectbox('Initialize Wandb?', ('', 'No', 'Yes'))
    if initialize_wandb == 'Yes':
        project_name = st.sidebar.text_input('Wandb Project Name', '')
        experiment_name = st.sidebar.text_input('Experiment Name', '')
        wandb_api_key = st.sidebar.text_input('Wandb API Key', '')
        if st.sidebar.button('Submit'):
            from ..utils import init_wandb
            init_wandb(
                project_name=project_name,
                experiment_name=experiment_name,
                wandb_api_key=wandb_api_key
            )
            wandb_url = str(wandb.run.url)
            st.markdown(
                '<strong>Track your experiment at </strong><a href="{}" target="_blank">{}</a>'.format(wandb_url, wandb_url),
                unsafe_allow_html=True
            )
            st.text_input('Done!!!')
            initialize_wandb = 'No'
    if initialize_wandb == 'No':
        st.text('Fetching Dataset...')
        dataset_option = st.selectbox(
            'Select your Dataset:', (
                '', 'Zero-DCE Dataset', 'Dark Face Dataset'
            )
        )
        if dataset_option == 'Zero-DCE Dataset':
            download_dataset(dataset_tag='zero_dce')
        elif dataset_option == 'Dark Face Dataset':
            download_dataset(dataset_tag='dark_face')
