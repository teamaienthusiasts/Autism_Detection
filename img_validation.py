import requests
from PIL import Image
import streamlit as st
import io

def validation(upl_img):
    
    # Secrets for cognitive services
    subscription_key = st.secrets["cognitive_srvs_subscription_key"]
    endpoint = st.secrets["cognitive_srvs_endpoint"]
    region = st.secrets["cognitive_srvs_region"]
    
    # Converting uploaded image to byte array
    image = Image.open(upl_img)
    img_byt_arr = io.BytesIO()
    image.save(img_byt_arr, format=image.format)
    data = img_byt_arr.getvalue()
    
    # set the request headers
    headers = dict()
    headers['Ocp-Apim-Subscription-Key'] = subscription_key
    headers['Content-Type'] = 'application/octet-stream'

    # Set request querystring parameters
    params = {'visualFeatures': 'Color,Categories,Tags,Description,ImageType,Faces,Adult'}
    #params = {'visualFeatures': 'Description,Faces'}

    # Make request and process response
    response = requests.request('post', "https://{}.api.cognitive.microsoft.com/vision/v1.0/analyze".format(region), data=data, headers=headers, params=params)
    st.write()
    # The isinstance() function returns True if the specified object is of the specified type, otherwise False .
    if response.status_code == 200 or response.status_code == 201:
        if 'content-length' in response.headers and int(response.headers['content-length']) == 0:
            result = None
        elif 'content-type' in response.headers and isinstance(response.headers['content-type'], str):
            if 'application/json' in response.headers['content-type'].lower():
                result = response.json() if response.content else None
            #elif 'image' in response.headers['content-type'].lower():
            #    result = response.content
            if len(result['faces']) == 0 or result['faces'][0]['age'] > 10 or \
               result['faces'][0]['age'] < 3 or len(result['faces']) > 1:
                img_ana_result = 'failed'
            else:
                img_ana_result = 'passed'
    else:
        img_ana_result = 'failed'
        st.error('Image analysis failed. Please find the below error code')
        st.write("Error code: %d" % response.status_code)
        st.write("Message: %s" % response.json())
    
    return img_ana_result, result