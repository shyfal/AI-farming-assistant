🌿 AgriSense — AI Powered Farming Assistant

AgriSense is an AI-powered web application designed to help farmers detect crop diseases using plant leaf images and provide smart farming recommendations. The system uses image processing and Machine Learning concepts to analyze uploaded crop images and display disease predictions along with useful farming suggestions.

The frontend of the project is developed using HTML, CSS, and JavaScript with a modern responsive UI, while the backend is implemented using Flask and Python. The application allows users to upload crop leaf images through a web interface and receive disease diagnosis results instantly. The uploaded index.html file contains the complete responsive frontend design, upload functionality, preview section, prediction interface, recommendation module, and dynamic UI interactions.

🚀 Features
🌱 Crop disease detection using AI
📷 Upload crop leaf images
🔬 Disease prediction with confidence score
💡 Smart farming recommendations
🌦️ Weather and crop care suggestions
📱 Responsive modern web interface
🎨 Animated UI with farming theme

🛠️ Technologies Used
Component	Technology
Frontend	HTML, CSS, JavaScript
Backend	Python Flask
AI Model	TensorFlow / CNN
Image Processing	PIL, NumPy
Database	SQLite / Firebase (Optional)

📂 Project Structure
AgriSense/
│
├── app.py
├── model.h5
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── images/
├── dataset/
├── requirements.txt
└── README.md

⚙️ Installation
1. Clone Repository
git clone https://github.com/your-username/agrisense.git
cd agrisense
2. Install Dependencies
pip install flask tensorflow pillow numpy flask-cors
3. Run Application
python app.py
4. Open Browser
http://127.0.0.1:5000

🌿 How It Works
User uploads crop leaf image
Image is preprocessed and resized
AI/CNN model analyzes image patterns
Disease prediction is generated
Farming recommendations are displayed
📸 User Interface

The frontend interface includes:

Upload zone with drag-and-drop support
Image preview section
Disease prediction result card
Confidence score visualization
Farming recommendation cards
Interactive responsive UI

The interface is designed with animated backgrounds, floating leaf effects, modern cards, and responsive layouts for better user experience.

🧠 AI Model

The system uses a CNN (Convolutional Neural Network) model trained on crop leaf datasets to classify diseases such as:

Tomato Early Blight
Potato Late Blight
Corn Leaf Rust
Healthy Leaf

The AI model analyzes visual features such as:

Leaf spots
Texture variations
Color changes
Disease symptoms

📊 Output Example
Disease: Tomato Early Blight
Confidence: 91.4%
Recommendation: Use copper-based fungicide

🔮 Future Enhancements
Mobile application support
Real-time weather API integration
Multilingual support for farmers
Advanced Deep Learning models
Live agricultural expert consultation

📌 Advantages
Easy to use
Fast prediction
Supports smart farming
Reduces crop loss
Accessible through web browser

⚠️ Limitations
Depends on dataset quality
Requires internet connection
Limited to trained crop diseases

👨‍💻 Developed By

Shyfal
Computer Science and Engineering
KPR Institute of Engineering and Technology
