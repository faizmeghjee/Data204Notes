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

# %% STARSHIP DATA 

# WORKING

# my_list = [] 

# req = requests.get('https://swapi.dev/api/starships/?page=1')

# # print(req.json()['results']) # the starship data

# starships = req.json()['results']

# for result in starships:
#     # print(result)
#     my_list.append(result)

# print(my_list)

# %% PILOTS DATA

# req = requests.get('https://swapi.dev/api/starships/?page=1')

# starships = req.json()['results']

# for result in my_list:
#     print(result['pilots'])


# print(req.json()['results'][0]['pilots']) # the starship data for pilots

# %% GET PILOT DOCUMENTS

# my_list - []

# req = requests.get('https://swapi.dev/api/starships/?page=1')

# starships = req.json()['results']

# pilot_data = []

# for result in my_list:
#     # print(result['pilots'])
#     pilots = result['pilots']

#     for idx in pilots:
#         # print(idx)
#         pilot_req = requests.get(f'{idx}')
#         # print(pilot_req.json()['name'])
#         data = pilot_req.json()
#         # print(data)
#         pilot_data.append(data)

#     result['pilots'] = pilot_data

# print(my_list)

# %% Replacing the dictionries of each pilot with their ids

# import pymongo
# try: 
#     client = pymongo.MongoClient() # establish connection
#     print('Connection Successful')
# except:
#     print('Uh oh, me no connect')

# db = client['starwars'] # creates db variable using the string given by user
# col_ships = db['starships']
# col_people = db['people'] # creates col variable using the string given by user

# starships = col_ships.find({})

# for document in starships:
#     data = []
#     pilots = document['pilots']

#     for pilot in pilots:
#         z = pilot['name']
#         each_pilot_id = col_people.find( {'name': f'{z}'}, {'_id': 1} )
#         for id1 in each_pilot_id:
#             id1
#             data.append(id1)

#     print(data)

