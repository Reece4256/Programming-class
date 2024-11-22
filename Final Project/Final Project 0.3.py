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
        
def add_vehicle():
    new_vehicle = input("Please Enter the full Vehicle name you would like to add: ")
    if new_vehicle not in AllowedVehiclesList:
        AllowedVehiclesList.append(new_vehicle) 
        print(f"{new_vehicle} has been added to the allowed vehicles list.")
    else:
        print(f"{new_vehicle} is already in the allowed vehicles list.")



# Function to display the menu
def display_menu(): 
        print("\n********************************") 
        print("AutoCountry Vehicle Finder v0.2") 
        print("********************************") 
        print("1. PRINT all Authorized Vehicles") 
        print("2. SEARCH for Authorized Vehicle") 
        print("3. ADD Authorized Vehicle")
        print("4. Exit")
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
            add_vehicle()
        elif choice == '4':
            print("Thank you for using the AutoCountry Vehicle Finder. Goodbye!")
            break
        else: 
            print("Invalid choice. Please try again.")
    
# Main function to run the program
if __name__ == "__main__": 
    main()