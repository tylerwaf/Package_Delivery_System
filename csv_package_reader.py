import csv 
from hash_table import HashTable

with open('csv_files/Packages.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')
    
    
    # Calls hash table class to create package objects
    add_to_hash = HashTable()
    truck_one = []
    truck_two = []
    truck_one_trip_two = []
    
    # O(n) -> takes csv data and adds them into key and value pairs
    for row in csv_reader:
        package_id = row[0]
        address_row = row[1]
        city_row = row[2]
        state_row = row[3]
        zip_code_row = row[4]
        delivery_row = row[5]
        size_row = row[6]
        notes_row = row[7]
        start_delivery = ''
        address_locate = ''
        status_of_delivery = 'at hub'
        iter_value = [package_id, address_locate, address_row, city_row, state_row, zip_code_row, delivery_row, size_row, notes_row, start_delivery, status_of_delivery]
        key = package_id
        value = iter_value
        
        
        
        if value[6] != 'EOD':
            # list for truck one
            if 'Must' in value[7] or 'None' in value[7]:
                truck_one.append(value)
        
        # adds delayed and can only packages to truck two
        if 'Can only be' in value[7]:
            truck_two.append(value)
        if 'Delayed' in value[7]:
            truck_one_trip_two.append(value)
        if '10:30' in value[6]:
            truck_two.append(value)
        if '84104' in value[5] and '10:30' not in value[6]:
            # if wrong address, then it will be corrected to the right address
            truck_one_trip_two.append(value)
        if 'Wrong address listed' in value[8]:
            value[2] = '410 S State St'
            value[5] = '84111'
            truck_one_trip_two.append(value)
        if value not in truck_one and value not in truck_two and value not in truck_one_trip_two:
            if len(truck_two) > len(truck_one_trip_two):
                truck_one_trip_two.append(value)
            else:
                truck_two.append(value)
                # adds values from csv to hash table
        add_to_hash.add(key, value)
        
        
        
        # O(1) -> get full list of values from the start
        def full_hash_table():
            return add_to_hash
        
        
        # O(1) -> grab packages that are on truck one
        def check_truck_one():
            return truck_one
        
        
        # O(1) -> grab packages that are on truck two
        def check_truck_two():
            return truck_two
        
        
        # O(1) -> grab packages on truck ones second trip
        def check_truck_one_trip_two():
            return truck_one_trip_two
    
        