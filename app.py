import streamlit as st
from intro import intro
from img_processing import processing
from references import refer
from img_try_on import try_on

if __name__ == '__main__':

    st.header('Autism Detection using Children Facial expression')
    st.sidebar.title('Options:')
    sidebar_selector = st.sidebar.radio('Use the Below Options',
                                       ('About ASD', 'Try the App', 'Autism Detection App','References'))
    st.sidebar.header("Help:")
    st.sidebar.info("Please click the '+' sign to expand the sections.")
    st.sidebar.header("Authors:")
    st.sidebar.warning("AI_Enthusiats")
    st.sidebar.header("Language:")
    st.sidebar.info("Python")
    st.sidebar.header("Packages:")
    st.sidebar.info("Azure Cognitive Services. \n\n"
                    "Azure Custom Vision. \n\n"
                    "TensorFlow. \n\n"
                    "Streamlit.\n\n"
                    "Pillow.")
    
    # About ASD section
    if sidebar_selector == ('About ASD'):
        intro()

    # Sample Image testing section
    if sidebar_selector == ('Try the App'):
        try_on()

    # Autism Detection section
    if sidebar_selector == ('Autism Detection App'):
        processing()
    
    # Reference Section    
    if sidebar_selector == ('References'):
        refer()
