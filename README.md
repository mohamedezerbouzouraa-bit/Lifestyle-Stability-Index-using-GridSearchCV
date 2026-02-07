# Lifestyle-Stability-Index-using-GridSearchCV
Lifestyle Stability Index (LSI-Predictor) estimates lifestyle consistency from sleep, steps, screen time, and bedtime variability.  Trains an SVC with GridSearchCV to classify STABLE vs UNSTABLE routines.  Interactive CLI lets users predict their own lifestyle stability in real-time.
📖 Project Overview

LSI-GridSearch predicts how stable your lifestyle is, based on:

🛏️ Sleep & sleep variability

👣 Daily steps & activity variability

📱 Screen time & its consistency

🌙 Bedtime regularity

It uses Support Vector Classification (SVC) with hyperparameter tuning via GridSearchCV to find the best model for classifying routines as:

STABLE ✅

UNSTABLE ⚠️

You can interactively enter your own lifestyle metrics and see your predicted stability!

✨ Features

✅ Deterministic dataset for reproducibility

🧪 SVC pipeline with StandardScaler

🔍 GridSearchCV for hyperparameter optimization (C, gamma, kernel)

📊 Train/test evaluation for model performance

🖥️ Interactive CLI for predicting your own lifestyle stability

🗂️ Modular structure for scalability
