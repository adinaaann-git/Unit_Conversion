import streamlit as st

# Function to convert lengths
def convert_length(value, from_unit, to_unit):
    units = {
        "meters": 1,
        "kilometers": 1000,
        "centimeters": 0.01,
        "inches": 0.0254,
        "feet": 0.3048,
    }

    value_in_meters = value * units[from_unit]
    converted_value = value_in_meters / units[to_unit]
    return converted_value

# Function to convert temperatures
def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value

    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15

    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15

    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32

# Streamlit app
st.title("Unit Converter")

# Dropdown for selecting measurement type
measurement_type = st.selectbox("Select measurement type", ["Length", "Temperature"])

if measurement_type == "Length":
    # Dropdown for selecting units to convert from
    from_unit = st.selectbox("Select unit to convert from", ["meters", "kilometers", "centimeters", "inches", "feet"])

    # Text box for entering the quantity
    value = st.number_input(f"Enter quantity in {from_unit}:", min_value=0.0)

    # Dropdown for selecting units to convert to
    to_unit = st.selectbox("Select unit to convert to", ["meters", "kilometers", "centimeters", "inches", "feet"])

    # Convert button
    if st.button("Convert"):
        if value is not None:
            result = convert_length(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} is equal to {result} {to_unit}")

elif measurement_type == "Temperature":
    # Dropdown for selecting units to convert from
    from_unit = st.selectbox("Select unit to convert from", ["Celsius", "Fahrenheit", "Kelvin"])

    # Text box for entering the quantity
    value = st.number_input(f"Enter temperature in {from_unit}:", min_value=-273.15)  # Minimum temperature for Celsius

    # Dropdown for selecting units to convert to
    to_unit = st.selectbox("Select unit to convert to", ["Celsius", "Fahrenheit", "Kelvin"])

    # Convert button
    if st.button("Convert"):
        if value is not None:
            result = convert_temperature(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} is equal to {result} {to_unit}")

