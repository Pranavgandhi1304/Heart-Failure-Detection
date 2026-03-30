# Heart Failure Detection

## Description
This project is a machine learning application designed to detect heart failure using predictive models. It analyzes patient health data to assess the risk of heart failure, providing valuable insights for early diagnosis and medical intervention. The application features a user-friendly web interface built with Streamlit, allowing users to input patient parameters and receive predictions based on trained models.

## Features
- **Web Interface**: Interactive Streamlit app for easy data input and prediction visualization.
- **Pre-trained Model**: Uses a trained Random Forest model for heart failure risk prediction.
- **Data Scaling**: Applies standard scaling to numerical features for accurate predictions.
- **Data Exploration**: Visualizes dataset distributions and insights using pre-generated plots.
- **Prediction Page**: Dedicated interface for real-time heart failure risk assessment based on patient inputs.

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/Pranavgandhi1304/Heart-Failure-Detection
   cd heart-failure-detection
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the application locally:
```
streamlit run app.py
```
Open your browser and navigate to the provided local URL. Use the prediction page (`predict_page.py`) to input patient data such as age, blood pressure, cholesterol levels, etc., and get an instant heart failure risk prediction.

## Models and Techniques
The application uses a pre-trained Random Forest model saved in `Saved_steps.pkl`, which includes the trained classifier and a standard scaler for numerical features. The model predicts heart failure risk based on encoded categorical inputs and scaled numerical data. Data exploration is provided through `explore.py`, displaying visualizations from the `Images/` folder.

## Technologies Used
- **Python**: Core programming language.
- **Streamlit**: For building the web application.
- **Scikit-learn**: For the Random Forest model and standard scaling.
- **Pandas & NumPy**: For data manipulation and analysis.
- **Pillow**: For image handling in data exploration.

## Dataset
The model is trained on a heart failure dataset (e.g., from Kaggle or UCI repository). Ensure the dataset includes features like age, anemia, creatinine phosphokinase, diabetes, ejection fraction, high blood pressure, platelets, serum creatinine, serum sodium, sex, smoking, and time.

## Deployment
The project can be deployed on platforms like Streamlit Cloud or Heroku. For Heroku, use the provided `procfile` (if applicable).

Link to deployed project: https://heart-failure-detection-ngxwwryvgwfebqzkmyi9v5.streamlit.app

## Troubleshooting
- **Scikit-learn Version Mismatch**: If you encounter errors loading the saved model (`Saved_steps.pkl`), it may be due to sklearn version incompatibility. The model was trained with sklearn 0.24.2. Update to a compatible version or retrain the model with your current sklearn version.
- **Missing Dependencies**: Ensure all packages in `requirements.txt` are installed.
- **Image Loading Issues**: Verify that the `Images/` folder contains the required PNG files for data exploration.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request. For major changes, open an issue first to discuss what you would like to change.
 file for details.

## Acknowledgments
- Dataset source: [UCI Heart Failure Clinical Records](https://archive.ics.uci.edu/dataset/519/heart+failure+clinical+records) or similar.
- Inspired by advancements in AI for healthcare.
