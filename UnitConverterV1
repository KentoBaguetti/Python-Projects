def distanceMetric(value, unit_in, unit_out):
    conversion = {"m" : 1.00,
                  "mm" : 0.001,
                  "cm" : 0.01,
                  "km" : 1000.00}
    return str(value*(conversion[unit_in]/conversion[unit_out])) + unit_out

def weightMetric(value, unit_in, unit_out):
    conversion = {"g" : 1.00,
                  "kg" : 1000.00,
                  "mg" : 0.001}
    return str(value*(conversion[unit_in]/conversion[unit_out]))

def printMenu():
    print("\n---------------------------------------------")
    print("Unit Converter | Supports Metric weight and distance conversions")
    print("Distances supported: Meter (m), Millimeter (mm), Centimeter (cm), Kilometer (km)")
    print("Weights supported: Grams (g), Milligrams (mg), Kilograms (kg)")
    print("What would you like to convert? Distance (d), Weight (w)")
    print("---------------------------------------------\n")
    
def main():
    printMenu()
    userInput = input("Distance (d) or Weight (w) or exit(Any other key): ")
    while userInput != "w" or userInput != "d":
        if userInput == "d":
            try:
                value = float(input("Enter value: "))
                unitIn = input("Enter the unit you want to convert from (m, mm, cm, km): ")
                unitOut = input("Enter the value you want covert to (m, mm, cm, km): ")
                print(distanceMetric(value, unitIn, unitOut))
                printMenu()
                userInput = input("Distance (d) or Weight (w) or exit(Any other key): ")
            except ValueError:
                print("Invalid Input. Try Again.")
                printMenu()
                userInput = input("Distance (d) or Weight (w) or exit(Any other key): ")
        elif userInput == "w":
            try:
                value = float(input("Enter value: "))
                unitIn = input("Enter the unit you want to convert from (g, kg, mg): ")
                unitOut = input("Enter the unit you want to convert to (g, kg, mg): ")
                print(weightMetric(value, unitIn, unitOut))
                printMenu()
                userInput = input("Distance (d) or Weight (w) or exit(Any other key): ")
            except ValueError:
                print("Invalid Input. Try Again.")
                printMenu()
                userInput = input("Distance (d) or Weight (w) or exit(Any other key): ")
        else:
            break
                
main()
