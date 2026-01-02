# AI-Powered Disease Prediction System

An end-to-end **AI-powered web application** that predicts **possible diseases based on user-selected symptoms** using **machine learning**.  
The system is trained on a **Kaggle disease–symptom dataset** and provides **multiple disease predictions with confidence scores above 10%**, ensuring realistic and informative results.

> This project is developed for **educational purposes only** and does **not replace professional medical advice**.


## Project Overview

Early identification of diseases based on symptoms can help users become more aware of potential health issues.  
This project leverages **machine learning and a user-friendly web interface** to allow users to:

- Select symptoms easily (without overwhelming checklists)
- Get **multiple possible diseases**, not just one
- View **confidence percentages** for each predicted disease
- Interact with a clean, modern, and intuitive UI


## Key Features

- **Smart Symptom Search**
  - Autocomplete-based symptom selection
  - No cluttered checkboxes

- **Machine Learning Powered**
  - Trained on Kaggle Disease Prediction Dataset
  - Uses Random Forest Classifier for high accuracy

- **Confidence-Based Results**
  - Displays all diseases with confidence ≥ 10%
  - Results sorted by highest probability

- **Attractive & User-Friendly UI**
  - Modern card-based design
  - Confidence bars for easy interpretation
  - Responsive layout

- **Web-Based Application**
  - Flask backend
  - HTML, CSS, JavaScript frontend


## Tech Stack

### Backend & ML
- Python
- Flask
- Scikit-learn
- Pandas, NumPy
- Joblib

### Frontend
- HTML5
- CSS3
- JavaScript (Fetch API)

### Dataset
- Kaggle Disease Prediction Dataset (Symptoms → Disease mapping)


## Project Structure

DISEASE_PREDICTION_SYSTEM/
- app.py
- requirements.txt
- README.md
- dataset/
   - Training.csv
   - Testing.csv
- model/
   - train_model.py
   - evaluate_model.py
   - disease_model.pkl
   - label_encoder.pkl
   - features.pkl
- static/
   - style.css
- templates/
   - index.html


## How the System Works

1. **Model Training**
   - The ML model is trained using symptom-based data
   - Each symptom is treated as a binary feature
   - Diseases are label-encoded for classification

2. **User Interaction**
   - User searches and selects symptoms
   - Selected symptoms are converted into a binary input vector

3. **Prediction**
   - The trained model calculates probabilities using `predict_proba()`
   - All diseases with confidence ≥ 10% are returned
   - Results are sorted by confidence

4. **Display**
   - Diseases are shown with confidence percentages
   - Visual confidence bars improve readability


## How to Run the Project Locally

1. Clone the Repository
git clone https://github.com/your-username/ai-disease-prediction-system.git
cd ai-disease-prediction-system

3. Install Dependencies
pip install -r requirements.txt

4. Train the Model (Once)
cd model
python train_model.py

5. Run the Application
cd ..
python app.py

6. Open in Browser
http://127.0.0.1:5000


**Sample Symptoms for Testing**

Example:
high_fever
headache
joint_pain
nausea
Expected Output:

Dengue        ~75%
Viral Fever  ~18%
Malaria      ~12%


**Model Performance**
Algorithm: Random Forest Classifier
Handles multi-class classification efficiently
Trained on full Kaggle dataset
Evaluated using separate testing data


**Future Enhancements**
Disease descriptions & precautions
Severity level indicator
Dark mode UI
Voice-based symptom input
Online deployment (Render / Railway)

**Use Cases**
College minor/major project
Machine Learning portfolio project
Resume & GitHub showcase
Web + ML integration demonstration

**Disclaimer**
This system is intended only for educational and learning purposes.
It should not be used for real medical diagnosis or treatment decisions.
Always consult a qualified medical professional.
