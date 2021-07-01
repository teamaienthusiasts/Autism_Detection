import streamlit as st
from PIL import Image

def intro():
    
    # Intro Section 0
    st.write("                                ")
    top_sec_img1 = "top_sec_img1.jpg"   
    top_sec_pil_img1 = Image.open(top_sec_img1)
    top_sec_img1_url = st.image(top_sec_pil_img1, caption=' ', use_column_width=True)

    # Intro Section 1
    st.write("                                ")
    intro_sec1 = st.beta_expander("What is Autism", expanded=False)
    intro_sec1_img1 = "intro_sec1_img1.jpg"
    intro_sec1_img2 = "intro_sec1_img2.jpg"
    with intro_sec1:
        st.write("Autism, or autism spectrum disorder (ASD), refers to a broad \
                range of conditions characterized by challenges with social \
                skills, repetitive behaviors, speech and nonverbal communication. \
                According to the Centers for Disease Control, autism affects an  \
                estimated 1 in 54 children in the United States today. \
                This App will detect if the child is having autism or not using \
                Azure Image classification method.")
        intro_sec1_img_col1, intro_sec1_img_col2 = st.beta_columns(2)
        intro_sec1_pil_img1 = Image.open(intro_sec1_img1)
        intro_sec1_img_col1.header("    ")
        intro_sec1_img_col1.image(intro_sec1_pil_img1, use_column_width=True)

        intro_sec1_pil_img2 = Image.open(intro_sec1_img2)
        intro_sec1_img_col2.header("    ")
        intro_sec1_img_col2.image(intro_sec1_pil_img2, use_column_width=True)       
    
    # Intro Section 2
    st.write("                                ")
    intro_sec2 = st.beta_expander("What are the Causes of Autism", expanded=False)
    intro_sec2_img1 = "intro_sec2_img1.jpg"
    intro_sec2_img2 = "intro_sec2_img2.jpg"
    with intro_sec2:
        st.write("1. Research indicates that genetics are involved in the vast majority of cases. \n"
                 "2. Children born to older parents are at a higher risk for having autism. \n"
                 "3. Parents who have a child with ASD have a 2 to 18 percent chance of \
                     having a second child who is also affected.  \n"
                 "4. Studies have shown that among identical twins, if one child has autism, \
                     the other will be affected about 36 to 95 percent of the time. \n" 
                 "5. In non-identical twins, if one child has autism, then the other is affected about \
                     31 percent of the time. \n"
                 "6. Over the last two decades, extensive research has asked whether there is any   \
                     link between childhood vaccinations and autism. The results of this research   \
                     are clear Vaccines do not cause autism. ") 
        intro_sec2_img_col1, intro_sec2_img_col2 = st.beta_columns(2)
        intro_sec2_pil_img1 = Image.open(intro_sec2_img1)
        intro_sec2_img_col1.header("       ")
        intro_sec2_img_col1.image(intro_sec2_pil_img1, use_column_width=True)
        
        intro_sec2_pil_img2 = Image.open(intro_sec2_img2)
        intro_sec2_img_col2.header("       ")
        intro_sec2_img_col2.image(intro_sec2_pil_img2, use_column_width=True)
    
    # Intro Section 3
    st.write("                                ")
    intro_sec3 = st.beta_expander("Signs of Autism", expanded=False)
    intro_sec3_img1 = "intro_sec3_img1.jpeg"
    intro_sec3_img2 = "intro_sec3_img2.jpg"
    with intro_sec3:
        intro_sec3_img_col1, intro_sec3_img_col2 = st.beta_columns(2)
        intro_sec3_pil_img1 = Image.open(intro_sec3_img1)
        intro_sec3_img_col1.header("     ")
        intro_sec3_img_col1.image(intro_sec3_pil_img1, use_column_width=True)
        
        intro_sec3_pil_img2 = Image.open(intro_sec3_img2)
        intro_sec3_img_col2.header("      ")
        intro_sec3_img_col2.image(intro_sec3_pil_img2, use_column_width=True)

    # Intro Section 4
    st.write("                                ")
    intro_sec4 = st.beta_expander("Autism Prevalence", expanded=False) 
    with intro_sec4:
        st.write("1. In 2020, the CDC reported that approximately 1 in 54 children in the U.S. \
                     is diagnosed with an autism spectrum disorder (ASD), according to 2016 data. \n" 
                 "2. Boys are four times more likely to be diagnosed with autism than girls. \n"
                 "3. Most children were still being diagnosed after age 4, though autism can be \
                     reliably diagnosed as early as age 2. \n"
                 "4. 31 percent of children with ASD have an intellectual disability (intelligence quotient [IQ] <70), \
                     25 percent are in the borderline range (IQ 71–85), and 44 percent have IQ scores in the average \
                     to above average range (i.e., IQ >85). \n"
                 "5. Autism affects all ethnic and socioeconomic groups. Minority groups tend to \
                     be diagnosed later and less often. \n"
                 "6. Early intervention affords the best opportunity to support healthy development \
                     and deliver benefits across the lifespan There is no medical detection for autism.") 
    
    # Intro Section 5
    st.write("                                ")
    intro_sec5 = st.beta_expander("Autism Intervention and Support", expanded=False)
    intro_sec5_img1 = "intro_sec5_img1.jpg"
    intro_sec5_img2 = "intro_sec5_img2.jpg"
    with intro_sec5:
        intro_sec5_img_col1, intro_sec5_img_col2 = st.beta_columns(2)
        intro_sec5_pil_img1 = Image.open(intro_sec5_img1)
        intro_sec5_img_col1.header("       ")
        intro_sec5_img_col1.image(intro_sec5_pil_img1, use_column_width=True)
        
        intro_sec5_pil_img2 = Image.open(intro_sec5_img2)
        intro_sec5_img_col2.header("       ")
        intro_sec5_img_col2.image(intro_sec5_pil_img2, use_column_width=True)
        st.write("1. Early intervention can improve learning, communication and social skills, \
                     as well as underlying brain development. \n" 
                 "2. Applied behavior analysis (ABA) and therapies based on its principles are \
                     the most researched and commonly used behavioral interventions for autism. \n"
                 "3. Many children affected by autism also benefit from other interventions \
                     such as speech and occupational therapy. \n"
                 "4. Developmental regression, or loss of skills, such as language and social \
                     interests, affects around 1 in 5 children who will go on to be diagnosed \
                     with autism and typically occurs between ages 1 and 3.") 
    
    # Video Section
    st.write("                                ")
    intro_sec6 = st.beta_expander("Generic Information Video on ASD", expanded=False)
    with intro_sec6:
        st.video('https://www.youtube.com/watch?v=6jUv3gDAM1E')