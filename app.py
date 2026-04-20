import streamlit as st
from api_calling import note_genarator,audio_transcription,quiz_generator
from PIL import Image
from gtts import gTTS

st.title("Note Summary and Quiz Genarator")
st.markdown("Upload upto 3 images to genarate Note Summary and Quizes")
st.divider()

with st.sidebar:
    st.header("Controls")

    # Image
    images = st.file_uploader("Upload the photos of your note",type=['jpg','jpeg','png'],accept_multiple_files=True)

    if images:


        pill_images= []

        for img in images:
            pill_img = Image.open(img)
            pill_images.append(pill_img)

        if (len (images)>3):
            st.warning("Upload at max 3 photos")
        else:
            st.subheader("Your Uploaded image")
            col = st.columns(len(images))

            st.subheader("Your Uploaded image")

            for i,img in enumerate(images):
                with col[i]:
                    st.image(img)

# difficulty 

    selected_option = st.selectbox( 
        "Enter the difficulty of your quiz",
        ("Easy","Medium","Hard"),
        index = None
    )
    # if selected_option:
    #     st.markdown(f"You selected **{selected_option}**")
    # else:
    #     st.error("You must select a difficulty")


    pressed = st.button("Click the button to initiate AI",type="primary")


if pressed:
    if not images:
        st.error("You must upload 1 image")
    if not selected_option:
        st.error("You must select a difficulty")
    if images and selected_option:


        with st.container(border=True):
            st.subheader("Your Note")

            with st.spinner("Ai is writing notes for you"):
                genarated_notes = note_genarator(pill_images)
                st.markdown(genarated_notes)



        with st.container(border=True):
            st.subheader("Audio Transcription")

            with st.spinner("Ai is writing notes for you"):

                genarated_notes = genarated_notes.replace("#","")
                genarated_notes = genarated_notes.replace("*","")
                genarated_notes = genarated_notes.replace("-","")
                genarated_notes = genarated_notes.replace("`","")

                audio_transcript = audio_transcription(genarated_notes)
                st.audio(audio_transcript)



        with st.container(border=True):
            st.subheader(f"Quiz ({selected_option} Difficulty)")
            with st.spinner("Ai is writing notes for you"):
                quizzes = quiz_generator(pill_images,selected_option)
                st.markdown(quizzes)