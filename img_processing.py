import streamlit as st
from PIL import Image
from img_validation import validation
from img_tagging import tagging
from img_prediction import predict

def processing():

    sam_mle = 'sample_male.jpg'
    sam_fmle = 'sample_female.jpg'
    i_agree = 'I Agree and Acknowledge the above statement. I give my concent.'
    i_disagree = 'I Disagree the above statement.'

    app_discl = st.beta_expander("Application Disclaimer", expanded=True)
    with app_discl:
         st.warning("The materials and information provided by this application are for educational \
                     and informational purposes only and are not intended to substitute for consulting \
                     with licensed medical or educational professionals in diagnosis and/or intervention \
                     with Autism Spectrum Disorder (ASD) or other developmental disability.\n\n"
                    
                    "This AI based application has been created to help parents to do preliminary in \
                     home detection of Autism Spectrum Disorder (ASD) in their children. This application \
                     can distinguish between autistic and non-autistic behavior of a child using their \
                     facial expression from the uploaded image.\n\n"
                     
                    "The application has been trained using sample facial images of children with or \
                     without Autism Spectrum Disorder (ASD). The application has a success rate of 79 \
                     percent in predicting autism. It can provide 'NEGATIVE PREDICTIONS' as well. \
                     The application validates the uploaded image against the below specifications.\n\n"
                             
                        "* Single child's facial image. \n\n"
                        "* Child should be aged greater than 3 and less than 10 years. \n\n"
                        "* Reject Images with group of children or adults. \n\n"
                        "* Reject Images of Adults. \n\n"

                    "Please understand and acknowledge this statement to continue the application.")
    st.write("                                ")
    st.write("                                ")
    app_disc_sel_box = st.selectbox("Please select the below dropdown options to \
                                    proceed futher", (" ", i_agree, i_disagree))          
    st.write("                                ")
    st.write("                                ")
    if app_disc_sel_box == i_agree:
        with st.spinner("Prediction Process begins. Please upload your child's facial image"):
            
            # providing sample image
            st.info('Please the refer sample images if you have any questions')     
            
            img_col1, img_col2 = st.beta_columns(2)
            sam_mle_img = Image.open(sam_mle)
            img_col1.header("Sample_1")
            img_col1.image(sam_mle_img, use_column_width=True)

            sam_fmle_img = Image.open(sam_fmle)
            img_col2.header("Sample_2")
            img_col2.image(sam_fmle_img, use_column_width=True)

            # getting the image from the user for processing
            up_file = st.file_uploader("Upload your Child's Facial Image", type='jpg')
            if up_file is not None:
                up_image = Image.open(up_file)
                image_url = st.image(up_image, caption='Uploaded Image', use_column_width=True)
                                
                # Validating, Analyzing and Printing Image characteristics
                img_validation, result = validation(up_file)
                st.subheader("Image characteristics")
                if len(result['faces']) != 0:
                    st.info("Age     : " + str(result['faces'][0]['age']) + '\n\n' +
                            "Gender  : " + str(result['faces'][0]['gender']) + "\n\n" +
                            "Caption : " + str(result['description']['captions'][0]['text']))
                else:
                    ani_predictions = []
                    for i in result['tags']:
                        ani_predictions.append([i['name'], "{:.2%}".format(i['confidence'])])
                    st.info("The Image contents prediction and its percentage")
                    st.warning(ani_predictions)
                    st.info("Image caption: \n\n" + result['description']['captions'][0]['text'])

                st.subheader("Image Validation Results")
                if img_validation == 'passed':
                    st.info("Uploaded image validation completed and its passed the validation. \n"
                            "Now the prediction process begins ->->->->->->")
                
                    # Predicting and Printing the Image prediction results
                    pred_results, acc = predict(up_file)
                    st.subheader("Image Prediction Results")
                    st.info("Model has been predicted the selected child image as " + pred_results + "\n\n" +
                            "Accuracy of the above results are " + "{:.2%}".format(acc))
                    if pred_results == 'Autistic':
                        st.warning("Since the uploaded image has been predicted as an Autistic image, \
                                    Please contact Heathcare Professional for further assistance")
                    
                    # Adding the user uploaded image to training set based on the predictions results
                    st.subheader("Image Usage")
                    app_data_discl = st.beta_expander("Image Usage Disclaimer", expanded=True)
                    with app_data_discl:
                        st.warning("Are you giving concent to store your child's image for \
                                    future model tuning?")
                    st.write("                                ")
                    st.write("                                ")
                    app_data_disc_sel_box = st.selectbox("Please select the below dropdown options to \
                                                          proceed futher", (" ", i_agree, i_disagree))
                    st.write("                                ")
                    if app_data_disc_sel_box == i_agree:
                        tagging(up_file, pred_results)
                        st.info("Thank you for providing the concent. Your child image has been stored \
                                 and it will be used for model training in future iterations.")
                    elif app_data_disc_sel_box == i_disagree:
                        st.info("Thank you for using our AI application.")            
                    
                elif img_validation == 'failed':
                    st.error("Error: Image validation failed due to anyone of the following reasons. \n\n"
                                 "1. Image contains group of children. \n\n"
                                 "2. Its a image of a single adult or group of adult or group of children \
                                     and adults. \n\n"
                                 "3. Image contains children aged less than 3 or more than 10. \n\n"
                                 "4. Uploaded image is not a human facial image.\n\n"
                                 "5. Uploaded image is a blurred image.")                   
    elif app_disc_sel_box == i_disagree:
        st.info("Thank you for considering our AI application.")
