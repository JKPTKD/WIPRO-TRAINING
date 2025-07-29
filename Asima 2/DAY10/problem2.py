'''Name: Asima Nayak
    ID:30396
   Email:asimanayak874@gmail.com
   Date:17-July-2025
   Purpose:Create a Temperature Class with:
		fromCelsius() and fromFahrenheit() as classmethods
		A staticmethod to convert Celsius to Fahrenheit and vice versa 
'''
class Temperature:
    def __init__(self, value, unit):
        """
        Initializes a Temperature object.
        :param value: The temperature value.
        :param unit: The unit of temperature ('C' for Celsius, 'F' for Fahrenheit).
        """
        self.value = value
        if unit.upper() in ('C', 'F'):
            self.unit = unit.upper()
        else:
            raise ValueError("Unit must be 'C' (Celsius) or 'F' (Fahrenheit)")

    @classmethod
    def fromCelsius(cls, celsius_value):
        """
        Class method to create a Temperature object from a Celsius value.
        """
        return cls(celsius_value, 'C')

    @classmethod
    def fromFahrenheit(cls, fahrenheit_value):
        """
        Class method to create a Temperature object from a Fahrenheit value.
        """
        return cls(fahrenheit_value, 'F')

    @staticmethod
    def celsius_to_fahrenheit(celsius_value):
        """
        Static method to convert a Celsius temperature to Fahrenheit.
        Formula: F = (C * 9/5) + 32
        """
        return (celsius_value * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit_value):
        """
        Static method to convert a Fahrenheit temperature to Celsius.
        Formula: C = (F - 32) * 5/9
        """
        return (fahrenheit_value - 32) * 5/9

    def __str__(self):
        """
        Returns a user-friendly string representation of the Temperature object.
        """
        return f"{self.value:.2f}°{self.unit}"

    def __repr__(self):
        """
        Returns an official string representation of the Temperature object,
        useful for debugging.
        """
        return f"Temperature(value={self.value}, unit='{self.unit}')"

# --- Demonstration ---
if __name__ == "__main__":
    print("--- Temperature Class Demonstration ---")

    # 1. Creating Temperature objects using classmethods
    temp_celsius = Temperature.fromCelsius(25)
    print(f"Temperature from Celsius: {temp_celsius}")
    print(f"Representation: {repr(temp_celsius)}")

    temp_fahrenheit = Temperature.fromFahrenheit(68)
    print(f"Temperature from Fahrenheit: {temp_fahrenheit}")
    print(f"Representation: {repr(temp_fahrenheit)}")

    # 2. Using the static methods for conversion
    print("\n--- Using Static Methods for Conversion ---")

    c_value = 30
    f_converted = Temperature.celsius_to_fahrenheit(c_value)
    print(f"{c_value}°C is equal to {f_converted:.2f}°F")

    f_value = 212
    c_converted = Temperature.fahrenheit_to_celsius(f_value)
    print(f"{f_value}°F is equal to {c_converted:.2f}°C")

    # Example: Body temperature
    body_temp_f = 98.6
    body_temp_c = Temperature.fahrenheit_to_celsius(body_temp_f)
    print(f"Normal body temperature: {body_temp_f}°F is {body_temp_c:.2f}°C")

    # Example: Freezing point
    freezing_c = 0
    freezing_f = Temperature.celsius_to_fahrenheit(freezing_c)
    print(f"Freezing point: {freezing_c}°C is {freezing_f:.2f}°F")

    # You can also get the value of an existing Temperature object and convert it
    print(f"\n--- Converting existing Temperature objects ---")
    current_temp_in_c = temp_fahrenheit.value # This is 68F
    converted_to_c = Temperature.fahrenheit_to_celsius(current_temp_in_c)
    print(f"{current_temp_in_c}°F is {converted_to_c:.2f}°C")

    current_temp_in_f = temp_celsius.value # This is 25C
    converted_to_f = Temperature.celsius_to_fahrenheit(current_temp_in_f)
    print(f"{current_temp_in_f}°C is {converted_to_f:.2f}°F")