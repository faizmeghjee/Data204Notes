# %%
import requests

cyndaquil = requests.get('https://pokeapi.co/api/v2/pokemon/cyndaquil')
cyndaquil_cont = cyndaquil.json()

print(cyndaquil_cont['types'])

cubone = requests.get('https://pokeapi.co/api/v2/pokemon/cubone')
cubone_cont = cubone.json()

print(cubone_cont['types'])

marowak = requests.get('https://pokeapi.co/api/v2/pokemon/marowak')
marowak_cont = marowak.json()

print(marowak_cont['types'])

mewtwo = requests.get('https://pokeapi.co/api/v2/pokemon/mewtwo')
mewtwo_cont = mewtwo.json()

print(mewtwo_cont['types'])


# %%
import requests
import json

# GET
postcodes_req = requests.get('https://api.postcodes.io/postcodes/kt123pf')

# print(postcodes_req.status_code)
# print(postcodes_req.headers)
# print(postcodes_req.content)

postcodes_dict = postcodes_req.json() # converts the get request content into a dictionary
# print(postcodes_dict) # prints the dictionary


# POST
data = json.dumps({'postcodes': ['0X49 5NU', 'M32 0JG', 'NE30 1DP']}) # converts the data into a formatted string
headers = {'Content-Type': 'application/json'}

post_multi_req = requests.post('https://api.postcodes.io/postcodes', headers=headers, data=data)
print(post_multi_req.json()['result'])




# %%
