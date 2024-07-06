def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def convert():
    print("**********Temperature Conversion Program**********")
    print("=================================================")
    while True:
        temprature = float(input("Enter Temperature value: "))
        unit = input("Enter unit of measurement (Celsius(CL) or Fahrenheit(FH)): ").lower()

        if unit == 'cl':
            converted_temprature = celsius_to_fahrenheit(temprature)
            print(f"{temprature} Celsius is equal to {converted_temprature: }℉  (Fahrenheit).")
        elif unit == 'fh':
            converted_temprature = fahrenheit_to_celsius(temprature)
            print(f"{temprature} Fahrenheit is equal to {converted_temprature: }℃  (Celsius).")

        else:
            print("Invalid unit of measurement. Please enter either Celcius or Fahrenheit.")


if __name__ == "__main__":
    convert()