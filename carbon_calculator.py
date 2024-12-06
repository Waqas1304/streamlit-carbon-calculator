import streamlit as st

# Set wide layout and page name at the beginning
st.set_page_config(layout="wide", page_title="Personal Carbon Calculator")

EMISSION_FACTORS = {
    "France": {
        "Transportation": 0.14,  # kgCO2/km
        "Bus": 0.05,  # kgCO2/km
        "Electricity": 0.060,  # kgCO2/kWh
        "Diet": 1.25,  # kgCO2/meal
        "Waste": 0.1,  # kgCO2/kg
        "Smoking": 0.01,  # kgCO2 per cigarette 
        "Plants": -22 #kg/tree/year
    },
    "India": {
        "Transportation": 0.14,  # kgCO2/km
        "Bus": 0.05,  # kgCO2/km
        "Electricity": 0.82,  # kgCO2/kWh
        "Diet": 1.25,  # kgCO2/meal
        "Waste": 0.1,  # kgCO2/kg
        "Smoking": 0.01,  # kgCO2 per cigarette 
        "Plants": -22 #kg/tree
    },
    "Pakistan": {
        "Transportation": 0.14,  # kgCO2/km
        "Bus": 0.05,  # kgCO2/km
        "Electricity": 0.462,  # kgCO2/kWh
        "Diet": 1.25,  # kgCO2/meal
        "Waste": 0.1, # kgCO2/kg
        "Smoking": 0.01,  # kgCO2 per cigarette 
        "Plants": -22 #kg/tree
    },
    "Italy": {
        "Transportation": 0.14,  # kgCO2/km
        "Bus": 0.05,  # kgCO2/km
        "Electricity": 0.241,  # kgCO2/kWh
        "Diet": 1.25,  # kgCO2/meal
        "Waste": 0.1,  # kgCO2/kg
        "Smoking": 0.01 , # kgCO2 per cigarette 
        "Plants": -22 #kg/tree
    },
    "Hungary": {
        "Transportation": 0.14,  # kgCO2/km
        "Bus": 0.05,  # kgCO2/km
        "Electricity": 0.354,  # kgCO2/kWh
        "Diet": 1.25,  # kgCO2/meal
        "Waste": 0.1,  # kgCO2/kg
        "Smoking": 0.01,  # kgCO2 per cigarette 
        "Plants": -22 #kg/tree
    }
}

# Streamlit app code
st.title("Carbon Calculator App ⚠️")

# User inputs
st.subheader("🌍 Your Country")
country = st.selectbox("Select", ["India", "Pakistan", "France", "Italy", "Hungary"])

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🚗 Daily commute distance (in km)")
    distance = st.slider("Distance", 0.0, 100.0, key="Car_distance_input")

    st.subheader("💡 Monthly electricity consumption (in kWh)")
    electricity = st.slider("Electricity", 0.0, 1000.0, key="electricity_input")

    st.subheader("💡 Number of Trees Planted (per month)")
    Plants = st.number_input("Plants", 0, key="Plants_input")

with col2:
    st.subheader("🍽️ Waste generated per week (in kg)")
    waste = st.slider("Waste", 0.0, 100.0, key="waste_input")

    st.subheader("🍽️ Number of meals per day")
    meals = st.number_input("Meals", 0, key="meals_input")
with col3:
    st.subheader ("🚌 Daily commute distance (in km)")
    Bus_Travel = st.slider("Distance", 0.0, 100.0, key="Bus_distance_input")
    
    st.subheader ("🚬 Number of cigarette per day ")
    cigarette = st.number_input("Cigarette", 0, key="cigarette_input")

# Normalize inputs
if distance > 0:
    distance = distance * 365  # Convert daily distance to yearly
if electricity > 0:
    electricity = electricity * 12  # Convert monthly electricity to yearly
if meals > 0:
    meals = meals * 365  # Convert daily meals to yearly
if waste > 0:
    waste = waste * 52  # Convert weekly waste to yearly
if Bus_Travel > 0:
    Bus_Travel = Bus_Travel * 365  # Convert weekly waste to yearly
if cigarette > 0:
    cigarette = cigarette * 365  # Convert weekly waste to yearly
if Plants > 0:
    Plants = Plants   # Convert monthly waste to yearly


# Calculate carbon emissions
transportation_emissions = EMISSION_FACTORS[country]["Transportation"] * distance
electricity_emissions = EMISSION_FACTORS[country]["Electricity"] * electricity
diet_emissions = EMISSION_FACTORS[country]["Diet"] * meals
waste_emissions = EMISSION_FACTORS[country]["Waste"] * waste
cigarette_emissions = EMISSION_FACTORS[country]["Smoking"] * cigarette
Bus_Emissions = EMISSION_FACTORS[country]["Bus"] * Bus_Travel
C02_Saving = EMISSION_FACTORS[country]["Plants"] * Plants


# Convert emissions to tonnes and round off to 2 decimal points
transportation_emissions = round(transportation_emissions / 1000, 2)
electricity_emissions = round(electricity_emissions / 1000, 2)
diet_emissions = round(diet_emissions / 1000, 2)
waste_emissions = round(waste_emissions / 1000, 2)
cigarette_emissions = round(cigarette_emissions/ 1000, 2)
Bus_emissions = round(waste_emissions / 1000, 2)
CO2_Saving = round(C02_Saving / 1000, 2)


# Calculate total emissions
# Correcting the total emissions calculation and ensuring proper indentation
# Calculate total emissions from various categories
# Calculate total emissions from various categories
# Calculate total emissions from various categories
# Initial total emissions calculation
total_emissions = round(
    transportation_emissions + electricity_emissions + diet_emissions + waste_emissions + Bus_Emissions + cigarette_emissions + C02_Saving, 2
)

# When the button is clicked, we show the initial results
if st.button("Calculate CO2 Emissions"):
    # Display results
    st.header("Your Current Carbon Footprint")

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Carbon Emissions by Category")
        st.info(f"🚗 Transportation: {transportation_emissions} tonnes CO2 per year")
        st.info(f"💡 Electricity: {electricity_emissions} tonnes CO2 per year")
        st.info(f"🍽️ Diet: {diet_emissions} tonnes CO2 per year")
        st.info(f"🗑️ Waste: {waste_emissions} tonnes CO2 per year")
        st.info(f"🚌 Bus: {Bus_Emissions} tonnes CO2 per year")
        st.info(f"🚬 Cigarettes: {cigarette_emissions} tonnes CO2 per year")
       
    with col4:
        st.subheader("Total Carbon Footprint")
        st.success(f"🌍 Your total carbon footprint is: {total_emissions} tonnes CO2 per year")
        st.info(f"🌲 CO2 Saved: {CO2_Saving} tonnes CO2 per year")

   
    





        
       