# AI-Powered Symptom Checker

## Overview
The **AI-Powered Symptom Checker** is a chatbot designed to analyze user-reported symptoms and predict possible diseases using advanced **Natural Language Processing (NLP)** models. It leverages **BERT/GPT-3.5 API** along with the **Symptom2Disease dataset** from Kaggle to provide accurate health insights. Users can interact via text or voice input using **Google Speech-to-Text**.

## Features
- **Symptom Analysis:** Predicts potential diseases based on user-input symptoms.
- **NLP Integration:** Uses **BERT/GPT-3.5** for accurate symptom interpretation.
- **Voice Input Support:** Enables users to input symptoms via **Google Speech-to-Text**.
- **User-Friendly Interface:** Simple chatbot-based interaction for ease of use.
- **Secure Data Processing:** Ensures privacy and confidentiality of user data.

## Tech Stack
- **Backend:** Python, Django/Flask
- **Machine Learning:** BERT, GPT-3.5 API, Symptom2Disease Dataset
- **Voice Processing:** Google Speech-to-Text API
- **Frontend:** HTML, CSS, JavaScript

## Installation & Setup
### Prerequisites
- Python 3+
- Virtual Environment (optional but recommended)
- Required libraries: Flask/Django, transformers, requests, SpeechRecognition

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/ai-symptom-checker.git
   cd ai-symptom-checker
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the application:
   ```sh
   python app.py
   ```

## Usage
- Enter symptoms via text or voice input.
- The AI processes the input and provides possible disease predictions.
- Users receive relevant medical insights based on predictions.

## Future Enhancements
- Improve disease prediction accuracy with more datasets.
- Add multilingual support.
- Integrate a doctor consultation feature.

## License
This project is **private and proprietary**. Unauthorized copying, modification, or distribution is strictly prohibited.
