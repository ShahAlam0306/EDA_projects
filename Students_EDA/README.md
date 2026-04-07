# 📊 AI Student Life Analysis (EDA Project)

## 📌 Project Overview

This project performs **Exploratory Data Analysis (EDA)** on a dataset of students using AI tools to understand:

* How students use AI tools
* Whether AI usage impacts academic performance
* Patterns in satisfaction and behavior

The dataset contains **400 student records** with demographic, behavioral, and outcome variables.

---

## 🎯 Objectives

* Analyze distribution of AI usage among students
* Identify relationship between AI usage and academic performance
* Understand purpose of AI usage (learning, coding, homework, etc.)
* Evaluate satisfaction levels with AI tools
* Validate findings using statistical testing

---

## 📂 Dataset Information

### Features:

* `Student_ID`
* `Age`
* `Gender`
* `Education_Level`
* `City`
* `AI_Tool_Used`
* `Daily_Usage_Hours`
* `Purpose`
* `Impact_on_Grades`
* `Satisfaction_Level`

---

## 🧪 Analysis Performed

### 🔹 Data Cleaning

* Checked for missing values → none found
* Removed duplicates → dataset clean

### 🔹 Univariate Analysis

* Distribution of categorical variables
* Percentage breakdown of:

  * Gender
  * Education level
  * AI tools used
  * Purpose
  * Grade impact
  * Satisfaction

### 🔹 Bivariate Analysis

* Gender vs AI usage
* Gender vs grade impact
* Gender vs satisfaction
* AI usage vs grade impact (boxplot)

### 🔹 Multivariate Analysis

* Purpose × Impact on Grades (heatmap of average usage)
* Education Level × AI Tool usage (pivot table)

### 🔹 Statistical Testing

* Applied **Chi-Square Test of Independence**
* Tested relationships between:

  * AI Tool vs Grade Impact
  * Purpose vs Grade Impact
  * Education vs Satisfaction
  * Gender vs Satisfaction

---

## 📊 Key Findings

* AI usage **does not significantly impact academic performance** (Chi-square p > 0.05)
* Students primarily use AI for **task-based activities** like coding and homework
* AI tool usage is **concentrated among Gemini and ChatGPT**
* Satisfaction levels are **mixed**, with no strong dominance
* No significant differences found across **gender or education level**

---

## 📈 Statistical Insight

All Chi-square tests resulted in:

> ❌ No statistically significant relationships

👉 This indicates:

* AI usage patterns are **independent of performance and satisfaction**
* Other external factors may influence academic outcomes

---

## 💡 Business Insights

* Heavy AI usage does **not guarantee better academic performance**
* Students rely on AI more for **completion of tasks rather than learning**
* Over-dependence on limited tools may restrict learning diversity

---

## 🚀 Recommendations

* Encourage **conceptual learning** instead of shortcut-based usage
* Promote **balanced AI usage**
* Provide training on **effective use of AI tools**
* Introduce **guidelines for academic AI usage**

---

## 🛠️ Tech Stack

* Python 🐍
* Pandas
* NumPy
* Matplotlib
* Seaborn
* SciPy

---

## 📌 Conclusion

This analysis highlights that while AI tools are widely adopted by students, their impact on academic performance is **not statistically significant**. The findings emphasize the importance of **how AI is used**, rather than just usage frequency.

---

## 📎 Author

**Shahalam (Rayeen Shakib)**
Aspiring Data Analyst

---
