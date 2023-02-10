# %%
import pymongo
import requests

def big_boi_looper(url: str = 'https://swapi.dev/api/starships/?page='):
    '''
    Loops through the 4 pages of the API where the starships data is
    '''
    try: 
        client = pymongo.MongoClient('mongodb://localhost:27017/') # establish connection
        print('Connection Successful')
    except:
        print('Uh oh, me no connect')
    
    db = client['starwars'] # creates db variable
    col = db['people'] # creates col variable for the collection we are querying for the pilots

    my_list = [] # our data once cleaned

    for page_number in range(1, 5): # iterating through pages 1, 2, 3 and 4
        req = requests.get(url + str(page_number)) # Making a get request where url is concated to the page number
        starships = req.json()['results'] # converts the data we want into a dictionary. (the key name is 'results')

        for ship in starships: # iterating through each dictionary in the list of results
            pilots = ship['pilots'] # creating a new object to iterate through where we are looking at the 'pilots' key
            pilot_data = [] # empty list to hold pilot data from each get request
            
            for pilot_url in pilots: # iterating through the pilots for each starship dictionary
                pilot_req = requests.get(f'{pilot_url}') # Gets the data for each pilot using a get request
                pilot_name = pilot_req.json()['name'] # Converts the request into a useable dictionary
                each_pilot_id = col.find( {'name': f'{pilot_name}'}, {'_id': 1} ) # queries the mongodb collection of the people/pilots

                for identity in each_pilot_id:
                    pilot_data.append(identity['_id']) # Appends the ids of each pilot to the list 'pilot_data'
            
            # previously ship['pilots'] = [url1, url2, url3 , etc] was a list of urls
            ship['pilots'] = pilot_data # Replaces the values for the key 'pilots' with our list of ids

            my_list.append(ship) # Appends data with corrected pilots to a list called 'my_list'

    return my_list

def write_to_mongodb(data: dict, database: str = 'starwars', collectionName: str = 'starships', server: str = 'mongodb://localhost:27017/'):
    '''
    Writes data to a mongodb database
    '''
    try: 
        client = pymongo.MongoClient(server) # establish connection
        print('Connection Successful')
    except:
        print('Uh oh, me no connect')
    
    db = client[database] # creates db variable using the string given by user
    col = db[collectionName] # creates col variable using the string given by user
    col.insert_many(data) # insert the list of dictionaries into the mongodb database
    return print(f'Data has been written to database: {database}')
    
write_to_mongodb(big_boi_looper())


# %%
