# Temperature Conversion Program
def convert_temperature(value, unit):
    unit = unit.upper()
    
    if unit == "C":  # Celsius
        f = (value * 9/5) + 32
        k = value + 273.15
        return f"Fahrenheit: {f:.2f} °F, Kelvin: {k:.2f} K"

    elif unit == "F":  # Fahrenheit
        c = (value - 32) * 5/9
        k = c + 273.15
        return f"Celsius: {c:.2f} °C, Kelvin: {k:.2f} K"

    elif unit == "K":  # Kelvin
        c = value - 273.15
        f = (c * 9/5) + 32
        return f"Celsius: {c:.2f} °C, Fahrenheit: {f:.2f} °F"

    else:
        return "Invalid unit! Please use C, F, or K."


# --- Main Program ---
try:
    temp = float(input("Enter the temperature value: "))
    unit = input("Enter the unit (C for Celsius, F for Fahrenheit, K for Kelvin): ")
    print(convert_temperature(temp, unit))
except ValueError:
    print("Please enter a valid numeric temperature!")
