import streamlit as st
from utils.gemini import generate_content

# ==========================================
# Page Configuration
# ==========================================
st.set_page_config(
    page_title="PhotoPilot AI",
    page_icon="📸",
    layout="centered"
)

# ==========================================
# Custom CSS
# ==========================================
st.markdown("""
<style>

.main-title{
    text-align:center;
    font-size:42px;
    font-weight:bold;
    color:#ff4b4b;
}

.sub-title{
    text-align:center;
    color:gray;
    font-size:18px;
    margin-bottom:25px;
}

.result-box{
    background:#262730;
    padding:18px;
    border-radius:12px;
    border:1px solid #444;
    margin-bottom:15px;
}

.footer{
    text-align:center;
    color:gray;
    margin-top:50px;
    font-size:14px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# Header
# ==========================================

st.markdown(
    "<div class='main-title'>📸 PhotoPilot AI</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>AI Powered Photography Assistant</div>",
    unsafe_allow_html=True
)

# ==========================================
# Upload
# ==========================================

uploaded_image = st.file_uploader(
    "Upload your image",
    type=["jpg", "jpeg", "png"]
)

# ==========================================
# Main Section
# ==========================================

if uploaded_image is not None:

    st.image(
        uploaded_image,
        use_container_width=True
    )

    st.success("Image uploaded successfully!")

    if st.button("✨ Analyze Image", use_container_width=True):

        try:

            with st.spinner("🤖 AI is analyzing your image..."):

                caption, description = generate_content(uploaded_image)

            st.divider()

            st.subheader("📷 Caption")

            st.markdown(
                f"""
<div class="result-box">

{caption}

</div>
""",
                unsafe_allow_html=True
            )

            st.subheader("📝 Description")

            st.markdown(
                f"""
<div class="result-box">

{description}

</div>
""",
                unsafe_allow_html=True
            )

            output = f"""

Caption

{caption}


Description

{description}

"""

            st.download_button(

                "⬇ Download Result",

                output,

                file_name="photo_description.txt",

                mime="text/plain",

                use_container_width=True

            )

        except Exception as e:

            st.error(f"❌ {e}")

# ==========================================
# Footer
# ==========================================

st.markdown(
"""
<div class='footer'>

Made with ❤️ using Streamlit & Gemini AI

</div>
""",
unsafe_allow_html=True
)