from package import Package
import csv

class Hashmap:
    def __init__(self, initial_size = 16) -> None:
        # initial value 16 since that is the size of an empty truck
        self.list = []
        for i in range(initial_size):
            self.list.append([])
        
    def insert(self, key, item):
        bucket = hash(key) % len(self.list) # bucket is key modulo list size
        bucket_elements = self.list[bucket] # bucket elements are the key value pairs stored in the list[bucket] subarray

        # update existing entry if exists
        for key_value_pair in bucket_elements:
            # print(key_value_pair)
            if key_value_pair[0] == key:
                key_value_pair[1] = item
                return
        
        # add key value pair to buck if not already there
        key_value_pair = [key, item]
        bucket_elements.append(key_value_pair)
        return
    
    # return an item from the hashmap if it exists
    def get_item(self, key):
        bucket = hash(key) % len(self.list)
        bucket_elements = self.list[bucket]

        # check if key value pair exists in the bucket and return it
        for key_value_pair in bucket_elements:
            if key_value_pair[0] == key:
                return key_value_pair[1]
            
        return None # if not found, return none

    def get_size(self):
        return len(self.list)
    
# create a hashmap of packages from CSV  
def create_pkg_hashmap(filename, pkg_hashmap):
    with open(filename) as packages_csv:
        csv_reader = csv.reader(packages_csv, delimiter = ',')

        # loop through csv and and turn each row into a package object
        # load each package object into hashmap
        for row in csv_reader:
            # temporary variables to ease initialization of package object from csv row
            ID = int(row[0])
            address = row[1]
            city = row[2]
            state = row[3]
            zip_code = int(row[4])
            deadline = row[5]
            weight = float(row[6])
            notes = row[7]
            status = "At Hub"

            # package to load into hashmap
            new_package = Package(ID, address, city, state, zip_code, deadline, weight, notes, status)
            # load object into hashmap
            pkg_hashmap.insert(ID, new_package)