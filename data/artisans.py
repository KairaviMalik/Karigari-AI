ARTISANS = {

    "naseem-ahmad": {

        "name": "Naseem Ahmad",
        "craft": "Banarasi",
        "craft_name": "Banarasi Brocade",
        "location": "Varanasi, Uttar Pradesh",
        "title": "Master Weaver",
        "award": "National Award, 2008",

        "image": "assets/images/artisans/naseem-ahmad.jpg",

        "specialisation": (
            "Banarasi silk brocade, traditional Jala/Naqsha "
            "weaving and handloom textile design"
        ),

        "about": (
            "Naseem Ahmad is a master weaver from Varanasi "
            "associated with the traditional Banarasi handloom "
            "tradition. His work includes the Jala or Naqsha "
            "system used for producing complex woven designs "
            "in Banarasi silk brocades."
        ),

        "heritage": (
            "He has contributed to preserving traditional "
            "handloom knowledge and training younger weavers "
            "in Varanasi."
        ),

        "verified": True,

        "source_name": "Powerhouse Collection",

        "source_url": (
            "https://collection.powerhouse.com.au/object/735579"
        )
    },


    "mohammad-alimohammad-khatri": {

        "name": "Mohammad Alimohammad Khatri",
        "craft": "Bandhani",
        "craft_name": "Bandhani",
        "location": "Kutch, Gujarat",
        "title": "Master Bandhani Artisan",
        "award": "Shilp Guru",

        "image": "assets/images/artisans/mohammad-khatri.jpg",

        "specialisation": (
            "Traditional Bandhani tie-and-dye craft"
        ),

        "about": (
            "Mohammad Alimohammad Khatri is a documented "
            "Bandhani craftsperson from Kutch, Gujarat. "
            "His discipline is traditional Tie & Dye "
            "(Bandhani)."
        ),

        "heritage": (
            "Bandhani involves carefully tying small sections "
            "of cloth before dyeing to create intricate resist "
            "patterns. His recognition as a Shilp Guru reflects "
            "his contribution to this traditional craft."
        ),

        "verified": True,

        "source_name": "Government Handicrafts Artisan List",

        "source_url": (
            "https://surajkundmelaauthority.org/"
            "WriteReadData/downloads/handicraft_2020.pdf"
        )
    },


    "b-krishnamoorthy": {

        "name": "B. Krishnamoorthy",
        "craft": "Kanjeevaram",
        "craft_name": "Kanjeevaram Silk",
        "location": "Kanchipuram, Tamil Nadu",
        "title": "Master Weaver & Textile Designer",
        "award": "National Award Winner",

        "image": "assets/images/artisans/b-krishnamoorthy.jpg",

        "specialisation": (
            "Kanchipuram silk saree weaving, traditional "
            "motifs and textile design"
        ),

        "about": (
            "B. Krishnamoorthy is a master weaver and "
            "traditional textile designer from Kanchipuram. "
            "He is known for Kanchipuram silk weaving and "
            "for documenting a large collection of traditional "
            "motifs and designs."
        ),

        "heritage": (
            "His work combines weaving, design documentation "
            "and preservation of traditional Kanchipuram motifs. "
            "He has also shared traditional weaving knowledge "
            "with students and other practitioners."
        ),

        "verified": True,

        "source_name": "The New Indian Express",

        "source_url": (
            "https://www.newindianexpress.com/cities/chennai/"
            "2015/Oct/20/he-wove-5000-designs-in-one-saree-"
            "with-not-a-single-repeat-831899.html"
        )
    },


    "rahul-salvi": {

        "name": "Rahul Vinayak Salvi",
        "craft": "Patola",
        "craft_name": "Patan Patola",
        "location": "Patan, Gujarat",
        "title": "Master Patola Weaver",
        "award": "Traditional Master Weaver",

        "image": "assets/images/artisans/rahul-salvi.jpg",

        "specialisation": (
            "Double Ikat Patola weaving using traditional "
            "resist-dyed warp and weft"
        ),

        "about": (
            "Rahul Vinayak Salvi is a master Patola weaver "
            "from Patan, Gujarat. He belongs to a family whose "
            "Patola weaving tradition spans many generations."
        ),

        "heritage": (
            "Traditional Patola requires both warp and weft "
            "threads to be resist-dyed and precisely aligned "
            "during weaving. The Salvi family is closely "
            "associated with preserving this highly specialised "
            "double-Ikat tradition."
        ),

        "verified": True,

        "source_name": "UNESCO",

        "source_url": (
            "https://www.unesco.org/sites/default/files/"
            "medias/fichiers/2022/11/382921eng.pdf"
        )
    },


    "nilamber-prasad-dewangan": {

        "name": "Nilamber Prasad Dewangan",
        "craft": "Tussar",
        "craft_name": "Tussar / Kosa Silk",
        "location": "Janjgir-Champa, Chhattisgarh",
        "title": "Master Handloom Weaver",
        "award": "National Award, 2002",

        "image": "assets/images/artisans/nilamber-dewangan.jpg",

        "specialisation": (
            "Traditional Tussar/Kosa silk saree weaving, "
            "Patiya (Khapa) technique and zari work"
        ),

        "about": (
            "Nilamber Prasad Dewangan is a National Award-winning "
            "handloom weaver from Chandrapur in Janjgir-Champa, "
            "Chhattisgarh. His work is associated with traditional "
            "Tussar, also locally known as Kosa silk."
        ),

        "heritage": (
            "Government handloom documentation describes his "
            "traditional Tussar silk saree work using Tussar "
            "silk yarn, golden zari and the Patiya or Khapa "
            "weaving technique."
        ),

        "verified": True,

        "source_name": (
            "Office of Development Commissioner for Handlooms"
        ),

        "source_url": (
            "https://www.handlooms.gov.in/assets/img/"
            "Weavers%20Database/"
            "Chhattisgarh637322642752617722.pdf"
        )
    }
}


# ============================================================
# CRAFT → ARTISAN MAPPING
# ============================================================

CRAFT_ARTISANS = {

    "Banarasi": [
        "naseem-ahmad"
    ],

    "Bandhani": [
        "mohammad-alimohammad-khatri"
    ],

    "Kanjeevaram": [
        "b-krishnamoorthy"
    ],

    "Patola": [
        "rahul-salvi"
    ],

    "Tussar": [
        "nilamber-prasad-dewangan"
    ]
}


# ============================================================
# HELPERS
# ============================================================

def get_artisan(artisan_id):

    return ARTISANS.get(
        artisan_id
    )


def get_artisans_for_craft(craft):

    ids = CRAFT_ARTISANS.get(
        craft,
        []
    )

    return [
        ARTISANS[artisan_id]
        for artisan_id in ids
        if artisan_id in ARTISANS
    ]


def get_artisan_ids_for_craft(craft):

    return CRAFT_ARTISANS.get(
        craft,
        []
    )


def get_artisan_image(artisan_id):

    artisan = ARTISANS.get(
        artisan_id
    )

    if not artisan:
        return None

    return artisan.get(
        "image"
    )