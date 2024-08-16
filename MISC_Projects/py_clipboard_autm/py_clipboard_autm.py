import sys
import clipboard  
import json

#print(sys.argv) - gets the command line argument

#problem is it takes everything after keyword 'py' o nthe command line. this includes the file name too. so we use 
#print(sys.argv[1:]) = [1:] = means everything except the first element 

SAVED_DATA = "clipboard.json"

def save_item(filepath, data):
    with open(filepath, "w") as f:  #"w" mode stands for write. i will either overwrite ior create a new file
        json.dump(data, f) #json lobrary to dump data . save data to  a json file
        


def load_item(filepath):
    try:                              
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}





if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_item(SAVED_DATA)
    
    if command == "save":
        key = input("Enter a key : ")
        data[key] = clipboard.paste()
        save_item(SAVED_DATA, data)
        print("data saved")
        
    elif command == "load":
        key = input("enter a key : ")
        if key in data:
            clipboard.copy(data[key])
            print("data copied")
        else:
            print("key does not exist")
            
    elif command == "list":
        print(data)
    else:
        print("Invalid command")
else:
    print("Invalid number of arguments. Enter only one")