import csv
import datetime

# scans the csv file for all of the distances
with open('csv_files/DistanceMeasurements.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')
    csv_reader = list(csv_reader)

# scans the csv file for all of the names of all possible delivery locations
with open('csv_files/Distance.csv') as name_file:
    name_csv_reader = csv.reader(name_file, delimiter=',')
    name_csv_reader = list(name_csv_reader)


    # O(1) -> rows and columns inserted. Calculates distance total
    def search_distance(row, column, sum_of):
        distances = csv_reader[row][column]
        if distances == '':
            distances = csv_reader[column][row]

        sum_of += float(distances)
        return sum_of


    # O(1) -> returns current distance
    def check_current_dist(row, column):
        distances = csv_reader[row][column]
        if distances == '':
            distances = csv_reader[column][row]
        return float(distances)


    time_list_one = ['8:00:00']
    time_list_two = ['9:10:00']
    time_list_three = ['11:00:00']


    # O(n) -> finds the full distance for the first truck
    def truck_one_time(distances):
        current_time = distances / 18
        distance_in_mins = '{0:02.0f}:{1:02.0f}'.format(*divmod(current_time * 60, 60))
        final_time = distance_in_mins + ':00'
        time_list_one.append(final_time)
        sum = datetime.timedelta()
        for i in time_list_one:
            (h, m, s) = i.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            sum += d
        return sum


    # O(n) -> same as above but with second truck
    def truck_two_time(distances):
        current_time = distances / 18
        distance_in_mins = '{0:02.0f}:{1:02.0f}'.format(*divmod(current_time * 60, 60))
        final_time = distance_in_mins + ':00'
        time_list_two.append(final_time)
        sum = datetime.timedelta()
        for i in time_list_two:
            (h, m, s) = i.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            sum += d
        return sum


    # O(n) -> same as above two but with third truck
    def truck_three_time(distances):
        current_time = distances / 18
        distance_in_mins = '{0:02.0f}:{1:02.0f}'.format(*divmod(current_time * 60, 60))
        final_time = distance_in_mins + ':00'
        time_list_three.append(final_time)
        sum = datetime.timedelta()
        for i in time_list_three:
            (h, m, s) = i.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            sum += d
        return sum


    # O(1) -> returns time objects that will be used in the packages file
    def address_check():
        return name_csv_reader


    # O(1) -> truck list
    truck_one_fin = []
    truck_one_fin_index = []
    truck_two_fin = []
    truck_two_fin_index = []
    truck_three_fin = []
    truck_three_fin_index = []


    # O(n2) -> algorithm finds the shortest distance. Variation of greedy algo
    def shortest_path(truck_distance, truck_num, curr_location):
        if len(truck_distance) == 0:
            return truck_distance
        else:
            try:
                lowest_val = 50.0
                new_location = 0
                for index in truck_distance:
                    if check_current_dist(curr_location, int(index[1])) <= lowest_val:
                        lowest_val = check_current_dist(curr_location, int(index[1]))
                        new_location = int(index[1])

                for index in truck_distance:
                    if check_current_dist(curr_location, int(index[1])) == lowest_val:
                        # first truck
                        if truck_num == 1:
                            truck_one_fin.append(index)
                            truck_one_fin_index.append(index[1])
                            pop_val = truck_distance.index(index)
                            truck_distance.pop(pop_val)
                            curr_location = new_location
                            shortest_path(truck_distance, 1, curr_location)

                        # second truck 
                        elif truck_num == 2:
                            truck_two_fin.append(index)
                            truck_two_fin_index.append(index[1])
                            pop_val = truck_distance.index(index)
                            truck_distance.pop(pop_val)
                            curr_location = new_location
                            shortest_path(truck_distance, 2, curr_location)

                        # third truck
                        elif truck_num == 3:
                            truck_three_fin.append(index)
                            truck_three_fin_index.append(index[1])
                            pop_val = truck_distance.index(index)
                            truck_distance.pop(pop_val)
                            curr_location = new_location
                            shortest_path(truck_distance, 3, curr_location)

            except IndexError:
                pass


    # O(1) -> truck one
    truck_one_fin_index.insert(0, '0')


    def truck_one_fin_index_func():
        return truck_one_fin_index


    def truck_one_fin_func():
        return truck_one_fin


    # O(1) -> truck two
    truck_two_fin_index.insert(0, '0')


    def truck_two_fin_index_func():
        return truck_two_fin_index


    def truck_two_fin_func():
        return truck_two_fin


    # O(1) -> truck three
    truck_three_fin_index.insert(0, '0')


    def truck_three_fin_index_func():
        return truck_three_fin_index


    def truck_three_fin_func():
        return truck_three_fin
