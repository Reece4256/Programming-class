# Define the allowed vehicles list
AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']
choice=""
# FC
def print_allowed_vehicles():
    print("Allowed Vehicles:")
    for vehicle in AllowedVehiclesList:
        print(vehicle)

def search_vehicle():
    search_query = input("Please Enter the full Vehicle name: ")
    if search_query in AllowedVehiclesList:
        print(f"{search_query} is an authorized vehicle.")
    else:
        print(f"{search_query} is not an authorized vehicle. If you received this in error, please check the spelling and try again.")
        


# Function to display the menu
def display_menu(): 
        print("\n********************************") 
        print("AutoCountry Vehicle Finder v0.2") 
        print("********************************") 
        print("1. PRINT all Authorized Vehicles") 
        print("2. SEARCH for Authorized Vehicle") 
        print("3. Exit") 
        print("********************************") 
        return input("Please enter your choice (1, 2, or 3): ")
        

def main():
    while True:
        choice = display_menu()
        if choice == '1':
            print_allowed_vehicles() 
        
        elif choice == '2': 
            search_vehicle()
        elif choice == '3': 
            print("Thank you for using the AutoCountry Vehicle Finder. Goodbye!")
            break
        else: 
            print("Invalid choice. Please try again.")
    
# Main function to run the program
if __name__ == "__main__": 
    main()