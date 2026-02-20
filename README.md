# 🩺 Diabetes Prediction Web App

A Machine Learning based web application that predicts whether a person is diabetic or non-diabetic using medical parameters.
The app is built using **Python, Scikit-Learn and Streamlit** and provides instant prediction along with visualization graphs.

---

## 📌 Features

* Simple and interactive UI
* Real-time prediction
* Probability score display
* Graph visualization
* Easy to use sliders for input
* Instant result after clicking **Predict**

---

## 🧠 Machine Learning Model

The model is trained using the **PIMA Indians Diabetes Dataset**.

### Input Features

* Pregnancies
* Glucose Level
* Blood Pressure
* Skin Thickness
* Insulin Level
* BMI (Body Mass Index)
* Diabetes Pedigree Function
* Age

### Output

* **0 → Non-Diabetic**
* **1 → Diabetic**

---

## 🛠️ Technologies Used

* Python
* Streamlit
* NumPy
* Pandas
* Scikit-Learn
* Matplotlib
* Joblib

---

## 📂 Project Structure

```
Diabetes-Prediction-App/
│── app.py
│── diabetes.pkl
│── scale.pkl
│── diabetes.csv
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation & Setup

### Step 1: Clone Repository

```bash
git clone https://github.com/your-username/diabetes-prediction-app.git
cd diabetes-prediction-app
```

### Step 2: Install Requirements

```bash
pip install -r requirements.txt
```

### Step 3: Run Application

```bash
streamlit run app.py
```

After running, the app will open automatically in your browser.

---

## 📊 How It Works

1. User enters medical details using sliders
2. Data is scaled using StandardScaler
3. Machine learning model predicts diabetes
4. Probability is calculated
5. Result is displayed with graphs

---

## 📷 Output

The application shows:

* Prediction Result
* Diabetes Probability
* Feature Distribution Graph
* Risk Level Graph

---

## 👍 Advantages

* Fast prediction
* User friendly
* Helpful for early detection
* No medical knowledge required

---

## ⚠️ Limitations

* Not a replacement for a doctor
* Depends on dataset accuracy
* Only works for trained parameters

---

## 🔮 Future Improvements

* User login system
* Database storage
* Doctor recommendation
* Mobile app version
* Multiple disease prediction

---

## 👨‍💻 Author

**Sourav Kumar Jha**
B.Tech CSE(AIML) Student


---

## 📚 References

* UCI Machine Learning Repository
* Scikit-Learn Documentation
* Streamlit Documentation

---

⭐ If you like this project, don't forget to star the repository!
