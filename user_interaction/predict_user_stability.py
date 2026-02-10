def predict_user_stability(model, user_features):
    
    prediction = model.predict(user_features)[0]
    return "STABLE✅" if prediction == 1 else "UNSTABLE⚠️"
