import tkinter as tk
from tkinter import messagebox
import numpy as np
import pickle

# Full path to your trained model (no scaler needed)
model_path = r"C:/Users/HP 15/Desktop/Rocheston Project/AI-diabetes-risk-assessment/Diabetesmodel.pkl"

# Load model only
try:
    with open(model_path, "rb") as f:
        model = pickle.load(f)
except Exception as e:
    print("Error loading model:", e)
    exit()

def predict_diabetes():
    try:
        # Get user input as floats
        glucose = float(entry_glucose.get())
        bp = float(entry_bp.get())
        bmi = float(entry_bmi.get())
        age = float(entry_age.get())

        # Prepare input array (raw values, no scaling)
        input_data = np.array([[glucose, bp, bmi, age]])

        # Predict directly with the model
        prediction = model.predict(input_data)

        # Show result
        result = "Diabetic" if prediction[0] == 1 else "Not Diabetic"
        messagebox.showinfo("Prediction Result", f"The person is likely: {result}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for all fields.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Setup GUI
root = tk.Tk()
root.title("Diabetes Risk Assessment")
root.geometry("400x300")
root.config(bg="#f2f2f2")

tk.Label(root, text="Diabetes Risk Checker", font=("Helvetica", 16, "bold"), bg="#f2f2f2").pack(pady=10)

frame = tk.Frame(root, bg="#f2f2f2")
frame.pack(pady=10)

tk.Label(frame, text="Glucose Level:", bg="#f2f2f2").grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_glucose = tk.Entry(frame)
entry_glucose.grid(row=0, column=1, padx=5)

tk.Label(frame, text="Blood Pressure:", bg="#f2f2f2").grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_bp = tk.Entry(frame)
entry_bp.grid(row=1, column=1, padx=5)

tk.Label(frame, text="BMI:", bg="#f2f2f2").grid(row=2, column=0, sticky="e", padx=5, pady=5)
entry_bmi = tk.Entry(frame)
entry_bmi.grid(row=2, column=1, padx=5)

tk.Label(frame, text="Age:", bg="#f2f2f2").grid(row=3, column=0, sticky="e", padx=5, pady=5)
entry_age = tk.Entry(frame)
entry_age.grid(row=3, column=1, padx=5)

tk.Button(root, text="Predict Diabetes", command=predict_diabetes, bg="#4CAF50", fg="white", width=20).pack(pady=20)

root.mainloop()
