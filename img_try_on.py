import streamlit as st
import streamlit as st
from PIL import Image
from img_validation import validation
from img_prediction import predict

def try_on_img_prs(try_on_img):

    image_url = st.image(try_on_img, caption='Selected Image', use_column_width=True)
    img_validation, result = validation(try_on_img)
    st.subheader("Image characteristics")
    
    if len(result['faces']) != 0:
        st.info("Age     : " + str(result['faces'][0]['age']) + '\n\n' +
                "Gender  : " + str(result['faces'][0]['gender']) + "\n\n" +
                "Caption : " + str(result['description']['captions'][0]['text']))
    else:
         ani_predictions = []
         for i in result['tags']:
             ani_predictions.append([i['name'], "{:.2%}".format(i['confidence'])])
         st.info("The Image contents prediction and its accuracy percentage displayed below.")
         st.warning(ani_predictions)
         st.info("Image caption: \n\n" + result['description']['captions'][0]['text'])
               
    # Predicting the uploaded Image
    st.subheader("Image Validation Results")
    if img_validation == 'passed':        
        st.info("Selected image validation completed and its passed the validation. \n"
                "Now the prediction process begins ->->->->->->")
        pred_results, acc = predict(try_on_img)
        st.subheader("Image Prediction Results")
        st.info("Model has been predicted the selected child image as " + pred_results + "\n\n" +
                 "Accuracy of the above results are " + "{:.2%}".format(acc))
        st.write("                                ")
        st.write("                                ")
    elif img_validation == 'failed':
        st.error("Error: Image validation failed due to anyone of the following reasons. \n\n"
                 "1. Image contains group of children. \n\n"
                 "2. Its a image of a single adult or group of adult or group of children \
                     and adults. \n\n"
                 "3. Image contains children aged less than 3 or more than 10. \n\n"
                 "4. Selected image is not a human facial image.\n\n"
                 "5. Selected image is a blurred image.")                    

