# Define the allowed vehicles list
AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']
choice=""
# FC
def print_allowed_vehicles():
    print("Allowed Vehicles:")
    for vehicle in AllowedVehiclesList:
        print(vehicle)
        
# Function to display the menu
def display_menu(): 
        print("\nAutoCountry Vehicle Finder v0.1") 
        print("1. PRINT all Allowed Vehicles") 
        print("2. Exit") 
        return input("Please enter your choice (1 or 2): ")
        

def main():
    while True:
        choice = display_menu()
        if choice == '1':
            print_allowed_vehicles() 
        
        elif choice == '2': 
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else: 
            print("Invalid choice. Please try again.")
    
# Main function to run the program
if __name__ == "__main__": 
    main()