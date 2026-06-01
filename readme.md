# Medical Insurance Cost Analysis & Feature Engineering

## Project Overview

This project performs Exploratory Data Analysis (EDA), Feature Engineering, and Statistical Analysis on a Medical Insurance dataset to identify the key factors influencing insurance charges.

The objective is to uncover business insights, understand customer risk profiles, and prepare the dataset for predictive modeling.

---

## Business Problem

Insurance companies need to understand the factors that drive medical costs in order to:

* Improve premium pricing strategies
* Identify high-risk customers
* Optimize risk assessment processes
* Design preventive healthcare programs
* Improve profitability while maintaining customer satisfaction

---

## Dataset Information

The dataset contains customer demographic, lifestyle, and insurance-related information:

| Feature  | Description               |
| -------- | ------------------------- |
| age      | Age of policyholder       |
| sex      | Gender of customer        |
| bmi      | Body Mass Index           |
| children | Number of dependents      |
| smoker   | Smoking status            |
| region   | Residential region        |
| charges  | Medical insurance charges |

---

## Project Workflow

### 1. Data Exploration

* Dataset inspection
* Data types analysis
* Missing value check
* Duplicate analysis
* Descriptive statistics

### 2. Data Cleaning

* Duplicate removal
* Data validation
* Data consistency checks

### 3. Exploratory Data Analysis

* Univariate Analysis
* Bivariate Analysis
* Correlation Analysis
* Distribution Analysis
* Outlier Detection

### 4. Feature Engineering

* Label Encoding
* One-Hot Encoding
* BMI Category Creation
* Feature Scaling

### 5. Statistical Analysis

* Pearson Correlation Test
* Chi-Square Test of Independence
* Feature Importance Evaluation

---

## Tools & Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* SciPy
* Jupyter Notebook

---

## Key Business Insights

### Smoking is the strongest predictor of insurance charges

Smokers incur significantly higher medical expenses compared to non-smokers, making smoking status the most influential risk factor.

### Age positively impacts insurance costs

Medical expenses generally increase with age, resulting in higher insurance charges for older customers.

### BMI influences insurance expenses

Overweight and obese individuals tend to generate higher healthcare costs compared to customers with normal BMI.

### Regional impact is limited

Insurance charges show relatively small differences across geographic regions.

### High-risk customer segment identified

Older smokers with high BMI represent the highest-cost customer group and contribute disproportionately to insurance expenses.

---

## Business Recommendations

* Implement wellness incentive programs for non-smokers.
* Promote preventive healthcare initiatives targeting obesity.
* Develop risk-based premium pricing strategies.
* Create customer segmentation models for better risk management.
* Invest in predictive analytics for early identification of high-cost customers.

---

## Project Structure

```text
Medical_Insurance_Analysis/
│
├── Analysis.ipynb
├── insurance.csv
├── README.md
│
├── images/
│   ├── correlation_heatmap.png
│   ├── distribution_plots.png
│   └── boxplots.png
│
└── requirements.txt
```

---

## Statistical Findings

### Pearson Correlation

Used to measure the relationship between numerical features and insurance charges.

### Chi-Square Test

Used to evaluate the relationship between categorical variables and charge categories.

---

## Future Improvements

* Linear Regression Model
* Random Forest Regressor
* XGBoost Regressor
* Hyperparameter Tuning
* Model Deployment using Streamlit
* Interactive Power BI Dashboard

---

## Conclusion

The analysis reveals that smoking status, age, and BMI are the most influential factors affecting medical insurance charges. Smoking emerged as the strongest predictor of higher costs, followed by age and BMI. These findings can support more effective risk assessment, premium pricing, and healthcare intervention strategies.

---

## Author

**Shahalam Rayeen**

* GitHub: https://github.com/ShahAlam0306
* Portfolio: https://shahalam-portfolio.vercel.app/
* LinkedIn: https://www.linkedin.com/in/shahalam-rayeen-104435319/
