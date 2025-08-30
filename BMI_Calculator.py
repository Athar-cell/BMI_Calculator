import streamlit as st

# Title of the app
st.title("BMI Calculator")

# Input: Weight in kilograms
weight = st.number_input("Enter your weight (kg):", min_value=1.0, format="%.2f")

# Input: Height format selection
height_unit = st.radio("Select your height unit:", ['Centimeters', 'Meters', 'Feet'])

# Input: Height value based on selected unit
height = st.number_input(f"Enter your height ({height_unit.lower()}):", min_value=0.0, format="%.2f")

# Calculate BMI when button is pressed
if st.button("Calculate BMI"):
    # Convert height to meters based on selected unit
    if height_unit == 'Centimeters':
        height_m = height / 100
    elif height_unit == 'Feet':
        height_m = height * 0.3048   # precise conversion
    else:
        height_m = height

    # Prevent division by zero
    if height_m <= 0:
        st.error("Height must be greater than zero.")
    else:
        bmi = weight / (height_m ** 2)
        st.success(f"Your BMI is {bmi:.2f}")

        # BMI interpretation
        if bmi < 16:
            st.error("You are Extremely Underweight")
        elif 16 <= bmi < 18.5:
            st.warning("You are Underweight")
        elif 18.5 <= bmi < 25:
            st.success("You are Healthy")
        elif 25 <= bmi < 30:
            st.warning("You are Overweight")
        else:
            st.error("You are Extremely Overweight")

# Optional: Show BMI reference table
st.markdown("""
**BMI Categories (WHO Standard):**
- <16 : Extremely Underweight  
- 16–18.5 : Underweight  
- 18.5–24.9 : Healthy  
- 25–29.9 : Overweight  
- ≥30 : Extremely Overweight  
""")
