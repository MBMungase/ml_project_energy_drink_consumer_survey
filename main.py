import streamlit as st
#from prediction_helper import predict_price_range
from prediction_helper import predict

# Allign dropwon and input boxes
# st.set_page_config(layout="wide")
#command -->  streamlit run ./main.py
st.set_page_config(
    page_title="Energy Drink Consumer Survey Price Prediction",
    layout="wide"
)
# Set the page configuration and title
st.markdown(
    "<h1 style='text-align: center;'>Energy Drink Consumer Survey : Price Prediction</h1>",
    unsafe_allow_html=True
)

row1 = st.columns(4)
row2 = st.columns(4)
row3 = st.columns(4)
row4 = st.columns(4)

with row1[0]:
    # age = st.number_input("Age", min_value=18,max_value=70,step=1)
    age = st.number_input('Age', min_value=18, step=1, max_value=100, value=18)
with row1[1]:
    gender = st.selectbox("Gender", ["Male", "Female"])
    #row1[1] = 1 if gender == "Male" else 0
with row1[2]:
    zone = st.selectbox("Zone", ['Urban', 'Metro', 'Rural', 'Semi-Urban'],width="stretch")
with row1[3]:
    occupation = st.selectbox("Occupation",['Working Professional', 'Student', 'Entrepreneur', 'Retired'])


with row2[0]:
    income_levels = st.selectbox("Income Levels",['<10L', '> 35L', '16L - 25L', 'Not Reported', '10L - 15L', '26L - 35L'])
with row2[1]:
    consume_frequency_weekly= st.selectbox("Consume Frequency(weekly)",['3-4 times', '5-7 times', '0-2 times'],width="stretch")
with row2[2]:
    current_brand = st.selectbox("Current Brand",['Newcomer', 'Established'])
with row2[3]:
    preferable_consumption_size = st.selectbox("Preferable Consumption Size",['Medium (500 ml)', 'Large (1 L)', 'Small (250 ml)'])

with row3[0]:
    awareness_of_other_brands = st.selectbox("Awareness Of Other Brands",['0 to 1', '2 to 4', 'above 4'])
with row3[1]:
    reasons_for_choosing_brands = st.selectbox("Reasons For Choosing Brands",['Price', 'Quality', 'Availability', 'Brand Reputation'])
with row3[2]:
    flavor_preference = st.selectbox("Flavor Preference",['Traditional', 'Exotic'])
with row3[3]:
    purchase_channel = st.selectbox("Purchase Channel",['Online', 'Retail Store'])

with row4[0]:
    packaging_preference = st.selectbox("Packaging Preference",['Simple', 'Premium', 'Eco-Friendly'])
with row4[1]:
    health_concerns = st.selectbox("Health Concerns",['Low (Not very concerned)','Medium (Moderately health-conscious)','High (Very health-conscious)'])
with row4[2]:
    typical_consumption_situations = st.selectbox("Typical Consumption Situations",['Active (eg. Sports, gym)', 'Social (eg. Parties)', 'Casual (eg. At home)'])

# Button to calculate price range
if st.button("Calculate Price Range"):
   print("First - Calling predict method")
   price = predict(age,gender, zone, occupation, income_levels, consume_frequency_weekly, current_brand,
                   preferable_consumption_size, awareness_of_other_brands, reasons_for_choosing_brands, flavor_preference,
                   purchase_channel, packaging_preference, health_concerns, typical_consumption_situations)

   st.success(f"Predicted Price Range: {price}")
