# ======================================================
# Tyler Wafkowksi
# Student ID: 002090157
# ======================================================

from Package import total_dist
from csv_package_reader import full_hash_table
import datetime
import sys



class Main:
    print('Welcome to the state of the art WGUPS Tracking System for packages!')
    print('The current round finished in', "{0:.2f}".format(total_dist(), 2), 'miles')
    
    
    # O(n) -> interface options
    user_choice = input('There are a few options for you: '
                        '\n 1: Please enter individual_package to find a package for an individual'
                        '\n 2: Please enter status to view the status of your delivery'
                        '\n 3: If you wish to EXIT. Please type exit '
                        '\n Please enter your selection: ')
    
    while user_choice != 'exit':
        # O(n) -> status of packages
        if user_choice == 'status':
            try:
                package_status = input('Time needs to be in (HH:MM:SS) format: ')
                (h, m, s) = package_status.split(':')
                user_time_convert = datetime.timedelta(hours = int(h), minutes = int(m), seconds = int(s))
                
                
                # O(n^2)
                for count in range(1, 41):
                    try:
                        time_first = full_hash_table().get(str(count))[9]
                        time_second = full_hash_table().get(str(count))[10]
                        (h, m, s) = time_first.split(':')
                        time_first_convert = datetime.timedelta(hours = int(h), minutes = int(m), seconds = int(s))
                        (h, m, s) = time_second.split(':')
                        time_second_convert = datetime.timedelta(hours = int(h), minutes = int(m), seconds = int(s))
                    except ValueError:
                        pass
                    
                    if time_first_convert >= user_time_convert:
                        full_hash_table().get(str(count))[10] = 'Package is currently at the Delivery Hub'
                        full_hash_table().get(str(count))[9] = 'Package leaves at ---> ' + time_first
                        
                        print('Package ID --->', full_hash_table().get(str(count))[0], ' Street address --->',
                              full_hash_table().get(str(count))[2], full_hash_table().get(str(count))[3],
                              full_hash_table().get(str(count))[4], full_hash_table().get(str(count))[5],
                              ' Delivery time required --->', full_hash_table().get(str(count))[6],
                              ' Package mass --->', full_hash_table().get(str(count))[7], ' Status of truck --->',
                              full_hash_table().get(str(count))[9], 'Delivery status --->',
                              full_hash_table().get(str(count))[10])
                    elif time_first_convert <= user_time_convert:
                        # sees which packages have left the delivery hub but haven't been delivered
                        if user_time_convert < time_second_convert:
                            full_hash_table().get(str(count))[10] = 'Currently on its way'
                            full_hash_table().get(str(count))[9] = 'Package left at ---> ' + time_first
                            
                            print('Package ID --->', full_hash_table().get(str(count))[0], ' Street address --->',
                                  full_hash_table().get(str(count))[2], full_hash_table().get(str(count))[3],
                                  full_hash_table().get(str(count))[4], full_hash_table().get(str(count))[5],
                                  ' Delivery time required --->', full_hash_table().get(str(count))[6],
                                  ' Package mass --->', full_hash_table().get(str(count))[7], ' Status of truck --->',
                                  full_hash_table().get(str(count))[9], ' Delivery status --->',
                                  full_hash_table().get(str(count))[10])
                        
                        # checks if everything was delivered and shows time
                        else:
                            full_hash_table().get(str(count))[10] = 'Package delivered at ---> ' + time_second
                            full_hash_table().get(str(count))[9] = 'Package left at ---> ' + time_first
                            
                            print('Package ID --->', full_hash_table().get(str(count))[0], ' Street address --->',
                                  full_hash_table().get(str(count))[2], full_hash_table().get(str(count))[3],
                                  full_hash_table().get(str(count))[4], full_hash_table().get(str(count))[5],
                                  ' Delivery time required --->', full_hash_table().get(str(count))[6],
                                  'Package mass --->', full_hash_table().get(str(count))[7], ' Status of truck --->',
                                  full_hash_table().get(str(count))[9], ' Delivery status --->',
                                  full_hash_table().get(str(count))[10])
            except IndexError:
                print(IndexError)
                sys.exit()
            except ValueError:
                print('Invalid Entry')
                sys.exit()
            
        
        elif user_choice == 'individual_package':
            try:
                pack_id = input('Enter a package id to search ---> ')
                time_first = full_hash_table().get(str(pack_id))[9]
                time_second = full_hash_table().get(str(pack_id))[10]
                pack_status_time = input('Enter the time in (HH:MM:SS) format please: ')
                (h, m, s) = pack_status_time.split(':')
                user_time_convert = datetime.timedelta(hours = int(h), minutes = int(m), seconds = int(s))
                (h, m, s) = time_first.split(':')
                time_first_convert = datetime.timedelta(hours = int(h), minutes = int(m), seconds = int(s))
                (h, m, s) = time_second.split(':')
                time_second_convert = datetime.timedelta(hours = int(h), minutes = int(m), seconds = int(s))
                
                # checks to see if package has left delivery hub
                if time_first_convert >= user_time_convert:
                    full_hash_table().get(str(pack_id))[10] = 'Package at delivery hub'
                    full_hash_table().get(str(pack_id))[9] = 'Package leaves at ---> ' + time_first
                    
                    print('Package ID --->', full_hash_table().get(str(pack_id))[0], ' Street address --->',
                                  full_hash_table().get(str(pack_id))[2], full_hash_table().get(str(pack_id))[3],
                                  full_hash_table().get(str(pack_id))[4], full_hash_table().get(str(pack_id))[5],
                                  ' Delivery time required --->', full_hash_table().get(str(pack_id))[6],
                                  'Package mass --->', full_hash_table().get(str(pack_id))[7], ' Status of truck --->',
                                  full_hash_table().get(str(pack_id))[9], ' Delivery status --->',
                                  full_hash_table().get(str(pack_id))[10])
                elif time_first_convert <= user_time_convert:
                    # check if package has left delivery hub but hasn't been delivered
                    if user_time_convert < time_second_convert:
                        full_hash_table().get(str(pack_id))[10] = 'Currently on its way'
                        full_hash_table().get(str(pack_id))[9] = 'Package left at ---> ' + time_first
                        
                        print('Package ID --->', full_hash_table().get(str(pack_id))[0], ' Street address --->',
                                  full_hash_table().get(str(pack_id))[2], full_hash_table().get(str(pack_id))[3],
                                  full_hash_table().get(str(pack_id))[4], full_hash_table().get(str(pack_id))[5],
                                  ' Delivery time required --->', full_hash_table().get(str(pack_id))[6],
                                  'Package mass --->', full_hash_table().get(str(pack_id))[7], ' Status of truck --->',
                                  full_hash_table().get(str(pack_id))[9], ' Delivery status --->',
                                  full_hash_table().get(str(pack_id))[10])
                        
                    # sees if package has already been delivered
                    else:
                        full_hash_table().get(str(pack_id))[10] = 'Package delivered at ---> ' + time_second
                        full_hash_table().get(str(pack_id))[9] = 'Package left at ---> ' + time_first
                        
                        print('Package ID --->', full_hash_table().get(str(pack_id))[0], ' Street address --->',
                                  full_hash_table().get(str(pack_id))[2], full_hash_table().get(str(pack_id))[3],
                                  full_hash_table().get(str(pack_id))[4], full_hash_table().get(str(pack_id))[5],
                                  ' Delivery time required --->', full_hash_table().get(str(pack_id))[6],
                                  'Package mass --->', full_hash_table().get(str(pack_id))[7], ' Status of truck --->',
                                  full_hash_table().get(str(pack_id))[9], ' Delivery status --->',
                                  full_hash_table().get(str(pack_id))[10])
            except ValueError:
                print('Invalid Entry')
                sys.exit()
        elif user_choice == 'exit':
            sys.exit()
        else:
            print('Invalid Entry')
            sys.exit()