def try_on():

    st.warning("This section of the Application can be used to select sample images and see the predictions \
                without uploading the actual images. You can select the image categories from the below dropdown. \
                Based on that, images will be displayed for testing the app. Then select the image \
                you want to test and see it in action. Please make yourself comfortable before using \
                the app.")
    st.subheader('Image Categories')
    img_slt_box = st.selectbox("Please select the image categories to select images for testing", 
                              (" ", "Adults", "Kids", "Others"))
    
    if img_slt_box == "Adults":
        
        adlt_col1, adlt_col2 = st.beta_columns(2)

        with adlt_col1:
            st.subheader("Image_1")
            st.image("image_1.jpg")
            img1_clk = st.button("Select_Image_1")

            st.subheader("Image_2")
            st.image("image_2.jpg")
            img2_clk = st.button("Select_Image2")

            st.subheader("Image_3")
            st.image("image_3.jpg")
            img3_clk = st.button("Select_Image3")
        
        with adlt_col2:
            st.subheader("Image_4")
            st.image("image_4.jpg")
            img4_clk = st.button("Select_Image_4")

            st.subheader("Image_5")
            st.image("image_5.jpg")
            img5_clk = st.button("Select_Image_5")

            st.subheader("Image_6")
            st.image("image_6.jpg")
            img6_clk = st.button("Select_Image_6")
                   
        if img1_clk:
            try_on_img_prs("image_1.jpg")
        elif img2_clk:
            try_on_img_prs("image_2.jpg")
        elif img3_clk:
            try_on_img_prs("image_3.jpg")
        elif img4_clk:
            try_on_img_prs("image_4.jpg")
        elif img5_clk:
            try_on_img_prs("image_5.jpg")
        elif img6_clk:
            try_on_img_prs("image_6.jpg")

    elif img_slt_box == "Kids":

        kds_col1, kds_col2, kds_col3 = st.beta_columns(3)

        with kds_col1:
            st.subheader("Image_1")
            st.image("kds_image_1.jpg")
            kds_img1_clk = st.button("Select_Image_1")
            
            st.subheader("Image_2")
            st.image("kds_image_2.jpg")
            kds_img2_clk = st.button("Select_Image_2")  
            
            st.subheader("Image_3")
            st.image("kds_image_3.jpg")
            kds_img3_clk = st.button("Select_Image_3")

            st.subheader("Image_4")
            st.image("kds_image_4.jpg")
            kds_img4_clk = st.button("Select_Image_4")

            st.subheader("Image_5")
            st.image("kds_image_5.jpg")
            kds_img5_clk = st.button("Select_Image_5")    

        with kds_col2:
            st.subheader("Image_6")
            st.image("kds_image_6.jpg")
            kds_img6_clk = st.button("Select_Image_6")

            st.subheader("Image_7")
            st.image("kds_image_7.jpg")
            kds_img7_clk = st.button("Select_Image_7")

            st.subheader("Image_8")
            st.image("kds_image_8.jpg")
            kds_img8_clk = st.button("Select_Image_8")

            st.subheader("Image_9")
            st.image("kds_image_9.jpg")
            kds_img9_clk = st.button("Select_Image_9")

            st.subheader("Image_10")
            st.image("kds_image_10.jpg")
            kds_img10_clk = st.button("Select_Image_10")  

        with kds_col3:
            st.subheader("Image_11")
            st.image("kds_image_11.jpg")
            kds_img11_clk = st.button("Select_Image_11")
            
            st.subheader("Image_12")
            st.image("kds_image_12.jpg")
            kds_img12_clk = st.button("Select_Image_12")

            st.subheader("Image_13")
            st.image("kds_image_13.jpg")
            kds_img13_clk = st.button("Select_Image_13")

            st.subheader("Image_14")
            st.image("kds_image_14.jpg")
            kds_img14_clk = st.button("Select_Image_14")

            st.subheader("Image_15")
            st.image("kds_image_15.jpg")
            kds_img15_clk = st.button("Select_Image_15")  
        
        if kds_img1_clk:
            try_on_img_prs("kds_image_1.jpg")
        elif kds_img2_clk:
            try_on_img_prs("kds_image_2.jpg")
        elif kds_img3_clk:
            try_on_img_prs("kds_image_3.jpg")
        elif kds_img4_clk:
            try_on_img_prs("kds_image_4.jpg")
        elif kds_img5_clk:
            try_on_img_prs("kds_image_5.jpg")
        elif kds_img6_clk:
            try_on_img_prs("kds_image_6.jpg")
        elif kds_img7_clk:
            try_on_img_prs("kds_image_7.jpg")
        elif kds_img8_clk:
            try_on_img_prs("kds_image_8.jpg")
        elif kds_img9_clk:
            try_on_img_prs("kds_image_9.jpg")
        elif kds_img10_clk:
            try_on_img_prs("kds_image_10.jpg")
        elif kds_img11_clk:
            try_on_img_prs("kds_image_11.jpg")
        elif kds_img12_clk:
            try_on_img_prs("kds_image_12.jpg")
        elif kds_img13_clk:
            try_on_img_prs("kds_image_13.jpg")
        elif kds_img14_clk:
            try_on_img_prs("kds_image_14.jpg")
        elif kds_img15_clk:
            try_on_img_prs("kds_image_15.jpg")
    
    elif img_slt_box == "Others":

        oths_col1, oths_col2 = st.beta_columns(2)

        with oths_col1:
            st.subheader("Image_1")
            st.image("ani_image_1.jpg")
            ani_img1_clk = st.button("Select_Image_1")

            st.subheader("Image_2")
            st.image("ani_image_2.jpg")
            ani_img2_clk = st.button("Select_Image_2")

            st.subheader("Image_3")
            st.image("ani_image_3.jpg")
            ani_img3_clk = st.button("Select_Image_3")
        
        with oths_col2:
            st.subheader("Image_4")
            st.image("ani_image_4.jpg")
            ani_img4_clk = st.button("Select_Image_4")

            st.subheader("Image_5")
            st.image("ani_image_5.jpg")
            ani_img5_clk = st.button("Select_Image_5")

            st.subheader("Image_6")
            st.image("ani_image_6.jpg")
            ani_img6_clk = st.button("Select_Image_6")
        
        if ani_img1_clk:
            try_on_img_prs("ani_image_1.jpg")
        elif ani_img2_clk:
            try_on_img_prs("ani_image_2.jpg")
        elif ani_img3_clk:
            try_on_img_prs("ani_image_3.jpg")
        elif ani_img4_clk:
            try_on_img_prs("ani_image_4.jpg")
        elif ani_img5_clk:
            try_on_img_prs("ani_image_5.jpg")
        elif ani_img6_clk:
            try_on_img_prs("ani_image_6.jpg")