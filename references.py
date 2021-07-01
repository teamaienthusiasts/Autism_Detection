import streamlit as st
from PIL import Image

def refer():

    st.subheader("Project References")
    
    st.write("                                ")
    refer_sec0 = st.beta_expander("User Interface", expanded=False)
    with refer_sec0:
        st.write("https://streamlit.io/")

    st.write("                                ")
    refer_sec1 = st.beta_expander("Kaggle Dataset", expanded=False)
    with refer_sec1:
        st.write("https://www.kaggle.com/gpiosenka/autistic-children-data-set-traintestvalidate")
    
    st.write("                                ")   
    refer_sec2 = st.beta_expander("Image Upload & Model Training", expanded=False)
    with refer_sec2:
        st.write("https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/getting-started-build-a-classifier")

    st.write("                                ")
    refer_sec3 = st.beta_expander("Image Tagging", expanded=False)
    with refer_sec3:
        st.write("https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/quickstarts/image-classification?tabs=visual-studio&pivots=programming-language-python")

    st.write("                                ")
    refer_sec4 = st.beta_expander("Tensorflow Model Execution", expanded=False)
    with refer_sec4:
        st.write("https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/export-model-python")
    
    st.write("                                ")
    refer_sec5 = st.beta_expander("Image Validation", expanded=False)
    with refer_sec5:
        st.write("https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/quickstarts-sdk/image-analysis-client-library?tabs=visual-studio&pivots=programming-language-python")
    
    st.write("                                ")
    refer_sec6 = st.beta_expander("Model Deployment", expanded=False)
    with refer_sec6:
        st.write("https://streamlit.io/sharing")
    
    st.write("                                ")
    refer_sec7 = st.beta_expander("Images", expanded=False)
    with refer_sec7:
        st.write("https://www.pexels.com/")