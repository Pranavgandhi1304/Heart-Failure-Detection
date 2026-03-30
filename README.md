# Heart Failure Detection

## Description
This project is a machine learning application designed to detect heart failure using predictive models. It analyzes patient health data to assess the risk of heart failure, providing valuable insights for early diagnosis and medical intervention. The application features a user-friendly web interface built with Streamlit, allowing users to input patient parameters and receive predictions based on trained models.

## Features
- **Web Interface**: Interactive Streamlit app for easy data input and prediction visualization.
- **Multiple Models**: Implements various machine learning algorithms including Random Forest, Deep Learning (Neural Networks), and Ensemble methods for robust predictions.
- **Model Tuning**: Includes scripts for hyperparameter tuning to optimize model performance.
- **Data Exploration**: Tools for analyzing and visualizing the dataset to understand key features.
- **Prediction Page**: Dedicated interface for real-time heart failure risk assessment.

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

3. (Optional) Run the setup script for additional configurations:
   ```
   bash setup.sh
   ```

## Usage
To run the application locally:
```
streamlit run app.py
```
Open your browser and navigate to the provided local URL. Use the prediction page (`predict_page.py`) to input patient data such as age, blood pressure, cholesterol levels, etc., and get an instant heart failure risk prediction.

## Models and Techniques
The project includes several machine learning components:
- **Random Forest Tuning** (`Random_Forest_tuning.py`): Optimizes Random Forest parameters for better accuracy.
- **Deep Learning Tuning** (`DL-Tuning.py`): Fine-tunes neural network models for heart failure prediction.
- **Ensemble Methods** (`ensemble.py`): Combines multiple models to improve overall prediction reliability.
- **Data Exploration** (`explore.py`): Scripts for data preprocessing, visualization, and feature engineering.
- **ML Techniques** (`MLTECH.py`): General machine learning utilities and techniques applied to the dataset.

## Technologies Used
- **Python**: Core programming language.
- **Streamlit**: For building the web application.
- **Scikit-learn**: For traditional ML models like Random Forest.
- **TensorFlow/Keras**: For deep learning implementations.
- **Pandas & NumPy**: For data manipulation and analysis.
- **Matplotlib/Seaborn**: For data visualization (assumed based on typical ML projects).

## Dataset
The model is trained on a heart failure dataset (e.g., from Kaggle or UCI repository). Ensure the dataset includes features like age, anemia, creatinine phosphokinase, diabetes, ejection fraction, high blood pressure, platelets, serum creatinine, serum sodium, sex, smoking, and time.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request. For major changes, open an issue first to discuss what you would like to change.

## Acknowledgments
- Dataset source: [UCI Heart Failure Clinical Records](https://archive.ics.uci.edu/dataset/519/heart+failure+clinical+records) or similar.
- Inspired by advancements in AI for healthcare.
