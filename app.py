import streamlit as st
import requests
from PIL import Image
import io
import base64
import os


from data.craft_info import CRAFTS
from data.artisans import ARTISANS, CRAFT_ARTISANS

# ============================================================
# CONFIG
# ============================================================

st.set_page_config(
    page_title="Karigari | India's Living Craft Heritage",
    page_icon="🪡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

API_URL = "https://displease-impure-trapping.ngrok-free.dev/predict"

CONFIDENCE_THRESHOLD = 55.0


# ============================================================
# HELPERS
# ============================================================

def image_to_base64(path):

    if not os.path.exists(path):
        return ""

    with open(path, "rb") as f:
        encoded = base64.b64encode(
            f.read()
        ).decode()

    ext = os.path.splitext(path)[1].lower()

    mime = "image/jpeg"

    if ext == ".png":
        mime = "image/png"

    elif ext == ".webp":
        mime = "image/webp"

    return f"data:{mime};base64,{encoded}"


def craft_image(key):

    return image_to_base64(
        CRAFTS[key]["image"]
    )
def artisan_image(artisan):

    return image_to_base64(
        artisan["image"]
    )
def icon_svg(icon):

    icons = {

        "saree": """
        <svg width="24" height="24" viewBox="0 0 24 24"
        fill="none" stroke="#211d19" stroke-width="1.7">
        <path d="M8 3h8l2 5-3 3v10H9V11L6 8l2-5Z"/>
        <path d="M9 11h6"/>
        </svg>
        """,

        "kurta": """
        <svg width="24" height="24" viewBox="0 0 24 24"
        fill="none" stroke="#211d19" stroke-width="1.7">
        <path d="M8 4 4 7l2 4 2-1v10h8V10l2 1 2-4-4-3"/>
        <path d="M10 4c0 2 4 2 4 0"/>
        </svg>
        """,

        "embroidery": """
        <svg width="24" height="24" viewBox="0 0 24 24"
        fill="none" stroke="#211d19" stroke-width="1.7">
        <circle cx="8" cy="8" r="3"/>
        <circle cx="8" cy="16" r="3"/>
        <path d="m10 10 10 10M10 14 20 4"/>
        </svg>
        """,

        "fabric": """
        <svg width="24" height="24" viewBox="0 0 24 24"
        fill="none" stroke="#211d19" stroke-width="1.7">
        <path d="m12 3 8 5-8 5-8-5 8-5Z"/>
        <path d="m4 12 8 5 8-5"/>
        <path d="m4 16 8 5 8-5"/>
        </svg>
        """,

        "craft": """
        <svg width="24" height="24" viewBox="0 0 24 24"
        fill="none" stroke="#211d19" stroke-width="1.7">
        <circle cx="12" cy="12" r="8"/>
        <path d="M12 7v10M7 12h10"/>
        <circle cx="12" cy="12" r="2"/>
        </svg>
        """
    }

    return icons.get(icon, "")

def go(page, **params):

    st.query_params.clear()

    st.query_params["page"] = page

    for key, value in params.items():
        st.query_params[key] = value

    st.rerun()


# ============================================================
# GLOBAL CSS
# ============================================================

st.html("""
<style>

@import url(
'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap'
);

:root {

    --paper:#f7f2e8;
    --cream:#fffaf2;

    --ink:#211d19;
    --muted:#756a60;

    --wine:#711f1f;
    --wine-dark:#4f1515;

    --gold:#b58a52;

    --line:#ded2c2;

    --soft:#eee3d3;

}


html,
body,
[class*="css"] {

    font-family:
    'DM Sans',
    sans-serif;

}


.stApp {

    background:
    var(--paper);

    color:
    var(--ink);

}


[data-testid="stSidebar"],
[data-testid="stHeader"],
[data-testid="stToolbar"],
.stDeployButton {

    display:
    none !important;

}


#MainMenu,
footer {

    visibility:
    hidden !important;

}


.block-container {

    max-width:
    100% !important;

    padding:
    0 !important;

}


a {

    text-decoration:
    none !important;

}


/* ============================================================
NAVBAR
============================================================ */


.navbar {

    height:
    74px;

    background:
    var(--cream);

    display:
    flex;

    align-items:
    center;

    justify-content:
    space-between;

    padding:
    0 4.5%;

    border-bottom:
    1px solid var(--line);

}


.logo {

    font-family:
    'Playfair Display',
    serif;

    font-size:
    25px;

    font-weight:
    700;

    color:
    var(--ink);

}


.navlinks {

    display:
    flex;

    align-items:
    center;

    gap:
    26px;

}


.navlinks a {

    color:
    var(--ink) !important;

    font-size:
    13px;

    font-weight:
    600;

}


.navlinks a:hover {

    color:
    var(--wine) !important;

}


/* ============================================================
BUTTONS
============================================================ */


.primary-link,
.secondary-link {

    display:
    inline-block;

    padding:
    13px 22px;

    border-radius:
    7px;

    font-size:
    14px;

    font-weight:
    700;

}


.primary-link {

    background:
    var(--cream);

    color:
    var(--ink) !important;

}


.secondary-link {

    color:
    white !important;

    border:
    1px solid rgba(
        255,
        255,
        255,
        .8
    );

}


.wine-link {

    display:
    inline-block;

    background:
    var(--wine);

    color:
    white !important;

    padding:
    11px 19px;

    border-radius:
    6px;

    font-size:
    13px;

    font-weight:
    700;

}


/* ============================================================
HOME
============================================================ */


.home-hero {

    min-height:
    510px;

    display:
    flex;

    align-items:
    center;

    padding:
    55px 6%;

    background:

        linear-gradient(

            90deg,

            rgba(
                35,
                14,
                10,
                .94
            ),

            rgba(
                48,
                19,
                14,
                .65
            ),

            rgba(
                40,
                10,
                8,
                .10
            )

        ),

        url(
        "https://images.unsplash.com/photo-1610030469983-98e550d6193c?auto=format&fit=crop&w=1800&q=90"
        );

    background-size:
    cover;

    background-position:
    center;

}


.home-copy {

    max-width:
    570px;

}


.eyebrow {

    color:
    #ddb16c;

    letter-spacing:
    2.5px;

    font-size:
    12px;

    font-weight:
    700;

}


.home-copy h1 {

    font-family:
    'Playfair Display',
    serif;

    color:
    #fffaf2;

    font-size:
    58px;

    line-height:
    1.03;

    margin:
    14px 0 18px;

}


.home-copy p {

    color:
    #f0e5d7;

    font-size:
    16px;

    line-height:
    1.65;

}


.home-actions {

    display:
    flex;

    gap:
    12px;

    margin-top:
    25px;

}


/* ============================================================
FEATURE STRIP
============================================================ */


.feature-strip {

    background:
    var(--cream);

    display:
    grid;

    grid-template-columns:
    repeat(
        4,
        1fr
    );

    padding:
    25px 5%;

    border-bottom:
    1px solid var(--line);

}


.feature-item {

    text-align:
    center;

    padding:
    8px 24px;

    border-right:
    1px solid var(--line);

}


.feature-item:last-child {

    border-right:
    none;

}


.feature-icon {

 display: none;    
}


.feature-item h3 {

    font-family:
    'Playfair Display',
    serif;

    font-size:
    16px;

    margin:
    8px 0 4px;

}


.feature-item p {

    font-size:
    11px;

    color:
    var(--muted);

    line-height:
    1.5;

}


/* ============================================================
GENERAL SECTIONS
============================================================ */


.section {

    padding:
    48px 5%;

}


.section-head {

    display:
    flex;

    align-items:
    flex-end;

    justify-content:
    space-between;

    margin-bottom:
    22px;

}


.section-head h2 {

    font-family:
    'Playfair Display',
    serif;

    font-size:
    31px;

    margin:
    0;

}


.section-head a {

    color:
    var(--wine) !important;

    font-size:
    12px;

    font-weight:
    700;

}


/* ============================================================
CARDS
============================================================ */


.card-grid {

    display:
    grid;

    grid-template-columns:
    repeat(
        4,
        1fr
    );

    gap:
    16px;

}


.visual-card {

    background:
    var(--cream);

    border:
    1px solid var(--line);

    border-radius:
    10px;

    overflow:
    hidden;

}


.visual-card img {

    width:
    100%;

    height:
    180px;

    object-fit:
    cover;

}


.visual-card-body {

    padding:
    13px;

}


.visual-card h3 {

    font-family:
    'Playfair Display',
    serif;

    font-size:
    17px;

    margin:
    0 0 4px;

}


.visual-card p {

    margin:
    0;

    color:
    var(--muted);

    font-size:
    11px;

}


/* ============================================================
ARTISAN BANNER
============================================================ */


.artisan-banner {

    margin:
    10px 5% 55px;

    padding:
    45px;

    min-height:
    190px;

    border-radius:
    12px;

    background:

        linear-gradient(

            90deg,

            rgba(
                42,
                17,
                12,
                .96
            ),

            rgba(
                42,
                17,
                12,
                .60
            )

        ),

        url(
        "https://images.unsplash.com/photo-1606293926075-69a00dbfde81?auto=format&fit=crop&w=1600&q=90"
        );

    background-size:
    cover;

    background-position:
    center;

}


.artisan-banner h2 {

    color:
    white;

    font-family:
    'Playfair Display',
    serif;

    font-size:
    30px;

}


.artisan-banner p {

    color:
    #eadfd1;

    max-width:
    550px;

    font-size:
    13px;

}


/* ============================================================
PAGE
============================================================ */


.page {

    padding:
    42px 5% 65px;

}


.center-head {

    text-align:
    center;

    max-width:
    700px;

    margin:
    0 auto 30px;

}


.center-head h1 {

    font-family:
    'Playfair Display',
    serif;

    font-size:
    38px;

    margin:
    0 0 8px;

}


.center-head p {

    color:
    var(--muted);

    font-size:
    13px;

    line-height:
    1.6;

}


/* ============================================================
DISCOVER
============================================================ */


[data-testid="stFileUploader"] {

    max-width:
    760px;

    margin:
    0 auto;

    background:
    var(--cream);

    border:
    1px solid var(--line);

    border-radius:
    10px;

    padding:
    18px;

}


[data-testid="stFileUploaderDropzone"] {

    min-height:
    190px;

    background:
    #fffdf8;

    border:
    1.5px dashed #a99b8b;

    border-radius:
    8px;

}


[data-testid="stFileUploaderDropzoneInstructions"] span {

    font-size:
    13px;

}


.stButton > button {

    background:
    var(--wine) !important;

    color:
    white !important;

    border:
    none !important;

    border-radius:
    6px !important;

    font-weight:
    700 !important;

}


.example-row {

    display:
    grid;

    grid-template-columns:
    repeat(
        5,
        1fr
    );

    gap:
    12px;

    max-width:
    620px;

    margin:
    15px auto 35px;

}


.example-row img {

    width:
    100%;

    height:
    72px;

    object-fit:
    cover;

    border-radius:
    6px;

    border:
    1px solid var(--line);

}


.identify-types {

    display:
    grid;

    grid-template-columns:
    repeat(
        5,
        1fr
    );

    gap:
    20px;

    max-width:
    700px;

    margin:
    15px auto 38px;

}


.identify-type {

    text-align:
    center;

}


.round-icon {

 display: none;

}


.identify-type p {

    font-size:
    11px;

    font-weight:
    600;

}


.ai-banner {

    max-width:
    760px;

    margin:
    auto;

    background:
    #efe5d6;

    border-radius:
    10px;

    padding:
    24px 28px;

}


.ai-banner h3 {

    font-family:
    'Playfair Display',
    serif;

    margin:
    0 0 5px;

}


.ai-banner p {

    color:
    var(--muted);

    font-size:
    12px;

    margin:
    0;

}


/* ============================================================
RESULT
============================================================ */


.result-title {

    text-align:
    center;

    font-family:
    'Playfair Display',
    serif;

    font-size:
    34px;

    margin-bottom:
    24px;

}


.result-top {

    display:
    grid;

    grid-template-columns:
    1.05fr .95fr;

    gap:
    20px;

    max-width:
    900px;

    margin:
    auto;

}


.result-photo {

    background:
    var(--cream);

    border-radius:
    10px;

    border:
    1px solid var(--line);

    overflow:
    hidden;

}


.result-photo img {

    width:
    100%;

    height:
    340px;

    object-fit:
    cover;

}


.result-info {

    background:
    #f2e4df;

    border-radius:
    10px;

    padding:
    30px;

}


.result-small {

    font-size:
    11px;

    font-weight:
    700;

    color:
    #7e4d46;

}


.result-info h1 {

    font-family:
    'Playfair Display',
    serif;

    font-size:
    34px;

    margin:
    7px 0;

}


.result-info p {

    color:
    #5f554d;

    font-size:
    13px;

    line-height:
    1.6;

}


.confidence {

    display:
    inline-block;

    background:
    #1d7a63;

    color:
    white;

    border-radius:
    20px;

    padding:
    7px 12px;

    font-size:
    12px;

    font-weight:
    700;

    margin:
    8px 0 13px;

}


/* UNCERTAIN */

.uncertain-info {

    background:
    #f3e7dc;

    border:
    1px solid #dcc9b7;

    border-radius:
    10px;

    padding:
    30px;

}


.uncertain-info h1 {

    font-family:
    'Playfair Display',
    serif;

    font-size:
    32px;

    margin:
    8px 0;

}


.uncertain-info p {

    color:
    #5f554d;

    font-size:
    13px;

    line-height:
    1.7;

}


.uncertain-badge {

    display:
    inline-block;

    background:
    #9a642f;

    color:
    white;

    border-radius:
    20px;

    padding:
    7px 12px;

    font-size:
    12px;

    font-weight:
    700;

    margin:
    8px 0 15px;

}


.tabs {

    display:
    flex;

    justify-content:
    center;

    max-width:
    900px;

    margin:
    22px auto 0;

    border-bottom:
    1px solid var(--line);

}


.tab {

    padding:
    12px 20px;

    font-size:
    11px;

    font-weight:
    600;

}


.tab.active {

    color:
    var(--wine);

    border-bottom:
    2px solid var(--wine);

}


.detail-box {

    max-width:
    900px;

    margin:
    auto;

    background:
    var(--cream);

    border:
    1px solid var(--line);

    border-top:
    none;

    padding:
    28px;

}


.detail-box h3 {

    font-family:
    'Playfair Display',
    serif;

    font-size:
    20px;

}


.detail-box p {

    color:
    #62584f;

    font-size:
    13px;

    line-height:
    1.75;

}


.top-predictions {

    max-width:
    900px;

    margin:
    25px auto;

}


.pred-row {

    display:
    flex;

    justify-content:
    space-between;

    padding:
    11px 0;

    border-bottom:
    1px solid var(--line);

    font-size:
    12px;

}


.retry-note {

    max-width:
    900px;

    margin:
    25px auto;

    background:
    var(--cream);

    border:
    1px solid var(--line);

    border-radius:
    9px;

    padding:
    22px;

    color:
    #62584f;

    font-size:
    12px;

    line-height:
    1.7;

}
/* ============================================================
LIBRARY
============================================================ */


.search-look {

    border:
    1px solid var(--line);

    background:
    var(--cream);

    border-radius:
    7px;

    padding:
    12px 16px;

    color:
    #8a8076;

    font-size:
    12px;

    margin-bottom:
    15px;

}


.filter-row {

    display:
    flex;

    gap:
    8px;

    margin-bottom:
    22px;

    flex-wrap:
    wrap;

}


.filter-pill {

    background:
    var(--cream);

    border:
    1px solid var(--line);

    border-radius:
    20px;

    padding:
    7px 14px;

    font-size:
    10px;

}


.filter-pill.active {

    background: #7b2024 !important;

    color: #ffffff !important;

    border: 1px solid #7b2024 !important;

    font-weight: 600;

}
.filter-pill.active,
.filter-pill.active:visited,
.filter-pill.active:hover {

    color: #ffffff !important;

}


.library-grid {

    display:
    grid;

    grid-template-columns:
    repeat(
        3,
        1fr
    );

    gap:
    20px;

}


.library-card {

    background:
    var(--cream);

    border:
    1px solid var(--line);

    border-radius:
    9px;

    padding:
    10px;

    transition:
    transform .2s ease;

}


.library-card:hover {

    transform:
    translateY(-3px);

}


.library-card img {

    width:
    100%;

    height:
    210px;

    object-fit:
    cover;

    border-radius:
    8px;

}


.library-card h3 {

    font-family:
    'Playfair Display',
    serif;

    margin:
    9px 0 2px;

    font-size:
    18px;

    color:
    var(--ink);

}


.library-card p {

    color:
    var(--muted);

    margin:
    0;

    font-size:
    11px;

}


/* ============================================================
CRAFT DETAILS
============================================================ */


.detail-hero {

    height:
    330px;

    display:
    flex;

    align-items:
    flex-end;

    padding:
    35px 5%;

    background-size:
    cover;

    background-position:
    center;

}


.detail-hero h1 {

    color:
    white;

    font-family:
    'Playfair Display',
    serif;

    font-size:
    42px;

    margin:
    0;

}


.detail-hero p {

    color:
    #f0e5d8;

    font-size:
    13px;

}


.detail-layout {

    display:
    grid;

    grid-template-columns:
    2fr 1fr;

    gap:
    25px;

    padding:
    30px 5%;

}


.info-panel,
.fact-panel {

    background:
    var(--cream);

    border:
    1px solid var(--line);

    border-radius:
    9px;

    padding:
    24px;

}


.info-panel h2,
.fact-panel h3 {

    font-family:
    'Playfair Display',
    serif;

}


.info-panel p,
.fact-panel p {

    color:
    var(--muted);

    line-height:
    1.7;

    font-size:
    13px;

}


/* ============================================================
ARTISAN DIRECTORY
============================================================ */


.directory-tools {

    max-width:
    900px;

    margin:
    0 auto 20px;

}


.artisan-list {

    max-width:
    900px;

    margin:
    auto;

}


.artisan-card {

    display:
    grid;

    grid-template-columns:
    90px 1fr auto;

    gap:
    16px;

    align-items:
    center;

    background:
    var(--cream);

    border:
    1px solid var(--line);

    border-radius:
    9px;

    padding:
    12px;

    margin-bottom:
    10px;

}


.artisan-avatar {

    height:
    80px;

    border-radius:
    7px;

    background:
    #ded0bf;

    display:
    flex;

    align-items:
    center;

    justify-content:
    center;

    font-size:
    28px;

}


.artisan-card h3 {

    font-family:
    'Playfair Display',
    serif;

    margin:
    0 0 4px;

}


.artisan-card p {

    margin:
    2px 0;

    color:
    var(--muted);

    font-size:
    11px;

}


.demo-badge {

    display:
    inline-block;

    background:
    #eee3d3;

    color:
    #775c3d;

    border-radius:
    12px;

    padding:
    3px 8px;

    font-size:
    9px;

    font-weight:
    700;

}


/* ============================================================
ARTISAN PROFILE
============================================================ */


.profile-hero {

    height:
    300px;

    background:

        linear-gradient(

            90deg,

            rgba(
                30,
                15,
                10,
                .25
            ),

            rgba(
                30,
                15,
                10,
                .05
            )

        ),

        url(
        "https://images.unsplash.com/photo-1606293926075-69a00dbfde81?auto=format&fit=crop&w=1600&q=90"
        );

    background-size:
    cover;

    background-position:
    center;

}


.profile-body {

    padding:
    30px 5%;

}


.profile-body h1 {

    font-family:
    'Playfair Display',
    serif;

    font-size:
    35px;

    margin-bottom:
    5px;

}


.profile-body p {

    color:
    var(--muted);

    font-size:
    13px;

    line-height:
    1.7;

}


/* ============================================================
ABOUT
============================================================ */


.about-grid {

    display:
    grid;

    grid-template-columns:
    1fr 1.2fr;

    gap:
    25px;

    max-width:
    950px;

    margin:
    auto;

}


.about-photo {

    min-height:
    300px;

    border-radius:
    10px;

    background:

        linear-gradient(
            rgba(
                50,
                20,
                10,
                .10
            ),
            rgba(
                50,
                20,
                10,
                .10
            )
        ),

        url(
        "https://images.unsplash.com/photo-1561361513-2d000a50f0dc?auto=format&fit=crop&w=1000&q=90"
        );

    background-size:
    cover;

    background-position:
    center;

}


.about-copy {

    background:
    var(--cream);

    border-radius:
    10px;

    padding:
    28px;

}


.about-copy h2 {

    font-family:
    'Playfair Display',
    serif;

}


.about-copy p {

    color:
    var(--muted);

    font-size:
    13px;

    line-height:
    1.75;

}


.values {

    display:
    grid;

    grid-template-columns:
    repeat(
        4,
        1fr
    );

    max-width:
    950px;

    margin:
    30px auto;

    gap:
    15px;

}


.value {

    text-align:
    center;

}


.value h4 {

    font-family:
    'Playfair Display',
    serif;

    margin:
    7px 0 3px;

}


.value p {

    color:
    var(--muted);

    font-size:
    10px;

}


/* ============================================================
FOOTER
============================================================ */


.footer {

    background:
    #211f1c;

    color:
    #dcd0c1;

    padding:
    22px 5%;

    display:
    flex;

    justify-content:
    space-between;

    font-size:
    11px;

}


/* ============================================================
RESPONSIVE
============================================================ */


@media(max-width:800px) {

    .navlinks {

        gap:
        10px;

    }


    .navlinks a {

        font-size:
        10px;

    }


    .card-grid,
    .library-grid,
    .feature-strip,
    .identify-types,
    .values {

        grid-template-columns:
        1fr 1fr;

    }


    .result-top,
    .detail-layout,
    .about-grid {

        grid-template-columns:
        1fr;

    }


    .artisan-card {

        grid-template-columns:
        70px 1fr;

    }


    .home-copy h1 {

        font-size:
        44px;

    }

}

/* ============================================================
PREMIUM FILE UPLOADER
============================================================ */

[data-testid="stFileUploader"] {
    background: #fffaf2 !important;
    border: 1px solid #dfd3c3 !important;
    border-radius: 14px !important;
    padding: 20px !important;
}

[data-testid="stFileUploaderDropzone"] {
    min-height: 220px !important;
    background: #fffdf8 !important;
    border: 1.5px dashed #b7a48e !important;
    border-radius: 12px !important;
}

/* Browse / Upload button */

[data-testid="stFileUploaderDropzone"] button {
    background: #7b2024 !important;
    color: #ffffff !important;

    border: none !important;
    border-radius: 7px !important;

    padding: 10px 24px !important;

    font-family: 'DM Sans', sans-serif !important;
    font-size: 13px !important;
    font-weight: 600 !important;

    box-shadow: none !important;

    transition: all 0.2s ease !important;
}

[data-testid="stFileUploaderDropzone"] button:hover {
    background: #5f171a !important;
    color: #ffffff !important;
    transform: translateY(-1px);
}

/* Upload icon */

[data-testid="stFileUploaderDropzone"] svg {
    color: #7b2024 !important;
    fill: #7b2024 !important;
}

/* Main uploader text */

[data-testid="stFileUploaderDropzoneInstructions"] span {
    color: #2b241f !important;
    font-size: 14px !important;
    font-weight: 600 !important;
}

/* JPG PNG size text */

[data-testid="stFileUploaderDropzoneInstructions"] small {
    color: #8b7d70 !important;
    font-size: 11px !important;
}

</style>
""")


# ============================================================
# NAVBAR
# ============================================================


def navbar():

    st.html(f"""
    <nav class="navbar">

        <div class="logo">
            ✤ Karigari
        </div>

        <div class="navlinks">

            <a
                href="?page=home"
                target="_self"
            >
                Home
            </a>

            <a
                href="?page=discover"
                target="_self"
            >
                Discover
            </a>

            <a
                href="?page=crafts"
                target="_self"
            >
                Crafts
            </a>

            <a
                href="?page=artisans"
                target="_self"
            >
                Artisans
            </a>

            <a
                href="?page=about"
                target="_self"
            >
                About
            </a>

        </div>

    </nav>
    """)


# ============================================================
# HOME PAGE
# ============================================================


def home_page():

    navbar()

    featured = [
        "Banarasi",
        "Bandhani",
        "Kanjeevaram",
        "Patola"
    ]

    cards = ""

    for key in featured:

        craft = CRAFTS[key]

        img = craft_image(key)

        cards += f"""
        <a
            href="?page=details&craft={key}"
            target="_self"
            style="color:inherit;"
        >

            <div class="visual-card">

                <img
                    src="{img}"
                    alt="{craft["name"]}"
                >

                <div class="visual-card-body">

                    <h3>
                        {craft["name"]}
                    </h3>

                    <p>
                        {craft["region"]}
                    </p>

                </div>

            </div>

        </a>
        """

    st.html(
        f"""
        <section class="home-hero">

            <div class="home-copy">

                <div class="eyebrow">
                    INDIA'S LIVING CRAFT HERITAGE
                </div>

                <h1>
                    Tradition<br>
                    In Every Thread
                </h1>

                <p>
                    Discover the stories, techniques and
                    artisans behind India's timeless crafts.
                </p>

                <div class="home-actions">

                    <a
                        class="primary-link"
                        href="?page=discover"
                        target="_self"
                    >
                        Identify a Craft
                    </a>

                    <a
                        class="secondary-link"
                        href="?page=crafts"
                        target="_self"
                    >
                        Explore Crafts
                    </a>

                </div>

            </div>

        </section>


        <section class="feature-strip">

            <div class="feature-item">

                <div class="feature-icon">{icon_svg("fabric")}</div>

                <h3>
                    AI Craft Recognition
                </h3>

                <p>
                    Upload a photo and identify
                    the likely craft.
                </p>

            </div>


            <div class="feature-item">

                <div class="feature-icon">{icon_svg("craft")}</div>

                <h3>
                    Cultural Insights
                </h3>

                <p>
                    Learn the history and significance
                    behind every recognised craft.
                </p>

            </div>


            <div class="feature-item">

                <div class="feature-icon">{icon_svg("kurta")}</div>

                <h3>
                    Meet Artisans
                </h3>

                <p>
                    Connect recognition with
                    the people behind the craft.
                </p>

            </div>


            <div class="feature-item">

                <div class="feature-icon">{icon_svg("saree")}</div>

                <h3>
                    Support & Preserve
                </h3>

                <p>
                    Help traditional knowledge
                    gain digital visibility.
                </p>

            </div>

        </section>


        <section class="section">

            <div class="section-head">

                <h2>
                    Featured Crafts
                </h2>

                <a
                    href="?page=crafts"
                    target="_self"
                >
                    View All →
                </a>

            </div>

            <div class="card-grid">
                {cards}
            </div>

        </section>


        <section class="artisan-banner">

            <h2>
                Artisans Keep Our Heritage Alive.
            </h2>

            <p>
                Meet the people whose knowledge,
                skill and patience keep India's
                textile traditions alive.
            </p>

            <br>

            <a
                class="primary-link"
                href="?page=artisans"
                target="_self"
            >
                Meet Our Artisans
            </a>

        </section>
        """
    )

    footer()


# ============================================================
# DISCOVER PAGE
# ============================================================


def discover_page():

    navbar()

    st.html("""
    <main class="page">

        <div class="center-head">

            <h1>
                Discover Your Craft
            </h1>

            <p>
                Upload a photo of a clothing item,
                embroidery or textile to identify
                the craft and learn its story.
            </p>

        </div>

    </main>
    """)

    st.html("""
    <style>

    div[data-testid="stFileUploader"] {

        margin-top:
        -45px;

    }

    </style>
    """)

    uploaded_file = st.file_uploader(

        "Upload craft image",

        type=[
            "jpg",
            "jpeg",
            "png",
            "webp"
        ],

        label_visibility=
        "collapsed"

    )

    if uploaded_file is not None:

        image_bytes = (
            uploaded_file
            .getvalue()
        )

        try:

            image = Image.open(
                io.BytesIO(
                    image_bytes
                )
            ).convert(
                "RGB"
            )

            preview_left, preview_mid, preview_right = (
                st.columns(
                    [
                        1.2,
                        2,
                        1.2
                    ]
                )
            )

            with preview_mid:

                st.image(
                    image,
                    use_container_width=True
                )

                identify = st.button(
                    "Identify the Craft",
                    use_container_width=True
                )

            if identify:

                predict_image(
                    uploaded_file,
                    image_bytes
                )

        except Exception:

            st.error(
                "Please upload a valid "
                "JPG, PNG or WEBP image."
            )

    else:

        examples = ""

        for key in CRAFTS:

            examples += (
                f'<img '
                f'src="{craft_image(key)}" '
                f'alt="{CRAFTS[key]["name"]}">'
            )

        st.html(
            f"""
            <div
                style="
                    text-align:center;
                    font-family:
                    'Playfair Display',
                    serif;
                    margin-top:25px;
                    font-size:15px;
                    font-weight:600;
                "
            >
                Or try these examples
            </div>


            <div class="example-row">
                {examples}
            </div>
            """
        )

    st.html(f"""
    <div
        style="
            text-align:center;
            font-family:
            'Playfair Display',
            serif;
            font-size:17px;
            font-weight:600;
            margin-top:28px;
        "
    >
        What can you identify?
    </div>


    <div class="identify-types">

        <div class="identify-type">

            <div class="round-icon">{icon_svg("saree")}</div>

            <p>
                Sarees
            </p>

        </div>


        <div class="identify-type">

            <div class="round-icon">{icon_svg("kurta")}</div>

            <p>
                Kurtas
            </p>

        </div>


        <div class="identify-type">

            <div class="round-icon">{icon_svg("embroidery")}</div>

            <p>
                Embroidery
            </p>

        </div>


        <div class="identify-type">

            <div class="round-icon">{icon_svg("fabric")}</div>

            <p>
                Fabrics
            </p>

        </div>


        <div class="identify-type">

            <div class="round-icon">{icon_svg("craft")}</div>

            <p>
                Handicrafts
            </p>

        </div>

    </div>


    <div class="ai-banner">

        <h3>
            Powered by AI.
            Rooted in Tradition.
        </h3>

        <p>
            Our deep-learning model analyses
            visual patterns, textures and
            weaving characteristics to recognise
            selected Indian textile traditions.
        </p>

    </div>
    """)

    footer()


# ============================================================
# API PREDICTION
# ============================================================


def predict_image(
    uploaded_file,
    image_bytes
):

    with st.spinner(
        "Identifying the craft..."
    ):

        try:

            response = requests.post(

                API_URL,

                files={

                    "image": (

                        uploaded_file.name,

                        image_bytes,

                        uploaded_file.type
                        or "image/jpeg"

                    )

                },

                headers={

                    "ngrok-skip-browser-warning":
                    "true",

                    "User-Agent":
                    "Karigari-App"

                },

                timeout=60

            )

            response.raise_for_status()

            result = (
                response.json()
            )

            if not result.get(
                "success"
            ):

                st.error(

                    result.get(

                        "error",

                        "Unable to analyse image."

                    )

                )

                return

            st.session_state[
                "prediction_result"
            ] = result

            st.session_state[
                "prediction_image"
            ] = image_bytes

            go(
                "result"
            )

        except requests.exceptions.ConnectionError:

            st.error(
                "Recognition service is offline. "
                "Keep the Colab backend connected."
            )

        except requests.exceptions.Timeout:

            st.error(
                "Recognition service timed out. "
                "Please try again."
            )

        except Exception as error:

            st.error(
                f"Prediction failed: {error}"
            )


# ============================================================
# RESULT PAGE
# ============================================================


def result_page():

    navbar()

    if (
        "prediction_result"
        not in st.session_state
    ):

        st.warning(
            "Upload an image first "
            "to identify a craft."
        )

        if st.button(
            "Go to Discover"
        ):

            go(
                "discover"
            )

        return

    result = st.session_state[
        "prediction_result"
    ]

    image_bytes = st.session_state[
        "prediction_image"
    ]

    prediction = result[
        "prediction"
    ]

    confidence = float(
        result[
            "confidence"
        ]
    )

    top_predictions = result.get(
        "top_predictions",
        []
    )

    image_b64 = base64.b64encode(
        image_bytes
    ).decode()

    is_confident = (
        confidence
        >=
        CONFIDENCE_THRESHOLD
    )


    # ========================================================
    # CONFIDENT RESULT
    # ========================================================

    if is_confident:

        craft = CRAFTS[
            prediction
        ]
        artisan_ids = CRAFT_ARTISANS.get(
            prediction,
            []
        )

        result_artisan_id = (
            artisan_ids[0]
            if artisan_ids
            else None
        )

        result_artisan = (
            ARTISANS[result_artisan_id]
            if result_artisan_id
            else None
        )

        result_artisan_img = (
            artisan_image(result_artisan)
            if result_artisan
            else ""
        )
        result_panel = f"""
        <div class="result-info">

            <div class="result-small">
                PREDICTED CRAFT
            </div>

            <h1>
                {craft["name"]}
            </h1>

            <p>
                ◉ {craft["region"]}
            </p>

            <div class="confidence">
                {confidence:.2f}%
                Confidence
            </div>

            <p>
                {craft["overview"]}
            </p>

            <br>

            <a
                class="wine-link"
                href="?page=details&craft={prediction}"
                target="_self"
            >
                Learn More
            </a>

            &nbsp;

            <a
                class="wine-link"
                href="?page=artisans&craft={prediction}"
                target="_self"
            >
                Find Artisans
            </a>

        </div>
        """


    # ========================================================
    # UNCERTAIN RESULT
    # ========================================================

    else:

        craft = None

        possible_matches = ", ".join(

            item["craft"]

            for item
            in top_predictions[:3]

        )

        result_panel = f"""
        <div class="uncertain-info">

            <div class="result-small">
                AI RECOGNITION RESULT
            </div>

            <h1>
                Identification Uncertain
            </h1>

            <div class="uncertain-badge">

                Highest Match:
                {confidence:.2f}%

            </div>

            <p>
                Karigari could not confidently
                identify this textile as one
                specific craft.
            </p>

            <p>
                The image shows visual
                similarities with
                <strong>
                    {possible_matches}
                </strong>.
            </p>

            <p>
                For a more reliable result,
                upload a closer, well-lit
                photograph of the fabric,
                border, weave or motif instead
                of the complete outfit.
            </p>

            <br>

            <a
                class="wine-link"
                href="?page=discover"
                target="_self"
            >
                Try Another Photo
            </a>

        </div>
        """


    # ========================================================
    # RESULT TOP
    # ========================================================

    st.html(
        f"""
        <main class="page">

            <div class="result-title">
                Identification Result
            </div>

            <div class="result-top">

                <div class="result-photo">

                    <img
                        src="
                        data:image/jpeg;base64,
                        {image_b64}
                        "
                    >

                </div>

                {result_panel}

            </div>

        </main>
        """
    )


    # ========================================================
    # CONFIDENCE BREAKDOWN
    # ========================================================

    st.html("""
    <div class="top-predictions">

        <h3
            style="
                font-family:
                'Playfair Display',
                serif;
                font-size:22px;
            "
        >
            AI Confidence Breakdown
        </h3>

        <p
            style="
                color:#756a60;
                font-size:12px;
                line-height:1.6;
            "
        >
            The model's three strongest
            matches for the uploaded image.
        </p>

    </div>
    """)

    for item in top_predictions:

        st.html(
            f"""
            <div class="top-predictions">

                <div class="pred-row">

                    <span>
                        {item["craft"]}
                    </span>

                    <strong>
                        {item["confidence"]:.2f}%
                    </strong>

                </div>

            </div>
            """
        )


    # ========================================================
    # UNCERTAIN EXPLANATION
    # ========================================================

    if not is_confident:

        st.html(
            f"""
            <div class="retry-note">

                <strong>
                    Why wasn't a craft confirmed?
                </strong>

                <br><br>

                Karigari only confirms a craft
                when the highest model confidence
                is at least

                <strong>
                    {CONFIDENCE_THRESHOLD:.0f}%
                </strong>.

                The strongest match for this
                photograph was only

                <strong>
                    {confidence:.2f}%
                </strong>.

                Showing
                <strong>
                    {prediction}
                </strong>
                as a definite identification
                would therefore be misleading.

            </div>
            """
        )

        st.html("""
        <section class="section">

            <div class="section-head">

                <h2>
                    Explore Possible Matches
                </h2>

                <a
                    href="?page=crafts"
                    target="_self"
                >
                    View Craft Library →
                </a>

            </div>

        </section>
        """)

        footer()

        return


    # ========================================================
    # CONFIDENT CRAFT DETAILS
    # ========================================================

    st.html(
        f"""
        <div class="tabs">

            <div class="tab active">
                About the Craft
            </div>

            <div class="tab">
                Technique
            </div>

            <div class="tab">
                Cultural Significance
            </div>

            <div class="tab">
                Geographical Roots
            </div>

        </div>


        <div class="detail-box">

            <h3>
                About {craft["name"]}
            </h3>

            <p>
                {craft["overview"]}
            </p>

            <p>

                <strong>
                    Technique:
                </strong>

                {craft["technique"]}

            </p>

            <p>

                <strong>
                    Cultural significance:
                </strong>

                {craft["significance"]}

            </p>

        </div>
        """
    )


    # ========================================================
    # ARTISAN SECTION
    # ========================================================

    if result_artisan:

        st.html(
            f"""
            <section class="section">

                <div class="section-head">

                    <h2>
                        Meet an Artisan Behind This Craft
                    </h2>

                    <a
                        href="?page=artisans&craft={prediction}"
                        target="_self"
                    >
                        View All →
                    </a>

                </div>


                <div class="artisan-card">

                    <div class="artisan-avatar">

                        <img
                            src="{result_artisan_img}"
                            alt="{result_artisan["name"]}"
                            style="
                                width:100%;
                                height:100%;
                                object-fit:cover;
                                object-position:center top;
                                border-radius:7px;
                            "
                        >

                    </div>


                    <div>

                        <span class="demo-badge">
                            VERIFIED SOURCE
                        </span>

                        <h3>
                            {result_artisan["name"]}
                        </h3>

                        <p>
                            {result_artisan["location"]}
                        </p>

                        <p>
                            <strong>
                                {result_artisan["craft_name"]}
                            </strong>
                            · {result_artisan["title"]}
                        </p>

                        <p>
                            {result_artisan["specialisation"]}
                        </p>

                        <p style="
                            color:#9a7445;
                            font-size:10px;
                            font-weight:700;
                        ">
                            {result_artisan["award"]}
                        </p>

                    </div>


                    <a
                        class="wine-link"
                        href="?page=artisan-profile&artisan={result_artisan_id}"
                        target="_self"
                    >
                        View Profile
                    </a>

                </div>

            </section>
            """
        )

    footer()
   # ============================================================
# ALL CRAFTS PAGE
# ============================================================


def crafts_page():

    navbar()

    cards = ""

    for key, craft in CRAFTS.items():

        cards += f"""
        <a
            href="?page=details&craft={key}"
            target="_self"
            style="
                color:inherit;
                text-decoration:none;
            "
        >

            <div class="library-card">

                <img
                    src="{craft_image(key)}"
                    alt="{craft["name"]}"
                >

                <h3>
                    {craft["name"]}
                </h3>

                <p>
                    {craft["region"]}
                </p>

                <p
                    style="
                        margin-top:7px;
                        font-size:10px;
                        color:#9a7445;
                        font-weight:700;
                    "
                >
                    {craft["type"]}
                </p>

            </div>

        </a>
        """

    st.html(
        f"""
        <main class="page">

            <div class="center-head">

                <h1>
                    Explore Traditional Indian Crafts
                </h1>

                <p>
                    Discover the rich diversity of India's
                    textile traditions and the cultural
                    knowledge behind them.
                </p>

            </div>


            <div class="search-look">

                ⌕ &nbsp;

                Search crafts
                (e.g. Banarasi, Bandhani...)

            </div>


            <div class="filter-row">

                <div class="filter-pill active">
                    All
                </div>

                <div class="filter-pill">
                    Weaving
                </div>

                <div class="filter-pill">
                    Tie-Dye
                </div>

                <div class="filter-pill">
                    Silk
                </div>

                <div class="filter-pill">
                    Ikat
                </div>

                <div class="filter-pill">
                    Brocade
                </div>

            </div>


            <div class="library-grid">

                {cards}

            </div>


            <div
                style="
                    max-width:900px;
                    margin:40px auto 0;
                    padding:22px;
                    background:#efe5d6;
                    border-radius:9px;
                    color:#655b52;
                    font-size:12px;
                    line-height:1.7;
                "
            >

                <strong>
                    Growing Craft Library
                </strong>

                <br><br>

                Karigari's current deep-learning prototype
                recognises five textile traditions:
                Banarasi, Bandhani, Kanjeevaram,
                Patola and Tussar.

                The wider platform is designed to expand
                to additional Indian embroidery, weaving,
                dyeing, painting and handicraft traditions.

            </div>

        </main>
        """
    )

    footer()


# ============================================================
# CRAFT DETAILS PAGE
# ============================================================


def craft_details_page():

    navbar()

    key = st.query_params.get(
        "craft",
        "Banarasi"
    )

    if key not in CRAFTS:

        key = "Banarasi"

    craft = CRAFTS[
        key
    ]

    image = craft_image(
        key
    )

    st.html(
        f"""
        <section
            class="detail-hero"

            style="
                background-image:

                linear-gradient(

                    90deg,

                    rgba(
                        40,
                        15,
                        10,
                        .78
                    ),

                    rgba(
                        40,
                        15,
                        10,
                        .12
                    )

                ),

                url('{image}');
            "
        >

            <div>

                <div
                    style="
                        color:#ddb16c;
                        font-size:11px;
                        font-weight:700;
                        letter-spacing:2px;
                        margin-bottom:7px;
                    "
                >
                    TRADITIONAL INDIAN CRAFT
                </div>

                <h1>
                    {craft["name"]}
                </h1>

                <p>
                    ◉ {craft["region"]}
                </p>

            </div>

        </section>


        <div class="tabs">

            <div class="tab active">
                Overview
            </div>

            <div class="tab">
                Technique
            </div>

            <div class="tab">
                History
            </div>

            <div class="tab">
                Cultural Significance
            </div>

            <div class="tab">
                Gallery
            </div>

        </div>


        <section class="detail-layout">


            <div class="info-panel">

                <h2>
                    Overview
                </h2>

                <p>
                    {craft["overview"]}
                </p>


                <h2>
                    Technique
                </h2>

                <p>
                    {craft["technique"]}
                </p>


                <h2>
                    Cultural Significance
                </h2>

                <p>
                    {craft["significance"]}
                </p>


                <h2>
                    Visual Identity
                </h2>

                <p>
                    Common motifs and visual characteristics
                    include {craft["motifs"]}.
                </p>

            </div>


            <div class="fact-panel">

                <div
                    style="
                        color:#9a7445;
                        font-size:10px;
                        letter-spacing:2px;
                        font-weight:700;
                    "
                >
                    CRAFT AT A GLANCE
                </div>

                <h3>
                    Craft Details
                </h3>


                <p>

                    <strong>
                        Type
                    </strong>

                    <br>

                    {craft["type"]}

                </p>


                <p>

                    <strong>
                        Primary Materials
                    </strong>

                    <br>

                    {craft["materials"]}

                </p>


                <p>

                    <strong>
                        Region
                    </strong>

                    <br>

                    {craft["region"]}

                </p>


                <p>

                    <strong>
                        Common Motifs
                    </strong>

                    <br>

                    {craft["motifs"]}

                </p>


                <br>


                <a
                    class="wine-link"
                    href="?page=artisans&craft={key}"
                    target="_self"
                >
                    Find Artisans
                </a>

            </div>

        </section>


        <section
            style="
                padding:10px 5% 55px;
            "
        >

            <div class="section-head">

                <h2>
                    The People Behind the Craft
                </h2>

                <a
                    href="?page=artisans"
                    target="_self"
                >
                    Explore Artisans →
                </a>

            </div>


            <div
                style="
                    background:#fffaf2;
                    border:1px solid #ded2c2;
                    border-radius:9px;
                    padding:25px;
                "
            >

                <span class="demo-badge">
                    ARTISAN EMPOWERMENT
                </span>

                <p
                    style="
                        color:#655b52;
                        font-size:13px;
                        line-height:1.75;
                        margin-bottom:0;
                    "
                >
                    Karigari's long-term goal is not only
                    to recognise a craft, but also to help
                    users discover verified artisans and
                    communities carrying that tradition
                    forward.
                </p>

            </div>

        </section>
        """
    )

    footer()


# ============================================================
# ARTISAN DIRECTORY
# ============================================================


def artisans_page():

    navbar()

    selected_craft = st.query_params.get(
        "craft",
        "All"
    )
    search_query = st.text_input(
        "Search artisans",
        placeholder="Search by artisan, craft or location...",
        label_visibility="collapsed",
        key="artisan_search"
    )

    artisan_cards = ""

    for artisan_id, artisan in ARTISANS.items():
        if search_query:

            q = search_query.lower().strip()

            searchable_text = " ".join([
                artisan["name"],
                artisan["craft"],
                artisan["craft_name"],
                artisan["location"],
                artisan["title"],
                artisan["specialisation"]
            ]).lower()

            if q not in searchable_text:
                continue
        # Load actual artisan photograph
        artisan_img = artisan_image(
            artisan
        )

        # Craft filter
        if (
            selected_craft != "All"
            and artisan["craft"] != selected_craft
        ):
            continue

        artisan_cards += f"""
        <div class="artisan-card">

            <div class="artisan-avatar">

                <img
                    src="{artisan_img}"
                    alt="{artisan["name"]}"
                    style="
                        width:100%;
                        height:100%;
                        object-fit:cover;
                        object-position:center top;
                        border-radius:7px;
                    "
                >

            </div>

            <div>

                <span class="demo-badge">
                    VERIFIED SOURCE
                </span>

                <h3>
                    {artisan["name"]}
                </h3>

                <p>
                    {artisan["location"]}
                </p>

                <p>
                    <strong>
                        {artisan["craft_name"]}
                    </strong>
                    · {artisan["title"]}
                </p>

                <p>
                    {artisan["specialisation"]}
                </p>

                <p
                    style="
                        color:#9a7445;
                        font-size:10px;
                        font-weight:700;
                    "
                >
                    {artisan["award"]}
                </p>

            </div>

            <a
                class="wine-link"
                href="?page=artisan-profile&artisan={artisan_id}"
                target="_self"
            >
                View Profile
            </a>

        </div>
        """

    if not artisan_cards:

        artisan_cards = """
        <div
            style="
                background:#fffaf2;
                border:1px solid #ded2c2;
                padding:25px;
                border-radius:9px;
                text-align:center;
            "
        >
            No documented artisan profile is currently
            available for this craft.
        </div>
        """

    st.html(
        f"""
        <main class="page">

            <div class="center-head">

                <h1>
                    Meet Our Artisans
                </h1>

                <p>
                    Discover documented master artisans and
                    weavers associated with India's traditional
                    textile crafts.
                </p>

            </div>

            <div class="directory-tools">

                

                <div class="filter-row">

                    <a
                        href="?page=artisans&craft=All"
                        target="_self"
                        class="filter-pill {'active' if selected_craft == 'All' else ''}"
                        style="color:inherit;"
                    >
                        All
                    </a>

                    <a
                        href="?page=artisans&craft=Banarasi"
                        target="_self"
                        class="filter-pill {'active' if selected_craft == 'Banarasi' else ''}"
                        style="color:inherit;"
                    >
                        Banarasi
                    </a>

                    <a
                        href="?page=artisans&craft=Bandhani"
                        target="_self"
                        class="filter-pill {'active' if selected_craft == 'Bandhani' else ''}"
                        style="color:inherit;"
                    >
                        Bandhani
                    </a>

                    <a
                        href="?page=artisans&craft=Kanjeevaram"
                        target="_self"
                        class="filter-pill {'active' if selected_craft == 'Kanjeevaram' else ''}"
                        style="color:inherit;"
                    >
                        Kanjeevaram
                    </a>

                    <a
                        href="?page=artisans&craft=Patola"
                        target="_self"
                        class="filter-pill {'active' if selected_craft == 'Patola' else ''}"
                        style="color:inherit;"
                    >
                        Patola
                    </a>

                    <a
                        href="?page=artisans&craft=Tussar"
                        target="_self"
                        class="filter-pill {'active' if selected_craft == 'Tussar' else ''}"
                        style="color:inherit;"
                    >
                        Tussar
                    </a>

                </div>

            </div>

            <div class="artisan-list">

                {artisan_cards}

            </div>

        </main>
        """
    )

    footer()

# ============================================================
# ARTISAN PROFILE
# ============================================================


def artisan_profile_page():

    navbar()

    artisan_id = st.query_params.get(
        "artisan",
        "naseem-ahmad"
    )

    if artisan_id not in ARTISANS:

        artisan_id = "naseem-ahmad"

    artisan = ARTISANS[
        artisan_id
    ]

    craft_key = artisan[
        "craft"
    ]

    craft = CRAFTS[
        craft_key
    ]

    craft_img = craft_image(
        craft_key
    )
    artisan_img = artisan_image(
        artisan
    )

    st.html(
        f"""
        <section
            class="profile-hero"

            style="
                background-image:

                linear-gradient(
                    90deg,
                    rgba(30,15,10,.62),
                    rgba(30,15,10,.10)
                ),

                url('{artisan_img}');

                background-size:cover;
                background-position:center;
            "
        >
        </section>


        <main class="profile-body">

            <span class="demo-badge">
                DOCUMENTED ARTISAN
            </span>


            <h1>
                {artisan["name"]}
            </h1>


            <p>
                {artisan["title"]}
                · {artisan["location"]}
            </p>


            <p
                style="
                    color:#9a7445;
                    font-weight:700;
                "
            >
                {artisan["award"]}
            </p>


            <br>


            <a
                class="wine-link"
                href="?page=artisans&craft={craft_key}"
                target="_self"
            >
                ← Back to Artisans
            </a>


            <div
                class="detail-layout"

                style="
                    padding-left:0;
                    padding-right:0;
                "
            >


                <div class="info-panel">

                    <h2>
                        About
                    </h2>

                    <p>
                        {artisan["about"]}
                    </p>


                    <h2>
                        Craft Specialisation
                    </h2>

                    <p>
                        {artisan["specialisation"]}
                    </p>


                    <h2>
                        Heritage & Contribution
                    </h2>

                    <p>
                        {artisan["heritage"]}
                    </p>


                    <h2>
                        Associated Craft
                    </h2>

                    <p>
                        <strong>
                            {artisan["craft_name"]}
                        </strong>
                    </p>

                    <p>
                        {craft["overview"]}
                    </p>


                    <a
                        class="wine-link"
                        href="?page=details&craft={craft_key}"
                        target="_self"
                    >
                        Explore {artisan["craft_name"]}
                    </a>

                </div>


                <div class="fact-panel">

                    <div
                        style="
                            color:#9a7445;
                            font-size:10px;
                            letter-spacing:2px;
                            font-weight:700;
                        "
                    >
                        ARTISAN INFORMATION
                    </div>


                    <h3>
                        Profile Details
                    </h3>


                    <p>
                        <strong>
                            Name
                        </strong>

                        <br>

                        {artisan["name"]}
                    </p>


                    <p>
                        <strong>
                            Craft
                        </strong>

                        <br>

                        {artisan["craft_name"]}
                    </p>


                    <p>
                        <strong>
                            Location
                        </strong>

                        <br>

                        {artisan["location"]}
                    </p>


                    <p>
                        <strong>
                            Specialisation
                        </strong>

                        <br>

                        {artisan["specialisation"]}
                    </p>


                    <p>
                        <strong>
                            Recognition
                        </strong>

                        <br>

                        {artisan["award"]}
                    </p>


                    <p>
                        <strong>
                            Information Source
                        </strong>

                        <br>

                        {artisan["source_name"]}
                    </p>


                    <br>


                    <a
                        class="wine-link"
                        href="{artisan["source_url"]}"
                        target="_blank"
                    >
                        Verify Source ↗
                    </a>

                </div>

            </div>

        </main>
        """
    )

    footer()

# ============================================================
# ABOUT PAGE
# ============================================================


def about_page():

    navbar()

    banarasi_img = craft_image("Banarasi")

    st.html(
        f"""
        <main class="page">

            <div class="center-head">

                <div style="
                    color:#9a7445;
                    letter-spacing:2px;
                    font-size:10px;
                    font-weight:700;
                    margin-bottom:8px;
                ">
                    THE STORY BEHIND KARIGARI
                </div>

                <h1>Our Story</h1>

                <p>
                    Using technology to help people recognise
                    India's textile traditions, understand their
                    stories and discover the artisans behind them.
                </p>

            </div>


            <div class="about-grid">

                <div style="
                    min-height:360px;
                    border-radius:10px;
                    background:
                        linear-gradient(
                            rgba(35,15,10,.08),
                            rgba(35,15,10,.08)
                        ),
                        url('{banarasi_img}');
                    background-size:cover;
                    background-position:center;
                ">
                </div>


                <div class="about-copy">

                    <div style="
                        color:#9a7445;
                        font-size:10px;
                        letter-spacing:2px;
                        font-weight:700;
                    ">
                        WHY KARIGARI?
                    </div>

                    <h2>
                        More Than Just a Textile
                    </h2>

                    <p>
                        A traditional textile carries much more
                        than colour and pattern. It represents
                        regional identity, specialised techniques
                        and generations of craftsmanship.
                    </p>

                    <p>
                        Yet someone looking at a beautiful saree
                        may not know whether it is Banarasi,
                        Bandhani, Kanjeevaram, Patola or Tussar —
                        or know anything about the people who
                        preserve that tradition.
                    </p>

                    <p>
                        Karigari bridges this gap by combining
                        deep-learning based craft recognition
                        with cultural information and documented
                        artisan discovery.
                    </p>

                </div>

            </div>


            <div style="
                max-width:950px;
                margin:50px auto 20px;
                text-align:center;
            ">

                <h2 style="
                    font-family:'Playfair Display',serif;
                    font-size:30px;
                    margin-bottom:8px;
                ">
                    How Karigari Works
                </h2>

                <p style="
                    color:#756a60;
                    font-size:13px;
                ">
                    From an image to a deeper understanding
                    of India's living craft heritage.
                </p>

            </div>


            <div style="
                max-width:950px;
                margin:auto;
                display:grid;
                grid-template-columns:repeat(4,1fr);
                gap:14px;
            ">

                <div style="
                    background:#fffaf2;
                    border:1px solid #ded2c2;
                    border-radius:9px;
                    padding:24px;
                ">
                    <div style="
                        color:#9a7445;
                        font-size:11px;
                        font-weight:700;
                    ">
                        01
                    </div>

                    <h3 style="
                        font-family:'Playfair Display',serif;
                    ">
                        Upload
                    </h3>

                    <p style="
                        color:#756a60;
                        font-size:11px;
                        line-height:1.6;
                    ">
                        Upload a clear photograph of a textile,
                        saree, weave or motif.
                    </p>
                </div>


                <div style="
                    background:#fffaf2;
                    border:1px solid #ded2c2;
                    border-radius:9px;
                    padding:24px;
                ">
                    <div style="
                        color:#9a7445;
                        font-size:11px;
                        font-weight:700;
                    ">
                        02
                    </div>

                    <h3 style="
                        font-family:'Playfair Display',serif;
                    ">
                        Recognise
                    </h3>

                    <p style="
                        color:#756a60;
                        font-size:11px;
                        line-height:1.6;
                    ">
                        Our deep-learning model analyses
                        visual patterns and textile features.
                    </p>
                </div>


                <div style="
                    background:#fffaf2;
                    border:1px solid #ded2c2;
                    border-radius:9px;
                    padding:24px;
                ">
                    <div style="
                        color:#9a7445;
                        font-size:11px;
                        font-weight:700;
                    ">
                        03
                    </div>

                    <h3 style="
                        font-family:'Playfair Display',serif;
                    ">
                        Discover
                    </h3>

                    <p style="
                        color:#756a60;
                        font-size:11px;
                        line-height:1.6;
                    ">
                        Learn about the craft's region,
                        technique and cultural significance.
                    </p>
                </div>


                <div style="
                    background:#fffaf2;
                    border:1px solid #ded2c2;
                    border-radius:9px;
                    padding:24px;
                ">
                    <div style="
                        color:#9a7445;
                        font-size:11px;
                        font-weight:700;
                    ">
                        04
                    </div>

                    <h3 style="
                        font-family:'Playfair Display',serif;
                    ">
                        Meet the Makers
                    </h3>

                    <p style="
                        color:#756a60;
                        font-size:11px;
                        line-height:1.6;
                    ">
                        Discover documented artisans associated
                        with the recognised tradition.
                    </p>
                </div>

            </div>


            <div style="
                max-width:950px;
                margin:45px auto 0;
                background:#efe5d6;
                border-radius:12px;
                padding:38px;
                text-align:center;
            ">

                <div style="
                    color:#9a7445;
                    letter-spacing:2px;
                    font-size:10px;
                    font-weight:700;
                ">
                    OUR PURPOSE
                </div>

                <h2 style="
                    font-family:'Playfair Display',serif;
                    font-size:29px;
                    margin:12px 0;
                ">
                    From recognising patterns
                    to recognising people.
                </h2>

                <p style="
                    max-width:720px;
                    margin:auto;
                    color:#655b52;
                    line-height:1.8;
                    font-size:13px;
                ">
                    Karigari is designed not only to classify
                    textiles, but to make traditional craft
                    knowledge and the skilled people behind
                    these traditions more visible.
                </p>

            </div>


            <div style="
              max-width:950px;
             margin:25px auto 0;
              background:#fffaf2;
              border:1px solid #ded2c2;
              border-radius:10px;
              padding:25px;
            ">

              <strong>
                AI-Powered Craft Recognition
              </strong>

            <p style="
              color:#655b52;
              font-size:12px;
              line-height:1.7;
              margin-bottom:0;
            ">
        
             Karigari currently recognises five Indian textile
             traditions — Banarasi, Bandhani, Kanjeevaram,
             Patola and Tussar. Our recognition system analyses
             visual patterns, textures and weaving characteristics
             to suggest the most likely craft tradition.

             When the model is not sufficiently confident,
             Karigari clearly reports the result as uncertain
             instead of presenting an unreliable identification.
            </p>

</div>

        </main>
        """
    )

    footer()

# ============================================================
# FOOTER
# ============================================================


def footer():

    st.html("""
    <footer class="footer">

        <span>
            ✤ Karigari
        </span>

        <span>
            Recognising craft.
            Celebrating its makers.
        </span>

    </footer>
    """)


# ============================================================
# ROUTER
# ============================================================


page = st.query_params.get(
    "page",
    "home"
)


if page == "discover":

    discover_page()


elif page == "result":

    result_page()


elif page == "crafts":

    crafts_page()


elif page == "details":

    craft_details_page()


elif page == "artisans":

    artisans_page()


elif page == "artisan-profile":

    artisan_profile_page()


elif page == "about":

    about_page()


else:

    home_page() 