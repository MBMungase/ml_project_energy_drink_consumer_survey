import joblib
import numpy as np
import pandas as pd

# Path to the saved model and its components
MODEL_PATH = 'artifacts/model_young.joblib'


# Load the model and its components
model_data = joblib.load(MODEL_PATH)
model = model_data['model']
#print('Model', model)
features = model_data['features']
label_encoders = model_data["label_encoders"]


def prepare_input(age,gender,zone,occupation,income_levels,consume_frequency_weekly,current_brand,
                     preferable_consumption_size,awareness_of_other_brands,reasons_for_choosing_brands,flavor_preference,
                     purchase_channel,packaging_preference,health_concerns,typical_consumption_situations):
    #Create a dictionary with input values and dummy values for missing features
   # Create Age Group
   # Same logic as training

   if 18 <= age <= 25:
    age_group = "18-25"
   elif 26 <= age <= 35:
    age_group = "26-35"
   elif 36 <= age <= 45:
    age_group = "36-45"
   elif 46 <= age <= 55:
    age_group = "46-55"
   elif 56 <= age <= 70:
    age_group = "56-70"
   else:
    age_group = "70+"

   input_data = {
       # Label encoded columns
       "age_group": age_group,
       "income_levels": income_levels,
       "health_concerns": health_concerns,
       "consume_frequency(weekly)": consume_frequency_weekly,
       "preferable_consumption_size": preferable_consumption_size,
       # Numerical columns
       "cf_ab_score": 1,  # Dummy value
       "zas_score": 1,  # Dummy value
       "bsi": 1,  # Dummy value
       # Gender
       "gender_M": 1 if gender == "Male" else 0,
       # Zone
       "zone_Rural": 1 if zone == "Rural" else 0,
       "zone_Semi-Urban": 1 if zone == "Semi-Urban" else 0,
       "zone_Urban": 1 if zone == "Urban" else 0,
       # Occupation
       "occupation_Retired": 1 if occupation == "Retired" else 0,
       "occupation_Student": 1 if occupation == "Student" else 0,
       "occupation_Working Professional": 1 if occupation == "Working Professional" else 0,
       # Current brand
       "current_brand_Newcomer": 1 if current_brand == "Newcomer" else 0,
       # Awareness
       "awareness_of_other_brands_2 to 4": 1 if awareness_of_other_brands == "2 to 4" else 0,
       "awareness_of_other_brands_above 4": 1 if awareness_of_other_brands == "above 4" else 0,
       # Reasons
       "reasons_for_choosing_brands_Brand Reputation": 1 if reasons_for_choosing_brands == "Brand Reputation" else 0,
       "reasons_for_choosing_brands_Price": 1 if reasons_for_choosing_brands == "Price" else 0,
       "reasons_for_choosing_brands_Quality": 1 if reasons_for_choosing_brands == "Quality" else 0,
       # Flavor
       "flavor_preference_Traditional": 1 if flavor_preference == "Traditional" else 0,
       # Purchase channel
       "purchase_channel_Retail Store": 1 if purchase_channel == "Retail Store" else 0,
       # Consumption situation
       "typical_consumption_situations_Casual (eg. At home)": 1 if typical_consumption_situations == "Casual (eg. At home)" else 0,
       "typical_consumption_situations_Social (eg. Parties)": 1 if typical_consumption_situations == "Social (eg. Parties)" else 0,
        # Packaging
        "packaging_preference_Premium": 1 if packaging_preference == "Premium" else 0,
        "packaging_preference_Simple":  1 if packaging_preference == "Simple" else 0
   }

   # Ensure all columns for features
   df = pd.DataFrame([input_data])
   # print("Columns before encoding:")
   # print(df.columns)

   # Apply the SAME LabelEncoders used during training
   categorical_cols = [
        'income_levels',
        'consume_frequency(weekly)',
        'preferable_consumption_size',
        'health_concerns',
        'age_group'
   ]

   for col in categorical_cols:
        df[col] = label_encoders[col].transform(df[col])

   # Make input columns exactly same as model training
   df = df.reindex(columns=features, fill_value=0)

   # Ensure all columns are numeric
   df = df.astype(int)

   return df

def predict(age,gender,zone,occupation,income_levels,consume_frequency_weekly,current_brand,
                     preferable_consumption_size,awareness_of_other_brands,reasons_for_choosing_brands,flavor_preference,
                     purchase_channel,packaging_preference,health_concerns,typical_consumption_situations):
    # Prepare input data
    # print('Actual Age',age)
    input_df= prepare_input(age, gender, zone, occupation, income_levels, consume_frequency_weekly, current_brand,
                  preferable_consumption_size, awareness_of_other_brands, reasons_for_choosing_brands,
                  flavor_preference,purchase_channel, packaging_preference, health_concerns, typical_consumption_situations)
    print("INPUT DATA TYPES:")
    print(input_df.dtypes)
    print("\nINPUT DATA:")
    print(input_df)
    print("\nMODEL FEATURES:")
    print(features)
    # Model prediction
    prediction = model.predict(input_df)

    # Convert encoded price_range back to original value
    price = label_encoders['price_range'].inverse_transform(
        prediction.astype(int)
    )

    return price[0]