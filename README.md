# ml_project_energy_drink_consumer_survey
This project analyzes consumer survey data to understand energy drink consumption behavior, brand preferences, purchasing patterns, health concerns, and price sensitivity

The target variable is **`price_range`**, which represents the price category of the energy drink typically purchased by the respondent. :chatgpt-content-reference{index="1"} :chatgpt-content-reference{index="2"}

The project involves data cleaning, feature engineering, categorical encoding, model training, model comparison, and selection of the best-performing machine learning model. :chatgpt-content-reference{index="3"} :chatgpt-content-reference{index="4"}
# 2. Task List

- **Data Understanding:** Understand the business problem, dataset, columns, data types, and target variable.

- **Data Cleaning:**
  - Remove duplicate records.
  - Identify and handle age outliers.
  - Handle missing values.
  - Replace missing income values with **"Not Reported"**.
  - Handle missing values in consumption frequency and purchase channel.
  - Correct spelling and formatting inconsistencies in categorical data. :chatgpt-content-reference{index="5"}

- **Feature Engineering:**
  - Create `age_group`.
  - Create **CF-AB Score** (`cf_ab_score`) using consumption frequency and brand awareness.
  - Create **Zone Affluence Score** (`zas_score`) using zone and income level.
  - Create **Brand Switching Indicator** (`bsi`). :chatgpt-content-reference{index="6"} :chatgpt-content-reference{index="7"}

- **Logical Outlier Removal:**
  - Identify logically inconsistent records, such as students appearing in older age groups.
  - Remove records where the occupation and age group do not make logical sense. :chatgpt-content-reference{index="8"}

- **Feature and Target Preparation:**
  - Create feature matrix `X`.
  - Create target variable `y`.
  - Remove `respondent_id` and `price_range` from the feature set. :chatgpt-content-reference{index="9"}

- **Data Splitting:**
  - Split the data into **75% training** and **25% testing**.
  - Use `random_state = 42`. :chatgpt-content-reference{index="10"}

- **Feature Encoding:**
  - Apply Label Encoding to selected categorical features.
  - Apply One-Hot Encoding to the remaining categorical features.
  - Label encode the target variable `price_range`. :chatgpt-content-reference{index="11"}

- **Model Building:**
  - Gaussian Naive Bayes
  - Logistic Regression
  - Support Vector Machine
  - Random Forest
  - XGBoost
  - LightGBM :chatgpt-content-reference{index="12"}

- **Model Evaluation:**
  - Calculate accuracy for each model.
  - Generate classification reports.
  - Compare model performance. :chatgpt-content-reference{index="13"}

- **Model Selection:**
  - Select the best-performing model for further use and deployment. :chatgpt-content-reference{index="14"}


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

