# Skin Sense AI

**Skin Sense AI** is an advanced platform leveraging machine learning to assist in the detection and management of skin diseases. Designed to focus on critical skin health, this project combines image-based disease detection with comprehensive resources about skin conditions and their treatments, empowering users to take proactive steps toward better skin health.

## Features

1. **Skin Disease Detection**
   - Input: Image of a skin condition.
   - Output: Predicted disease classification with detailed analysis.

2. **Comprehensive Skin Disease Glossary**
   - Provides detailed information on various skin diseases, including causes, symptoms, and risks.

3. **Treatment Guidance**
   - Offers personalized suggestions for managing and treating identified skin conditions.

## Technology Stack

- **Programming Language**: Python
- **Machine Learning Framework**: TensorFlow/Keras
- **Pretrained Model**: EfficientNetV2 (Fine-tuned)
- **Dataset**: Sourced from Kaggle, organized into folders by disease categories.
- **Deployment**: Streamlit for the web interface

## How to Replicate

Follow these steps to replicate the project on your system:

### 1. Prerequisites

- Python 3.8 or higher installed on your system.
- GPU support (optional but recommended for faster training and inference).

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/skin-sense-ai.git
cd skin-sense-ai
```

### 3. Install Dependencies

Create a virtual environment and install the required packages:

```bash
python -m venv env
source env/bin/activate # For Linux/Mac
# or
env\Scripts\activate # For Windows

pip install -r requirements.txt
```

### 4. Dataset Setup

1. Download the dataset from Kaggle (linked in the repository).
2. Extract the dataset and place it in the `data/` directory.

### 5. Model Training

To train the model using the provided dataset:

```bash
python train.py
```

### 6. Run the Application

Start the Streamlit web app:

```bash
streamlit run dashboard/dashboard.py
```

### 7. Access the Application

Open your browser and go to `http://localhost:8501` to use the app.

## Contributing

We welcome contributions! If you'd like to improve the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature/bug fix.
3. Submit a pull request with detailed information about your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

For questions or support, please contact us through the issues page on GitHub or via email at support@skinsense.ai.
