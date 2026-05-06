from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
from PIL import Image
import io
import os
import random

# ── Flask app ─────────────────────────────────────────────
app = Flask(__name__)
CORS(app)

# ── Disable model (IMPORTANT FIX) ─────────────────────────
USE_MODEL = False   # 🔥 Always use mock (no error)

# ── Mock Results ─────────────────────────────────────────
MOCK_RESULTS = [
    {"disease": "Tomato Early Blight", "confidence": 91.4},
    {"disease": "Potato Late Blight", "confidence": 87.2},
    {"disease": "Corn Common Rust", "confidence": 83.5},
    {"disease": "Healthy Leaf", "confidence": 96.8},
]

def mock_predict():
    result = random.choice(MOCK_RESULTS)
    return result["disease"], result["confidence"]

# ── Image Preprocessing (optional) ───────────────────────
def preprocess_image(file_bytes):
    img = Image.open(io.BytesIO(file_bytes)).convert("RGB")
    img = img.resize((224, 224))
    arr = np.array(img) / 255.0
    arr = np.expand_dims(arr, axis=0)
    return arr

# ── Routes ───────────────────────────────────────────────

@app.route("/")
def home():
    return jsonify({"message": "AI Farming Assistant Running 🌿"})

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "Empty file"}), 400

    try:
        file_bytes = file.read()

        # 🔥 Always use mock (safe)
        disease, confidence = mock_predict()

        return jsonify({
            "disease": disease,
            "confidence": confidence,
            "status": "success"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ── Run App ──────────────────────────────────────────────
if __name__ == "__main__":
    print("🌿 Server running at http://127.0.0.1:5000")
    app.run(debug=True)