import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np
import time

# ===============================
# ✅ APP CONFIG
# ===============================
st.set_page_config(
    page_title="AI Plant Disease Detection",
    page_icon="🌱",
    layout="centered"
)

# ===============================
# ✅ LOAD MODEL (CACHED)
# ===============================
@st.cache_resource
def load_model():
    tf.keras.backend.clear_session()
    return tf.keras.models.load_model("best_model_2.h5")

model = load_model()

def infer(x):
    return model.predict(x)

# ===============================
# ✅ CLASS NAMES (IN ORDER)
# ===============================
class_names = [
    'Apple___Apple_scab','Apple___Black_rot','Apple___Cedar_apple_rust','Apple___healthy',
    'Blueberry___healthy','Cherry___Powdery_mildew','Cherry___healthy',
    'Corn___Cercospora_leaf_spot','Corn___Common_rust','Corn___Northern_Leaf_Blight','Corn___healthy',
    'Grape___Black_rot','Grape___Esca','Grape___Leaf_blight','Grape___healthy',
    'Orange___Citrus_greening','Peach___Bacterial_spot','Peach___healthy',
    'Pepper___Bacterial_spot','Pepper___healthy','Potato___Early_blight','Potato___Late_blight','Potato___healthy',
    'Raspberry___healthy','Soybean___healthy','Squash___Powdery_mildew',
    'Strawberry___Leaf_scorch','Strawberry___healthy','Tomato___Bacterial_spot','Tomato___Early_blight',
    'Tomato___Late_blight','Tomato___Leaf_Mold','Tomato___Septoria_leaf_spot',
    'Tomato___Spider_mites','Tomato___Target_Spot','Tomato___Yellow_Leaf_Curl_Virus',
    'Tomato___Mosaic_virus','Tomato___healthy'
]

# ===============================
# ✅ DISEASE INFO & REMEDIES
# ===============================
disease_info = {
    "Apple___Apple_scab": {
        "description": "Fungal disease causing dark scaly spots on leaves and fruit.",
        "remedy": "Use fungicides like captan or mancozeb. Remove infected leaves."
    },
    "Potato___Late_blight": {
        "description": "Rapidly spreading disease causing leaf decay and tuber rot.",
        "remedy": "Apply copper fungicide. Destroy infected plants immediately."
    },
    "Tomato___Bacterial_spot": {
        "description": "Bacterial disease causing dark lesions on leaves and fruits.",
        "remedy": "Use copper sprays and certified seeds."
    }
}

# ===============================
# ✅ IMAGE PREPROCESSING
# ===============================
def preprocess_image(image):
    image = image.resize((256, 256))
    image = np.array(image) / 255.0
    image = image.astype("float32")
    return np.expand_dims(image, axis=0)

# ===============================
# ✅ UI HEADER
# ===============================
st.title("🌱 AI Plant Disease Detection System")
st.caption("Upload a leaf image to detect plant disease using Deep Learning.")

with st.sidebar:
    st.header("ℹ️ About")
    st.write("AI-based system to detect 38+ plant diseases.")
    st.warning("⚠️ Avoid stock/watermarked images for best accuracy.")
    st.write("Built with TensorFlow & Streamlit")
    st.write("© Akash Malik")

# ===============================
# ✅ FILE UPLOADER
# ===============================
uploaded_file = st.file_uploader("📤 Upload a plant leaf image", type=["jpg", "jpeg", "png"])

# ===============================
# ✅ MAIN PREDICTION LOGIC
# ===============================
if uploaded_file:
    try:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Uploaded Image", use_container_width=True)
        st.info(f"🖼️ Image Size: {image.size[0]} x {image.size[1]}")

        with st.spinner("🔍 Analyzing Image..."):
            time.sleep(1.2)
            processed_image = preprocess_image(image)
            predictions = infer(processed_image)[0]

        # ✅ TOP 3 PREDICTIONS
        top_3_idx = np.argsort(predictions)[-3:][::-1]
        top_1_class = class_names[top_3_idx[0]]
        top_1_conf = predictions[top_3_idx[0]] * 100

        st.success(f"✅ Prediction: {top_1_class}")
        st.metric("🎯 Confidence", f"{top_1_conf:.2f}%")

        # ✅ HEALTH STATUS
        if "healthy" in top_1_class.lower():
            st.success("🌿 Plant Status: Healthy")
        else:
            st.error("⚠️ Plant Status: Diseased")

        # ✅ CONFIDENCE INDICATOR
        if top_1_conf > 80:
            st.success("✅ High Confidence Prediction")
        elif top_1_conf > 60:
            st.warning("⚠️ Medium Confidence Prediction")
        else:
            st.error("❌ Low Confidence Prediction")

        # ✅ DISEASE INFO
        if top_1_class in disease_info:
            st.subheader("🧠 Disease Information")
            st.write("**Description:**", disease_info[top_1_class]["description"])
            st.write("**Recommended Remedy:**", disease_info[top_1_class]["remedy"])

        # ✅ TOP 3 TABLE
        st.subheader("📊 Top 3 Predictions")
        st.table({
            "Disease": [class_names[i] for i in top_3_idx],
            "Confidence %": [round(predictions[i] * 100, 2) for i in top_3_idx]
        })

        # ✅ BAR CHART
        st.subheader("📈 Prediction Probability Distribution")
        chart_data = {class_names[i]: predictions[i] * 100 for i in top_3_idx}
        st.bar_chart(chart_data)

        st.balloons()

    except Exception as e:
        st.error("❌ Error while processing the image.")
        st.exception(e)

# ===============================
# ✅ FOOTER
# ===============================
st.divider()
st.caption("🚀 AI Plant Disease Detection | Final Year / Internship Ready Project")
