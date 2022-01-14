from Distance import search_distance
from Distance import truck_one_time
from Distance import truck_two_time
from Distance import truck_three_time
from Distance import shortest_path
from Distance import check_current_dist
from Distance import truck_one_fin_func
from Distance import truck_one_fin_index_func
from Distance import truck_two_fin_func
from Distance import truck_two_fin_index_func
from Distance import truck_three_fin_func
from Distance import truck_three_fin_index_func

from csv_package_reader import full_hash_table
from csv_package_reader import check_truck_one
from csv_package_reader import check_truck_two
from csv_package_reader import check_truck_one_trip_two

import datetime
import Distance




# from csv_package_reader import full_hash_table, check_truck_one, check_truck_two
# from csv_package_reader import check_truck_one_trip_two
# import datetime
# import Distance


# Truck one
truck_one_delivery = []
truck_one_distance = []

# Truck two
truck_two_delivery = []
truck_two_distance = []

# Truck three
truck_three_delivery = []
truck_three_distance = []

# when the specified trucks leave the delivery base in the morning
time_one = '8:00:00'
time_two = '9:10:00'
time_three = '11:00:00'


# Conversion into time delta
(h, m, s) = time_one.split(':')
transform_time_one = datetime.timedelta(hours = int(h), minutes = int(m), seconds = int(s))

(h, m, s) = time_two.split(':')
transform_time_two = datetime.timedelta(hours = int(h), minutes = int(m), seconds = int(s))

(h, m, s) = time_three.split(':')
transform_time_three = datetime.timedelta(hours = int(h), minutes = int(m), seconds = int(s))


# O(n) -> updates status of packages
i = 0
for value in check_truck_one():
    check_truck_one()[i][9] = time_one
    truck_one_delivery.append(check_truck_one()[i])
    i += 1
    

# O(n2) -> compares addresses and adds it to index
try:
    truck_one_count = 0
    for k in truck_one_delivery:
        for j in Distance.address_check():
            if k[2] == j[2]:
                truck_one_distance.append(j[0])
                truck_one_delivery[truck_one_count][1] = j[0]
        truck_one_count += 1
except IndexError:
    pass
# calls shortest path algo to sort packages
shortest_path(truck_one_delivery, 1, 0)
truck_one_total_dist = 0


# O(n) -> takes val from truck one and through dist function
truck_one_packageid = 0
for index in range(len(truck_one_fin_index_func())):
    try:
        # total distance for truck one
        truck_one_total_dist = search_distance(int(truck_one_fin_index_func()[index]), int(truck_one_fin_index_func()[index + 1]), truck_one_total_dist)
        deliver_package = truck_one_time(check_current_dist(int(truck_one_fin_index_func()[index]), int(truck_one_fin_index_func()[index + 1])))
        truck_one_fin_func()[truck_one_packageid][10] = (str(deliver_package))
        full_hash_table().update(int(truck_one_fin_func()[truck_one_packageid][0]), truck_one_delivery)
        truck_one_packageid += 1
    
    except IndexError:
        pass
    
        
# O(n) -> updates statues of packages(truck two)
i = 0
for value in check_truck_two():
    check_truck_two()[i][9] = time_two
    truck_two_delivery.append(check_truck_two()[i])
    i += 1
    
    
# O(n2) -> compares addresses and adds it to index(truck two)
try:
    truck_two_count = 0
    for k in truck_two_delivery:
        for j in Distance.address_check():
            if k[2] == j[2]:
                truck_two_distance.append(j[0])
                truck_two_delivery[truck_two_count][1] = j[0]
        truck_two_count += 1

except IndexError:
    pass


# calls shortest path algo to sort packages(truck two)
shortest_path(truck_two_delivery, 2, 0)
truck_two_total_dist = 0


# O(n) -> takes val from truck two and through dist function
truck_two_packageid = 0
for index in range(len(truck_two_fin_index_func())):
    try:
        # total distance for truck two
        truck_two_total_dist = search_distance(int(truck_two_fin_index_func()[index]), int(truck_two_fin_index_func()[index + 1]), truck_two_total_dist)
        deliver_package = truck_two_time(check_current_dist(int(truck_two_fin_index_func()[index]), int(truck_two_fin_index_func()[index + 1])))
        truck_two_fin_func()[truck_two_packageid][10] = (str(deliver_package))
        full_hash_table().update(int(truck_two_fin_func()[truck_two_packageid][0]), truck_two_delivery)
        truck_two_packageid += 1
    
    except IndexError:
        pass
    
    

# O(n) updates status of packages(truck three)
i = 0

for value in check_truck_one_trip_two():
    check_truck_one_trip_two()[i][9] = time_three
    truck_three_delivery.append(check_truck_one_trip_two()[i])
    i += 1
    
    
    
# O(n2) -> compares addresses and adds it to index(truck three)
try:
    truck_three_count = 0
    for k in truck_three_delivery:
        for j in Distance.address_check():
            if k[2] == j[2]:
                truck_three_distance.append(j[0])
                truck_three_delivery[truck_three_count][1] = j[0]
        truck_three_count += 1
        
except IndexError:
    pass


# calls shortest path algo to sort packages
shortest_path(truck_three_delivery, 3, 0)
truck_three_total_dist = 0

# O(n) -> takes val from truck three(truck one trip two) and through dist function
truck_three_packageid = 0
for index in range(len(truck_three_fin_index_func())):
    try:
        # total distance for truck three
        truck_three_total_dist = search_distance(int(truck_three_fin_index_func()[index]), int(truck_three_fin_index_func()[index + 1]), truck_three_total_dist)
        deliver_package = truck_three_time(check_current_dist(int(truck_three_fin_index_func()[index]), int(truck_three_fin_index_func()[index + 1])))
        truck_three_fin_func()[truck_three_packageid][10] = (str(deliver_package))
        full_hash_table().update(int(truck_three_fin_func()[truck_three_packageid][0]), truck_three_delivery)
        truck_three_packageid += 1
    except IndexError:
        pass
    


# O(1) -> total dist for all of the trucks
def total_dist():
    total_dist = truck_one_total_dist + truck_two_total_dist + truck_three_total_dist
    return total_dist
    

    
