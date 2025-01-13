print("\n*********************************************************************************************\n")
print("\n\t ******** Hi, Welcome to the Temperature Converter! ******** ")
print("\n*********************************************************************************************\n")

while True:
    print("\nChoose a conversion optio from the given menu: \n")
    print("1- Celcius to Farenhite")
    print("2- Fahrenheit to Celsius")
    print("3- Celsius to Kelvin")
    print("4- Kelvin to Celsius")
    print("5- Fahrenheit to Kelvin")
    print("6- Kelvin to Fahrenheit")
    print("7- Exit")

    selected_option = input("\nSelected Option: ")

    if selected_option == "1":
        celsius = float(input("\nCelsius degree temperature: "))
        farenhite = (celsius * 9/5) + 32
        print(f"\n{celsius}°C is equal to {farenhite}°F")

    elif selected_option == "2":
        farenhite = float(input("\nFarenhite degree temperature: "))
        celsius = (farenhite - 32) * 5/9
        print(f"\n{farenhite}°F is equal to {celsius}°C")

    elif selected_option == "3":
        celsius = float(input("\nCelsius degree temperature: "))
        kelvin = celsius + 273.15
        print(f"\n{celsius}°C is equal to {kelvin}°K")

    elif selected_option == "4":
        kelvin = float(input("\nKelvin degree temperature: "))
        celsius = kelvin - 273.15
        print(f"\n{kelvin}°K is equal to {celsius}°C")

    elif selected_option == "5":
        farenhite = float(input("\nFarenhite degree temperature: "))
        kelvin = ((farenhite - 32) * 5/9) + 273.15
        print(f"\n{farenhite}°F is equal to {kelvin}°K")

    elif selected_option == "6":
        kelvin = float(input("\nKelvin degree temperature: ")) 
        farenhite =   ((kelvin - 273.15) * 9/5) + 32
        print(f"\n{kelvin}°K is equal to {farenhite}°F")

    elif selected_option == "7":
        print("\nExiting... Goodbye!\n")
        break

    else:
        print("\n WARNING: Invalid option! Do you want to choose again?")
        print("\n- Yes(y)")
        print("\n- No(n)")

        choice = input("\nChoose one: ").lower()

        if(choice == "y"):
            continue
        else:
            print("\nExiting... Goodbye!\n")
            break