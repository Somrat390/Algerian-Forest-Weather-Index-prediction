# 🌲 Algerian Forest Fire Weather Index Prediction

This project predicts the **Fire Weather Index (FWI)** for the Algerian Forest dataset using a **Ridge Regression Model**.  
It is deployed on **Render** as a Flask web application.

---

## 📊 Dataset

- **Source:** [Kaggle - Algerian Forest Fires Dataset](https://www.kaggle.com/datasets/abdelghaniaaba/algerian-forest-fires-dataset)
- **Features include:**
  - 🌡️ Temperature (°C)
  - 💧 Relative Humidity (%)
  - 🌬️ Wind Speed (km/h)
  - 🌧️ Rain (mm)
  - 🔥 Fire Weather Codes → FFMC, DMC, ISI
  - 🏷️ Classes (0 = No Fire, 1 = Fire)
  - 🗺️ Region (Bejaia / Sidi-Bel Abbes)

---

## ⚙️ Tech Stack

- **Python 3**
- **Flask** (Web Framework)
- **Scikit-Learn** (ML Model)
- **NumPy, Pandas** (Data Processing)
- **Render** (Deployment)

---

## 🚀 Deployment

The project is deployed on **Render** and can be accessed here:  
🔗 **Live Demo:** https://algerian-forest-weather-index-prediction.onrender.com/predict
---

## 🖥️ Local Setup

Follow these steps to run the project locally:

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/Algerian-Forest-Weather-Index-prediction.git
cd Algerian-Forest-Weather-Index-prediction
````

### 2️⃣ Create Virtual Environment & Install Dependencies

```bash
python -m venv venv
source venv/bin/activate    # For Mac/Linux
venv\Scripts\activate       # For Windows

pip install -r requirements.txt
```

### 3️⃣ Run the Flask App

```bash
python application.py
```

Your app will start at **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

---

## 📌 Example Prediction

**Input Example:**

| Feature     | Value      |
| ----------- | ---------- |
| Temperature | 25°C       |
| RH          | 40%        |
| Ws          | 15 km/h    |
| Rain        | 0 mm       |
| FFMC        | 85         |
| DMC         | 120        |
| ISI         | 10         |
| Classes     | 1 (Fire)   |
| Region      | 1 (Bejaia) |

**Output Example:**
🔥 **Predicted Fire Weather Index:** `42.31`

---

## 📂 Project Structure

```
├── Model/
│   ├── ridge.pkl
│   ├── scaler.pkl
├── templates/
│   ├── index.html
│   ├── home.html
├── static/
│   ├── style.css
├── application.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🧠 Notes

* Make sure `requirements.txt` is updated before deploying:

  ```bash
  pip freeze > requirements.txt
  ```
* Render uses **Gunicorn** to run Flask apps. Your `Start Command` in Render should be:

  ```
  gunicorn app:app
  ```

---

## ⭐ Contribute

If you like this project, consider **starring** ⭐ the repo and contributing with issues or pull requests!

```

---

This is now fully tailored for **Flask + Render** and includes:
✅ Deployment link  
✅ Local setup steps  
✅ Example prediction  
✅ Project structure  
✅ Best practices  

---

Do you want me to also generate a **sample `.gitignore`** (so that venv, __pycache__, and model.pkl files aren’t accidentally pushed)?  
That will make your repo cleaner and professional.
```


# UI of this Project
<img width="794" height="630" alt="image" src="https://github.com/user-attachments/assets/732fbe5d-ae0c-4366-938e-2b8a2a25dff4" />
<img width="528" height="617" alt="image" src="https://github.com/user-attachments/assets/76b4b833-ae9e-445f-b7fd-6e9d9c3ca654" />


