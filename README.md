# ml_project_energy_drink_consumer_survey
This project analyzes consumer survey data to understand energy drink consumption behavior, brand preferences, purchasing patterns, health concerns, and price sensitivity

The target variable is **`price_range`**, which represents the price category of the energy drink typically purchased by the respondent.

The project involves data cleaning, feature engineering, categorical encoding, model training, model comparison, and selection of the best-performing machine learning model.
# 2. Task List

- **Data Understanding:** Understand the business problem, dataset, columns, data types, and target variable.

- **Data Cleaning:**
  - Remove duplicate records.
  - Identify and handle age outliers.
  - Handle missing values.
  - Replace missing income values with **"Not Reported"**.
  - Handle missing values in consumption frequency and purchase channel.
  - Correct spelling and formatting inconsistencies in categorical data.

- **Feature Engineering:**
  - Create `age_group`.
  - Create **CF-AB Score** (`cf_ab_score`) using consumption frequency and brand awareness.
  - Create **Zone Affluence Score** (`zas_score`) using zone and income level.
  - Create **Brand Switching Indicator** (`bsi`).

- **Logical Outlier Removal:**
  - Identify logically inconsistent records, such as students appearing in older age groups.
  - Remove records where the occupation and age group do not make logical sense.

- **Feature and Target Preparation:**
  - Create feature matrix `X`.
  - Create target variable `y`.
  - Remove `respondent_id` and `price_range` from the feature set. 

- **Data Splitting:**
  - Split the data into **75% training** and **25% testing**.
  - Use `random_state = 42`.

- **Feature Encoding:**
  - Apply Label Encoding to selected categorical features.
  - Apply One-Hot Encoding to the remaining categorical features.
  - Label encode the target variable `price_range`.
- **Model Building:**
  - Gaussian Naive Bayes
  - Logistic Regression
  - Support Vector Machine
  - Random Forest
  - XGBoost
  - LightGBM

- **Model Evaluation:**
  - Calculate accuracy for each model.
  - Generate classification reports.
  - Compare model performance.

- **Model Selection:**
  - Select the best-performing model for further use and deployment.


# 3. Overall Learning

Through this project, I learned how to take a **real-world survey dataset from raw data to a machine learning prediction solution**.

The major learnings include:

- Understanding a **business problem** and converting it into a machine learning problem.
- Performing **data exploration and data cleaning**.
- Handling **missing values, duplicates, spelling inconsistencies, and logical outliers**.
- Creating meaningful features through **feature engineering**.
- Understanding and implementing **Label Encoding and One-Hot Encoding**.
- Creating business-oriented features such as **CF-AB Score, Zone Affluence Score, and Brand Switching Indicator**.
- Splitting data into training and testing datasets correctly.
- Training and comparing multiple **classification algorithms**.
- Evaluating models using **accuracy and classification reports**.
- Selecting the best-performing model based on model comparison.
- Understanding the complete **end-to-end machine learning workflow**, from data preparation to prediction and deployment.

