from src.data_loader import load_data
from src.model_training import train_model
from src.user_interaction import get_user_input, predict_user_stability

X, y = load_data()
best_model, gs, X_test, y_test = train_model(X, y)
print("Best CV Accuracy:", gs.best_score_)
print("Best Hyperparameters:", gs.best_params_)
print("Test Accuracy:", best_model.score(X_test, y_test))
user_features = get_user_input()
if user_features is not None:
    result = predict_user_stability(best_model, user_features)
    print("Your lifestyle is predicted to be", result)
