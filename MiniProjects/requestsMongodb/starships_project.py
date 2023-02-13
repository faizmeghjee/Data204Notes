# %%
import pymongo
import requests

def big_boi_looper(url: str = 'https://swapi.dev/api/starships/?page='):
    '''
    Loops through the 4 pages of the API where the starships data is
    '''
    try: 
        client = pymongo.MongoClient('mongodb://localhost:27017/') 
        print('Connection Successful')
    except:
        print('Uh oh, me no connect')
    db = client['starwars']
    col = db['people']
    data = [] 

    for page_number in range(1, 5):
        req = requests.get(url + str(page_number)) 
        starships = req.json()['results'] 
        for ship in starships: 
            pilots = ship['pilots'] 
            pilot_data = [] 
            for pilot_url in pilots: 
                req_p = requests.get(f'{pilot_url}')
                pilot_name = req_p.json()['name']
                each_pilot_id = col.find( {'name': f'{pilot_name}'}, {'_id': 1} )
                for idx in each_pilot_id:
                    pilot_data.append(idx['_id']) 
            ship['pilots'] = pilot_data 
            data.append(ship) 
    return data

def write_to_mongodb(data: dict, database: str = 'starwars', collectionName: str = 'starships', server: str = 'mongodb://localhost:27017/'):
    '''
    Writes data to a mongodb database
    '''
    try: 
        client = pymongo.MongoClient(server)
        print('Connection Successful')
    except:
        print('Uh oh, me no connect')
    db = client[database] 
    col = db[collectionName] 
    col.insert_many(data)
    return print(f'Data is in database: {database}\n Collection: {collectionName}')
    
write_to_mongodb(big_boi_looper())

# %%
