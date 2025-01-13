print("\n*********************************************************************************************\n")
print("\n\t ******** Hi, Welcome to the Temperature Converter! ******** ")
print("\n*********************************************************************************************\n")

def get_valid_option():
    while True:
        selected_option = input("\nSelected Option: ")
        if selected_option.isdigit() and 1 <= int(selected_option) <= 7:
            return int(selected_option)
        else:
            print("\nWARNING: Please enter a valid option (1-7).")

def get_valid_temperature(prompt, allow_negative=False):
    while True:
        try:
            temp = float(input(prompt))
            if not allow_negative and temp < 0:
                print("\nERROR: Temperature cannot be negative for this scale. Please try again.")
                continue
            return temp
        except ValueError:
            print("\nERROR: Please enter a valid numeric value.")

while True:
    print("\nChoose a conversion option from the given menu: \n")
    print("1- Celsius to Fahrenheit")
    print("2- Fahrenheit to Celsius")
    print("3- Celsius to Kelvin")
    print("4- Kelvin to Celsius")
    print("5- Fahrenheit to Kelvin")
    print("6- Kelvin to Fahrenheit")
    print("7- Exit")

    selected_option = get_valid_option()

    if selected_option == 1:
        celsius = get_valid_temperature("\nCelsius degree temperature: ")
        fahrenheit = (celsius * 9/5) + 32
        print(f"\n{celsius}°C is equal to {fahrenheit}°F")

    elif selected_option == 2:
        fahrenheit = get_valid_temperature("\nFahrenheit degree temperature: ")
        celsius = (fahrenheit - 32) * 5/9
        print(f"\n{fahrenheit}°F is equal to {celsius}°C")

    elif selected_option == 3:
        celsius = get_valid_temperature("\nCelsius degree temperature: ")
        kelvin = celsius + 273.15
        print(f"\n{celsius}°C is equal to {kelvin}°K")

    elif selected_option == 4:
        kelvin = get_valid_temperature("\nKelvin degree temperature (non-negative): ", allow_negative=False)
        celsius = kelvin - 273.15
        print(f"\n{kelvin}°K is equal to {celsius}°C")

    elif selected_option == 5:
        fahrenheit = get_valid_temperature("\nFahrenheit degree temperature: ")
        kelvin = ((fahrenheit - 32) * 5/9) + 273.15
        print(f"\n{fahrenheit}°F is equal to {kelvin}°K")

    elif selected_option == 6:
        kelvin = get_valid_temperature("\nKelvin degree temperature (non-negative): ", allow_negative=False)
        fahrenheit = ((kelvin - 273.15) * 9/5) + 32
        print(f"\n{kelvin}°K is equal to {fahrenheit}°F")

    elif selected_option == 7:
        print("\nExiting... Goodbye!\n")
        break

    else:
        print("\nERROR: Invalid option!")

    print("\nDo you want to choose again?")
    print("\n- Yes (y)")
    print("\n- No (n)")

    choice = input("\nChoose one: ").strip().lower()
    while choice not in ["y", "n"]:
        print("\nERROR: Please enter 'y' for Yes or 'n' for No.")
        choice = input("\nChoose one: ").strip().lower()

    if choice == "n":
        print("\nExiting... Goodbye!\n")
        break
