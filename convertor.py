  # Project Name: Unit Converter
  #Build a google unit convertor using python and streamlit

import streamlit as st

st.markdown(
    """
    <style>
    body {
       background-color: #6dd5ed;
       color: white;
    }
    .stApp {
       background: linear-gradient(135deg, #bcbcbc, #cfe2f3);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 0px 30px rgba(0, 0, 0, 0.3);
    }
    h1 {
        text-align: center;
        font-size: 36px;
        color: white;
    }
    .stButton>button {
        background: linear-gradient(45deg, #0b5394, #351c75);
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 10px;
        transition: 0.3s;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.4);
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(45deg, #92fe9d, #00c9ff);
        color: black;
    }
    .result-box {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 15px;
        font-weight: bold;
        text-align: center;
        font-size: 24px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0 5px 15px rgba(0, 201, 255, 0.3);
    }
    .footer {
        text-align: center;
        font-size: 14px;
        color: black;
        margin-top: 50px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1>Unit Converter Using Python and Streamlit!</h1>", unsafe_allow_html=True)
st.write("Easily convert between different units")

# Sidebar
conversion_type = st.sidebar.selectbox("Choose Conversion Type", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter Value", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilometers", "Miles", "Feet", "Yard", "Inches", "Centimeters", "Millimeters"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilometers", "Miles", "Feet", "Yard", "Inches", "Centimeters", "Millimeters"])

if conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilograms", "Milligrams", "Grams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilograms", "Milligrams", "Grams", "Pounds", "Ounces"])

if conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

# Conversion Functions
def length_converter(value, from_unit, to_unit):
    length_units = {
        'Meters': 1,
        'Kilometers': 0.001,
        'Miles': 0.000621371,
        'Feet': 3.28084,
        'Yard': 1.09361,
        'Inches': 39.3701,
        'Centimeters': 100,
        'Millimeters': 1000
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        'Kilograms': 1,
        'Milligrams': 1_000_000,
        'Grams': 1000,
        'Pounds': 2.20462,
        'Ounces': 35.274
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return value * 9/5 + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    else:
        return value

# Conversion Button
if st.button("Convert"):
    if from_unit == to_unit:
        result = value
    else:
        result = {
            "Length": length_converter,
            "Weight": weight_converter,
            "Temperature": temperature_converter
        }[conversion_type](value, from_unit, to_unit)

    st.markdown(f"<div class='result-box'>{value} {from_unit} is equal to {result:.4f} {to_unit}</div>", unsafe_allow_html=True)
    st.markdown("<div class='footer'>Created by Subha Sajjad</div>", unsafe_allow_html=True)












