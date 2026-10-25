# 🪡 Karigari — AI-Powered Indian Craft Recognition

**Karigari** is an AI-powered platform designed to recognise traditional Indian textile crafts from images and connect users with the cultural stories and documented artisans behind them.

The project combines **deep learning, computer vision and an interactive web experience** to make Indian textile heritage easier to recognise, understand and explore.

🌐 **Live Application:**  
https://karigari-ai.streamlit.app

---

## ✨ What Karigari Does

Upload an image of a textile, saree, weave or motif and Karigari:

1. Analyses the image using a fine-tuned deep-learning model.
2. Predicts the most likely traditional craft.
3. Displays confidence scores and alternative predictions.
4. Provides information about the craft's region, technique and cultural significance.
5. Connects the recognised craft with documented artisans and weavers.

---

## 🧵 Crafts Currently Recognised

Karigari currently recognises five Indian textile traditions:

| Craft | Associated Region |
|---|---|
| Banarasi | Varanasi, Uttar Pradesh |
| Bandhani | Gujarat / Rajasthan |
| Kanjeevaram | Kanchipuram, Tamil Nadu |
| Patola | Patan, Gujarat |
| Tussar | Eastern and Central India |

---

## 🤖 AI Model

The craft recognition system is based on **EfficientNetB0** using transfer learning.

### Dataset

The final dataset contains:

- **5 craft classes**
- **1,600 training images**
- **200 validation images**
- **200 test images**
- **2,000 images in total**

Each class contains:

- 320 training images
- 40 validation images
- 40 test images

### Training Strategy

The model was developed in two stages:

**Stage 1 — Transfer Learning**

The pretrained EfficientNetB0 backbone was initially frozen while a new classification head was trained for the five craft categories.

**Stage 2 — Fine-Tuning**

Selected EfficientNet layers were then fine-tuned using a lower learning rate to improve craft-specific feature recognition.

---

## 📊 Model Performance

Final performance on the held-out test set:

**Test Accuracy: 80.50%**

**Test Loss: 0.6487**

| Craft | Precision | Recall | F1 Score |
|---|---:|---:|---:|
| Banarasi | 0.7632 | 0.7250 | 0.7436 |
| Bandhani | 0.7857 | 0.8250 | 0.8049 |
| Kanjeevaram | 0.7391 | 0.8500 | 0.7907 |
| Patola | 0.8571 | 0.7500 | 0.8000 |
| Tussar | 0.8974 | 0.8750 | 0.8861 |

**Macro F1 Score: 0.8050**

Tussar achieved the strongest F1 score, while visually similar textile patterns created some confusion between other classes.

---

## 🛡️ Confidence-Aware Prediction

Karigari does not blindly display every model prediction as a definite identification.

A **55% confidence threshold** is used.

If the highest model confidence is below the threshold, the application displays:

> **Identification Uncertain**

The user is then shown the strongest possible matches and encouraged to upload a clearer photograph.

This helps prevent low-confidence predictions from being presented as reliable identifications.

---

## 👨‍🎨 Artisan Discovery

Karigari extends beyond image classification by connecting craft recognition with documented artisans.

Current artisan profiles include representatives associated with:

- Banarasi weaving
- Bandhani
- Kanjeevaram silk
- Patan Patola
- Tussar / Kosa silk

Artisan profiles contain available information such as:

- Name
- Craft
- Location
- Specialisation
- Recognition / awards
- Heritage contribution
- Reference source

Users can search artisans by **name, craft or location** and filter the directory by craft.

---

## 🖥️ Application Features

### Home
Introduces Karigari and provides access to craft recognition, the craft library and artisan discovery.

### Discover
Allows users to upload a textile image and run AI-based recognition.

### Identification Result
Displays:

- Predicted craft
- Confidence score
- Top three model predictions
- Craft overview
- Technique
- Cultural significance
- Associated artisan

### Craft Library
Provides a visual library of the textile traditions currently supported by the model.

### Craft Details
Contains information about:

- Region
- Materials
- Technique
- Cultural significance
- Common motifs
- Associated artisans

### Artisan Directory
Provides searchable and craft-filtered documented artisan profiles.

### Artisan Profile
Displays artisan information, craft specialisation, recognition and reference sources.

### About
Explains Karigari's purpose and the relationship between AI recognition, cultural discovery and artisan visibility.

---

## 🏗️ System Architecture

```text
User
  │
  ▼
Streamlit Web Application
  │
  ▼
Image Upload
  │
  ▼
Image Preprocessing
224 × 224 RGB
  │
  ▼
ONNX Runtime
  │
  ▼
Fine-Tuned EfficientNetB0
  │
  ▼
5-Class Prediction
  │
  ├── Confidence ≥ 55%
  │        │
  │        ▼
  │   Craft Identified
  │        │
  │        ├── Craft Information
  │        └── Artisan Discovery
  │
  └── Confidence < 55%
           │
           ▼
     Identification Uncertain
```

---

## ⚙️ Technology Stack

### Machine Learning
- Python
- TensorFlow / Keras
- EfficientNetB0
- Transfer Learning
- Fine-Tuning
- NumPy

### Deployment Inference
- ONNX
- ONNX Runtime

### Frontend
- Streamlit
- HTML
- CSS

### Image Processing
- Pillow

### Development & Deployment
- Google Colab
- Visual Studio Code
- Git
- GitHub
- Streamlit Community Cloud

---

## 📁 Project Structure

```text
Karigari-AI/
│
├── app.py
│
├── requirements.txt
├── README.md
│
├── .gitignore
│
├── assets/
│   ├── styles.css
│   └── images/
│       ├── banarasi.jpg
│       ├── bandhani.jpg
│       ├── kanjeevaram.jpg
│       ├── patola.jpg
│       ├── tussar.jpg
│       └── artisans/
│
├── data/
│   ├── artisans.py
│   ├── craft_info.py
│   ├── artisans.json
│   └── crafts.json
│
├── model/
│   ├── karigari_model.onnx
│   └── class_names.json
│
└── pages/
    └── discover.py
```

---

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/KairaviMalik/Karigari-AI.git
cd Karigari-AI
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate it

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Start Karigari

```bash
streamlit run app.py
```

Open the local Streamlit URL shown in the terminal.

---

## 📦 Deployment

The deployed application performs inference directly using the ONNX model.

```text
Streamlit
    ↓
ONNX Runtime
    ↓
karigari_model.onnx
    ↓
Prediction
```

This means the deployed application does **not require a continuously running Colab notebook, Flask server or ngrok tunnel**.

---

## ⚠️ Current Limitations

Karigari currently supports only five textile traditions.

Recognition performance may be affected by:

- Poor lighting
- Blurry photographs
- Complex backgrounds
- Very distant textile images
- Visually similar patterns between crafts
- Images outside the model's trained classes

The prediction should therefore be treated as an AI-assisted craft recognition result rather than expert authentication of a textile.

---

## 🔮 Future Scope

Future versions of Karigari can include:

- More Indian weaving traditions
- Embroidery recognition
- Block-print recognition
- Handicraft recognition
- Larger and more diverse training datasets
- Improved model accuracy
- Multilingual cultural information
- Geographic craft exploration
- Expanded artisan directories
- Artisan onboarding
- Direct artisan-product discovery
- Mobile-first recognition

---

## 🌿 Vision

Karigari explores how artificial intelligence can support cultural discovery without separating a craft from the people and traditions behind it.

> **From recognising patterns to recognising people.**

---

## 🔗 Links

**Live Application:**  
https://karigari-ai.streamlit.app

**GitHub Repository:**  
https://github.com/KairaviMalik/Karigari-AI