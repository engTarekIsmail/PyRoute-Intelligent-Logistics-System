from config import SystemConfig
from inventory import Category, Product
from routing import CityMapFacade, FastestRouteStrategy
from logistics import OrderQueueManager, Order, CustomerObserver

def main():
    # 1. Singleton Check
    config = SystemConfig()
    
    # 2. Setup Data Structures
    inventory_root = Category("Main Inventory")
    queue_manager = OrderQueueManager()
    city_map = CityMapFacade(strategy=FastestRouteStrategy())
    
    # 3. Mock Data Loading (Student replaces this with File I/O)
    laptop = Product("Laptop", 1200.00, 101)
    inventory_root.add(laptop)
    
    # 4. Interactive Loop
    while True:
        print("\n--- PyRoute Logistics System ---")
        print("1. View Inventory")
        print("2. Add Order")
        print("3. Process Next Order")
        print("4. Calculate Route")
        print("5. Exit")
        
        choice = input("Select option: ")
        
        if choice == "1":
            inventory_root.show_details()
        
        elif choice == "2":
            cust_name = input("Customer Name: ")
            dest = input("Destination Node: ")
            # Creating an Observer for this customer
            customer = CustomerObserver(cust_name)
            queue_manager.attach(customer)
            
            new_order = Order(id=1, customer=cust_name, destination=dest, priority=1)
            queue_manager.add_order(new_order)
        
        elif choice == "3":
            # Process the next order in queue
            queue_manager.process_next_order()
        
        elif choice == "4":
            # Implement the routing call here
            start_node = input("Enter start node: ")
            end_node = input("Enter destination node: ")
            try:
                route = city_map.calculate_route(start=start_node, end=end_node)
                print(f"Fastest route from {start_node} to {end_node}: {route}")
            except Exception as e:
                print(f"Error calculating route: {e}")
        
        elif choice == "5":
            print("Exiting PyRoute System. Goodbye!")
            break
        
        else:
            print("Invalid option. Please select 1-5.")

if __name__ == "__main__":
    main()
