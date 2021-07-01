from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient as CVTC
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
from msrest.authentication import ApiKeyCredentials
import io
from numpy import random
from PIL import Image
import streamlit as st

def tagging(pred_image, pred_tag):

    # Secrets for custom vision services 
    ENDPOINT = st.secrets["cust_vision_endpoint"]
    training_key = st.secrets["cust_vision_training_key"]
    project_id = st.secrets["cust_vision_project_id"]
    iteration_id = st.secrets["cust_vision_iteration_id"]

    credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})
    trainer = CVTC(ENDPOINT, credentials)
    
    # get tags
    tag = trainer.get_tags(project_id,  iteration_id)
    
    # get_tag_ids
    for i in tag:
        print(i)
        if i.name == 'Non Autistic':
            non_autistic_tag_id = i.id
        if i.name == 'Autistic':
            autistic_tag_id = i.id

    # converting the image to byte array
    image = Image.open(pred_image)
    img_byt_arr = io.BytesIO()
    image.save(img_byt_arr, format=image.format)
    img_byt_arr = img_byt_arr.getvalue()
    
    # attach the predicted image and tag for upload
    image_list = []
    image_num =random.randint(50)
    if pred_tag == 'Autistic':
        file_name = "pred_autistic_{}.jpg".format(image_num)
        image_list.append(ImageFileCreateEntry(name=file_name, contents=img_byt_arr, 
                            tag_ids=[autistic_tag_id]))
    
    if pred_tag == 'Non Autistic':
        file_name = "pred_non_autistic_{}.jpg".format(image_num)
        image_list.append(ImageFileCreateEntry(name=file_name, contents=img_byt_arr, 
                            tag_ids=[non_autistic_tag_id]))
                            
    # upload image
    upload_result = trainer.create_images_from_files(project_id, ImageFileCreateBatch(images=image_list))
    print(upload_result)
    if not upload_result.is_batch_successful:
        st.error("Image upload failed. Please check the below error")
        for image in upload_result.images:
            st.error("Image status: ", image.status)
            exit(-1)
    else:
        st.info("Image has been uploaded successfully!")
    

    


