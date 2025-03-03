import streamlit as st

# Define conversion functions
def convert_length(value, from_unit, to_unit):
    length_conversions = {
        "meter": 1,
        "kilometer": 0.001,
        "centimeter": 100,
        "millimeter": 1000,
        "inch": 39.3701,
        "foot": 3.28084,
        "yard": 1.09361,
        "mile": 0.000621371,
    }
    return value * (length_conversions[to_unit] / length_conversions[from_unit])

def convert_weight(value, from_unit, to_unit):
    weight_conversions = {
        "kilogram": 1,
        "gram": 1000,
        "milligram": 1e6,
        "pound": 2.20462,
        "ounce": 35.274,
    }
    return value * (weight_conversions[to_unit] / weight_conversions[from_unit])

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "celsius":
        if to_unit == "fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "kelvin":
            return value + 273.15
    elif from_unit == "fahrenheit":
        if to_unit == "celsius":
            return (value - 32) * 5/9
        elif to_unit == "kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "kelvin":
        if to_unit == "celsius":
            return value - 273.15
        elif to_unit == "fahrenheit":
            return (value - 273.15) * 9/5 + 32
    return value

def convert_area(value, from_unit, to_unit):
    area_conversions = {
        "square meter": 1,
        "square kilometer": 1e-6,
        "square centimeter": 1e4,
        "square millimeter": 1e6,
        "square inch": 1550,
        "square foot": 10.7639,
        "square yard": 1.19599,
        "acre": 0.000247105,
        "hectare": 0.0001,
    }
    return value * (area_conversions[to_unit] / area_conversions[from_unit])

def convert_volume(value, from_unit, to_unit):
    volume_conversions = {
        "cubic meter": 1,
        "liter": 1000,
        "milliliter": 1e6,
        "cubic centimeter": 1e6,
        "cubic inch": 61023.7,
        "cubic foot": 35.3147,
        "gallon": 264.172,
        "quart": 1056.69,
        "pint": 2113.38,
    }
    return value * (volume_conversions[to_unit] / volume_conversions[from_unit])

def convert_speed(value, from_unit, to_unit):
    speed_conversions = {
        "meter per second": 1,
        "kilometer per hour": 3.6,
        "mile per hour": 2.23694,
        "foot per second": 3.28084,
        "knot": 1.94384,
    }
    return value * (speed_conversions[to_unit] / speed_conversions[from_unit])

# Streamlit app
def main():
    st.title("Professional Unit Converter")
    st.write("Convert between different units easily!")

    # Select conversion type
    conversion_type = st.selectbox(
        "Select Conversion Type",
        ["Length", "Weight", "Temperature", "Area", "Volume", "Speed"]
    )

    # Input value
    value = st.number_input("Enter value to convert", value=1.0)

    # Define units based on conversion type
    if conversion_type == "Length":
        units = ["meter", "kilometer", "centimeter", "millimeter", "inch", "foot", "yard", "mile"]
    elif conversion_type == "Weight":
        units = ["kilogram", "gram", "milligram", "pound", "ounce"]
    elif conversion_type == "Temperature":
        units = ["celsius", "fahrenheit", "kelvin"]
    elif conversion_type == "Area":
        units = ["square meter", "square kilometer", "square centimeter", "square millimeter", "square inch", "square foot", "square yard", "acre", "hectare"]
    elif conversion_type == "Volume":
        units = ["cubic meter", "liter", "milliliter", "cubic centimeter", "cubic inch", "cubic foot", "gallon", "quart", "pint"]
    elif conversion_type == "Speed":
        units = ["meter per second", "kilometer per hour", "mile per hour", "foot per second", "knot"]

    # Select from and to units
    from_unit = st.selectbox("From unit", units)
    to_unit = st.selectbox("To unit", units)

    # Perform conversion
    if st.button("Convert"):
        if conversion_type == "Length":
            result = convert_length(value, from_unit, to_unit)
        elif conversion_type == "Weight":
            result = convert_weight(value, from_unit, to_unit)
        elif conversion_type == "Temperature":
            result = convert_temperature(value, from_unit, to_unit)
        elif conversion_type == "Area":
            result = convert_area(value, from_unit, to_unit)
        elif conversion_type == "Volume":
            result = convert_volume(value, from_unit, to_unit)
        elif conversion_type == "Speed":
            result = convert_speed(value, from_unit, to_unit)
        st.success(f"Converted value: {result:.4f} {to_unit}")

# Run the app
if __name__ == "__main__":
    main()