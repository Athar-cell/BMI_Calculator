import streamlit as st

# App Title with style
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>💪 BMI Calculator 🚀</h1>", unsafe_allow_html=True)

# Input Section
st.subheader("📥 Enter Your Details")
weight = st.number_input("⚖️ Enter your weight (kg):", min_value=1.0, format="%.2f")
height_unit = st.radio("📏 Select your height unit:", ['Centimeters', 'Meters', 'Feet'])
height = st.number_input(f"📐 Enter your height ({height_unit.lower()}):", min_value=0.0, format="%.2f")

# Funny messages + emojis for BMI categories
def get_funny_message(bmi):
    if bmi < 16:
        return "🥦 Too skinny! Even noodles got more mass than you 🍜"
    elif 16 <= bmi < 18.5:
        return "🦴 Underweight — eat some parantha, bro! 🫓"
    elif 18.5 <= bmi < 25:
        return "✅ Perfect! You're in hero shape 😎"
    elif 25 <= bmi < 30:
        return "🍔 Overweight — maybe swap burger with bhindi 🥗"
    else:
        return "🍩 Extremely Overweight — Gym calling 📞💪"

# BMI Calculation
if st.button("✨ Calculate BMI ✨"):
    # Convert height to meters
    if height_unit == 'Centimeters':
        height_m = height / 100
    elif height_unit == 'Feet':
        height_m = height * 0.3048
    else:
        height_m = height

    if height_m <= 0:
        st.error("⚠️ Height must be greater than zero.")
    else:
        bmi = weight / (height_m ** 2)

        # Display BMI with style
        st.markdown(f"<h2 style='color:#2196F3;'>📊 Your BMI is: {bmi:.2f}</h2>", unsafe_allow_html=True)

        # Category + emoji + funny text
        message = get_funny_message(bmi)

        if bmi < 16:
            st.error(message)
        elif 16 <= bmi < 18.5:
            st.warning(message)
        elif 18.5 <= bmi < 25:
            st.success(message)
        elif 25 <= bmi < 30:
            st.warning(message)
        else:
            st.error(message)

# BMI Categories Table
st.markdown("""
---
### 📌 BMI Categories (WHO Standard)
- <16 : 🥦 Extremely Underweight  
- 16–18.5 : 🦴 Underweight  
- 18.5–24.9 : ✅ Healthy  
- 25–29.9 : 🍔 Overweight  
- ≥30 : 🍩 Extremely Overweight  
""")
