import streamlit as st
from PIL import Image
import os

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Discover Your Craft | Karigari",
    page_icon="🪡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# CUSTOM CSS
# ==========================================

st.html("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');

:root {
    --ivory: #f7f2e8;
    --cream: #fffaf2;
    --maroon: #711f1f;
    --dark: #211f1c;
    --gold: #b58a52;
    --border: #ded4c5;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: #f7f2e8;
}

[data-testid="stSidebar"] {
    display: none;
}

[data-testid="stHeader"] {
    background: transparent;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

.block-container {
    max-width: 1100px;
    padding-top: 35px;
    padding-bottom: 70px;
}

/* BRAND */

.brand {
    font-family: 'Playfair Display', serif;
    font-size: 30px;
    font-weight: 700;
    color: #211f1c;
    text-align: center;
    margin-bottom: 55px;
}

/* HEADING */

.discover-title {
    text-align: center;
    font-family: 'Playfair Display', serif;
    font-size: 52px;
    color: #211f1c;
    margin-bottom: 12px;
}

.discover-subtitle {
    text-align: center;
    color: #70675d;
    font-size: 17px;
    line-height: 1.7;
    max-width: 650px;
    margin: 0 auto 42px auto;
}

/* UPLOAD */

[data-testid="stFileUploader"] {
    background: #fffaf2;
    border: 1px solid #ded4c5;
    border-radius: 15px;
    padding: 25px;
}

[data-testid="stFileUploaderDropzone"] {
    background: #fffdf8;
    border: 2px dashed #bcae9c;
    border-radius: 12px;
    padding: 38px 20px;
}

[data-testid="stFileUploaderDropzone"]:hover {
    border-color: #711f1f;
}

/* IMAGE PREVIEW */

[data-testid="stImage"] img {
    border-radius: 14px;
    border: 1px solid #ded4c5;
}

/* BUTTON */

.stButton > button {
    width: 100%;
    background: #711f1f;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 14px 20px;
    font-size: 16px;
    font-weight: 600;
    transition: 0.2s;
}

.stButton > button:hover {
    background: #541616;
    color: white;
    border: none;
}

/* INFO */

.info-box {
    background: #efe5d6;
    border-radius: 12px;
    padding: 24px 28px;
    margin-top: 35px;
}

.info-box h3 {
    font-family: 'Playfair Display', serif;
    margin-top: 0;
    color: #211f1c;
}

.info-box p {
    color: #665d54;
    line-height: 1.7;
    margin-bottom: 0;
}

/* CATEGORIES */

.categories-title {
    font-family: 'Playfair Display', serif;
    text-align: center;
    font-size: 28px;
    margin-top: 55px;
}

.category-row {
    text-align: center;
    color: #766b60;
    line-height: 2;
    max-width: 850px;
    margin: auto;
}

.category-pill {
    display: inline-block;
    padding: 7px 13px;
    margin: 5px;
    border: 1px solid #d6c9b8;
    background: #fffaf2;
    border-radius: 50px;
    font-size: 13px;
}

/* BACK LINK */

.back-link {
    text-align: center;
    margin-top: 45px;
}

.back-link a {
    color: #711f1f;
    text-decoration: none;
    font-weight: 600;
}

</style>
""")


# ==========================================
# PAGE HEADER
# ==========================================

st.html("""
<div class="brand">
    ✤ Karigari
</div>

<h1 class="discover-title">
    Discover Your Craft
</h1>

<p class="discover-subtitle">
    Upload a photograph of traditional clothing, embroidery,
    textile or craftwork. Karigari will examine its visual
    patterns and help identify the tradition behind it.
</p>
""")


# ==========================================
# FILE UPLOADER
# ==========================================

uploaded_file = st.file_uploader(
    "Upload your photograph",
    type=["jpg", "jpeg", "png", "webp"],
    help="Supported formats: JPG, JPEG, PNG and WEBP"
)


# ==========================================
# IMAGE PREVIEW
# ==========================================

if uploaded_file is not None:

    try:

        image = Image.open(uploaded_file)

        st.write("")

        left, center, right = st.columns([1, 2, 1])

        with center:

            st.image(
                image,
                caption="Your uploaded photograph",
                use_container_width=True
            )

            identify_button = st.button(
                "Identify This Craft",
                type="primary"
            )

        # ==================================
        # TEMPORARY MODEL PLACEHOLDER
        # ==================================

        if identify_button:

            # Store uploaded image temporarily
            os.makedirs("data/uploads", exist_ok=True)

            image_path = os.path.join(
                "data",
                "uploads",
                "current_upload.png"
            )

            image.convert("RGB").save(image_path)

            # Store path for result page
            st.session_state["uploaded_image_path"] = image_path

            st.session_state["prediction_ready"] = False

            st.info(
                "Image received successfully. "
                "The Deep Learning model will be connected in the next step."
            )

    except Exception:

        st.error(
            "This image could not be read. "
            "Please upload another JPG, PNG or WEBP photograph."
        )


# ==========================================
# SUPPORTED CRAFTS
# ==========================================

st.html("""
<h2 class="categories-title">
    What can Karigari recognise?
</h2>

<div class="category-row">

    <span class="category-pill">Banarasi</span>
    <span class="category-pill">Chikankari</span>
    <span class="category-pill">Phulkari</span>
    <span class="category-pill">Kalamkari</span>
    <span class="category-pill">Ajrakh</span>
    <span class="category-pill">Bandhani</span>
    <span class="category-pill">Kantha</span>
    <span class="category-pill">Paithani</span>
    <span class="category-pill">Ikat</span>
    <span class="category-pill">Madhubani</span>
    <span class="category-pill">Warli</span>
    <span class="category-pill">Zardozi</span>
    <span class="category-pill">Kashida</span>
    <span class="category-pill">Pattachitra</span>
    <span class="category-pill">Bagh</span>
    <span class="category-pill">Chanderi</span>
    <span class="category-pill">Pithora</span>
    <span class="category-pill">Toda</span>

</div>
""")


# ==========================================
# HOW IT WORKS
# ==========================================

st.html("""
<div class="info-box">

    <h3>
        How identification works
    </h3>

    <p>
        Karigari uses a deep-learning image classification model
        trained on visual characteristics of Indian traditional
        crafts. The system analyses patterns, embroidery,
        weaving characteristics, colours and surface details
        before estimating the most likely craft tradition.
    </p>

</div>

<div class="back-link">
    <a href="/">
        ← Back to Karigari
    </a>
</div>
""")