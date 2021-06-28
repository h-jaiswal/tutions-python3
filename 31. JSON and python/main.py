import json
from os import path

# NOTE RUN all FILES with file handling IN TERMINAL ONLY and NOT using RUN BUTTON
# NOTE Articles https://www.geeksforgeeks.org/json-dump-in-python/ 
#      https://www.geeksforgeeks.org/json-load-in-python/
#      https://www.geeksforgeeks.org/json-loads-in-python/
#      https://www.geeksforgeeks.org/json-dumps-in-python/

# file type does not matter while reading or writing using json library/package

def main():

    data = {
        "name": "ABC",
        "age" : 19
    }

    # write list of dictionary to json
    with open("write2.txt", "w") as fout:
        json.dump(data , fout, indent=4)

    # list of dictionary
    data = [{'id': 123, 'data': 'qwerty', 'indices': [1,10]}, {'id': 345, 'data': 'mnbvc', 'indices': [2,11]}]


    # write list of dictionary to json
    with open("write.json", "w") as fout:
        json.dump(data , fout)

    # read list of dictionary to json
    

    with open("write.json", "r") as read_file:
        data = json.load(read_file)
        print(type(data))
        for item in data:
            for k,v in item.items():
                print( "{} - {}".format(k,v) )

    with open("read.txt", "r") as read_file:
        data = json.load(read_file)
        print(type(data))
        for item in data:
            for k,v in item.items():
                print( "{} - {}".format(k,v) )
    
    # read a json file  (as dictionary)
    with open("read.json", "r") as read_file:
        data = json.load(read_file)
        print(type(data))
        print(data)

    
main()