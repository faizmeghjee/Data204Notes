# %% TOOLS

## HTTP request methods are most important in REST APIs?
# POST # The POST method submits an entity to the specified resource, often causing a change in state or side effects on the server.
# PATCH # The PATCH method applies partial modifications to a resource.
# PUT # The PUT method replaces all current representations of the target resource with the request payload.
# GET # The GET method requests a representation of the specified resource. Requests using GET should only retrieve data.
# DELETE # The DELETE method deletes the specified resource.

# curl -v (v for verbose)

# %% Response Codes

200 # okay response
300 # some kind of relocation of reasources
400 # some sort of error e.g. 404 not found (client side)
500 # server error (server side)

# Questions

# What are cookies used for?
# Storing information on the browser for sending to a server
# cookies help identify the specific user/browser using the website.

# http vs https # https is encrypted
# how things communicate with things on the internet

# What is HTTPS?
# A sercure version of HTTP, providing encryption of messages

# Which 2 versions of HTTP are found widely on the Internet today?
# 1.1
# 2

# What is TLS?
# Transport Layer Security, the current standard for implementing secure internet connections

# What does HTTP stand for?
# Hypertext Transfer Protocol

# What is curl?
# A command-line HTTP client

# True or False: An HTTP request can contain a body?
# True

# %%

## JSON (JavaScript Object Notation)

# 6 types allowed in a json
# number (either int or float)
# string
# boolean
# array
# json object
# null

# Questions

# Which 6 of these types of data can be included in a JSON data structure?
# number (either int or float)
# string
# boolean
# array
# json object
# null

# What is Unicode?
# A standard for encoding text

# %%

# Whats an API?
# A mechanism which allows two computer programs to communciate with each other

# What is REST?
# Respresentational state transfer
# REST is an architechtural style
# Not a standard 
# Not an implementation technology

# What does RESTful mean?
# 'RESTful' means 'complies with the REST architectural style'

# REST APIs must use specific technologies in their implementation
# False

# REST Constraints (key architectual concepts)
# Client-Server architecture
# Statelessness
# Cacheability
# Layered System
# Uniform Interface:
    # Resource identification in requests, data format transferred not the same as storage
    # Resource manipulation through representations
    # Self-descriptive messages
    # Hypermedia as the engine of application state

# REST Technologies
# Message exchange
    # HTTP
# Describing the location, actions and target
    # URIs - Uniform Resource Identifier
    # HTTP Methods
# Representing the data
    # JSON - Most Commonly
    # XML or HTML - possibly, less frequent
# Describing the service
    # Swagger/OpenAPI

# HTTP and JSON support are widespread within programming languages
# True

# Which technology is widely used to share information about the way in which a REST API can be accessed?
# Swagger/OpenAPI

## REST Implementation
# What is CRUD
# CRUD describes how we often access data
# C= Create # Insert a new record into the data store (PUT or POST)
# R= Read # Read an existing record or records from the data store (GET)
# U= Update # Modify an existing record in the data store (PUT or PATCH)
# D= Delete # Remove an existing record from the data store (DELETE)

# REST API is often just CRUD using HTTP/JSON

# In a REST endpoint, collections are normally names with plural nouns.
# True

# What is the name given to the architectural constraint in REST which gives us links in the returned JSON document, allowing further data to be retrieved by following the links?
# Hypertext as the engine of application state
