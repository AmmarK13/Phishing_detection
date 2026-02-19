# 🛡️ Phishing URL Detection using Machine Learning

## 📌 Project Overview

This project implements a **machine learning–based phishing URL detection system** using structured feature extraction from URLs.

Instead of relying on blacklist databases or signature-based detection, this system analyzes **URL lexical patterns and domain-level characteristics** to classify URLs as:

- ✅ Benign  
- ⚠️ Phishing  

The model is trained using engineered URL features and evaluated using robust metrics such as **ROC-AUC and Precision-Recall curves** to ensure strong performance even under class imbalance.

---

## 🎯 Why This Approach is Efficient

Traditional phishing detection systems often rely on:

- Blacklists (slow to update)
- Manual signature rules
- Deep inspection of page content (computationally heavy)

This project improves efficiency by:

- 🚀 Using lightweight lexical and statistical URL features  
- ⚡ Avoiding full webpage scraping  
- 📉 Reducing computational overhead  
- 🎯 Maintaining strong predictive performance  

Because it works directly on the URL string and domain features, predictions are:

- Faster  
- Scalable  
- Suitable for real-time systems  

---

## 🧠 Tech Stack

| Component | Technology |
|------------|------------|
| Programming Language | Python 3.x |
| Data Processing | Pandas, NumPy |
| Feature Engineering | Custom pipeline (`pipeline.py`) |
| Machine Learning | Scikit-learn (Random Forest) |
| Model Persistence | Joblib |
| Evaluation | ROC Curve, AUC, Precision-Recall |
| Version Control | Git |

---

## 📂 Project Structure

```
Phishing_Detection/
│
├── notebooks/
│   ├── chisquare_test.ipynb
│   ├── feature_extraction.ipynb
│   ├── feature_extraction.py
│   ├── pipeline.py
│   └── training.ipynb
│
├── data/
│   ├── raw_urls.csv
│   └── processed_dataset.csv
│
├── models/
│   └── random_forest.pkl
│
├── requirements.txt
└── README.md
```

---

# 📊 Dataset Construction

## 🔍 Feature Engineering Pipeline (`pipeline.py`)

The dataset is built using a custom feature engineering pipeline that extracts meaningful features directly from URL strings.

## 🔍 Feature Engineering Pipeline (`pipeline.py`)

The dataset is constructed using engineered lexical, structural, and statistical features extracted directly from URL strings.

The following features were implemented:

### 📏 Structural & Length-Based Features
- `url_length` → Total length of the URL  
- `domain_lenght` → Length of the domain name  
- `path_to_length_ratio` → Ratio of URL path length to total URL length  

---

### 🔢 Symbol & Character Count Features
- `num_slashes` → Number of `/` characters  
- `num_dots` → Number of `.` characters  
- `num_question_marks` → Number of `?` characters  
- `num_dashes` → Number of `-` characters  
- `num_at` → Number of `@` symbols  
- `suspicious_char_count` → Count of suspicious special characters  
- `special_char_ratio` → Ratio of special characters to total length  

---

### ⚠️ Suspicious Pattern Indicators
- `symbol_at_end` → Checks if suspicious symbol appears at end of URL  
- `http_in_middle` → Detects `http` appearing in the middle of URL  
- `has_ip` → Detects presence of raw IP address instead of domain  
- `has_unicode` → Detects obfuscated Unicode characters  
- `has_port` → Detects explicit port usage (e.g., `:8080`)  
- `special_keyword_count` → Counts phishing-related keywords (e.g., login, secure, update)  

---

### 🌐 Domain & Subdomain Features
- `num_subdomain` → Number of subdomains present  
- `digit_ratio_in_domain` → Ratio of numeric characters in domain  

---

### 📊 Statistical Feature
- `url_entropy` → Shannon entropy of URL string (measures randomness/obfuscation)

---

## 🛠️ How to Build the Dataset

### Step 1: Place Raw URLs

Create a CSV file:

`data/raw_urls.csv`

Format:

```csv
url,label
http://example.com,0
http://login-secure-bank.xyz,1
```

Where:
- `0 = Benign`
- `1 = Phishing`

---

### Step 2: Run Feature Pipeline

```bash
python pipeline.py -i input path -o output path
```

This will:

- Load raw URLs  
- Extract engineered features  
- Encode categorical variables  
- Output processed dataset  

Output file:

```
path/processed_dataset.csv
```

---

## ⚙️ Inside `pipeline.py`

The pipeline:

1. Cleans URL strings  
2. Extracts lexical and statistical features    
5. Scales numerical features (if enabled)  
6. Exports structured dataset ready for ML  

This modular design allows easy:

- Feature expansion  
- Model replacement  
- Integration into APIs  

---

# 🤖 Model Training

### Model Used
Random Forest Classifier

### Why Random Forest?

- Handles nonlinear patterns effectively  
- Robust to noisy features  
- Performs well on structured tabular data  
- Requires minimal hyperparameter tuning  
- Reduces overfitting via ensemble averaging  

---

# 📈 Model Evaluation

The model is evaluated using:

- ✅ Accuracy  
- ✅ Precision  
- ✅ Recall  
- ✅ F1 Score  
- ✅ ROC-AUC  
- ✅ Precision-Recall Curve  

### Why ROC-AUC?

Phishing datasets are often imbalanced. ROC-AUC measures model performance across all classification thresholds.

### Why Precision-Recall?

Precision-Recall is especially useful for rare-event detection like phishing, where false positives and false negatives have significant impact.

---

# 📊 Example Prediction Output

```json
{
  "url": "http://secure-update-paypal-login.xyz",
  "prediction": "Phishing",
  "probability": 0.94
}
```

---

# 🚀 Performance Highlights

- Strong discrimination between phishing and benign URLs  
- Low false positive rate  
- Efficient inference time  
- Lightweight feature extraction  
- Suitable for real-time applications  

Potential use cases:

- Browser extensions  
- Email spam filters  
- Enterprise web gateways  
- Security monitoring tools  

---

# 🔁 Reproducibility

To recreate this project:

```bash
git clone <repository-url>
cd Phishing_Detection
pip install -r requirements.txt
python pipeline.py
todo
```

---

# 📌 Future Improvements

- Add WHOIS-based domain features  
- Incorporate DNS resolution features  
- Compare with XGBoost / LightGBM  
- Experiment with deep learning models  
- Add adversarial robustness evaluation  
- Implement API for real-time inference  

---

# ☁️ Deployment

## 🚧 To Do

---

# 📜 License

This project is developed for educational and research purposes in cybersecurity and machine learning.
