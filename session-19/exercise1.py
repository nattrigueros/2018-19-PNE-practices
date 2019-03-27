import http.client
import json

# -- API information
HOSTNAME = "api.icndb.com"
ENDPOINT = "/jokes/random"
METHOD = "GET"

# -- Here we can define special headers if needed
headers = {'User-Agent': 'http-client'}

# -- Connect to the server
# -- NOTICE it is an HTTPS connection!
# -- If we do not specify the port, the standar one
# -- will be used
conn = http.client.HTTPConnection(HOSTNAME)   # CODE FOR GETTING THE RANDOM JOKE

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT, None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()

# -- Print the status
print()
print("Response received: ", end='')
print(r1.status, r1.reason)

# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
conn.close()

# -- Optionally you can print the
# -- received json file for testing
# print(text_json)

# -- Generate the object from the json file
joke = json.loads(text_json)

# -- Print the received URL
print("RANDOM JOKE: ", joke['value']['joke'])  # ENTER IN THE DICTIONARY TO GET THE RANDOM JOKE

ENDPOINT = '/jokes/count'  # REDEFINE THE ENDPOINT TO CHANGE THE THING WE WANT

conn = http.client.HTTPConnection(HOSTNAME)   # THIS IS THE CODE FOR THE NUMBER OF JOKES

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT, None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()

# -- Print the status
print()
print("Response received: ", end='')
print(r1.status, r1.reason)

# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
conn.close()

# -- Optionally you can print the
# -- received json file for testing
# print(text_json)

# -- Generate the object from the json file
number = json.loads(text_json)

print("THE NUMBER OF JOKES: ", number['value'])

ENDPOINT = '/categories'  # REDEFINE THE ENDPOINT TO CHANGE THE THING WE WANT

conn = http.client.HTTPConnection(HOSTNAME)   # THIS IS THE CODE FOR THE NUMBER OF JOKES

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT, None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()

# -- Print the status
print()
print("Response received: ", end='')
print(r1.status, r1.reason)

# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
conn.close()

# -- Optionally you can print the
# -- received json file for testing
# print(text_json)

# -- Generate the object from the json file
categories = json.loads(text_json)

print("THE NUMBER OF CATEGORIES IS: ", len(categories['value']), '\n')  # THE LENGTH OF THE LIST IS GOING TO BE TH NUMBER OF CATEGORIES

for i in categories['value']:  # INDEX THE ELEMENTS OF THE LIST AND PRINT THE ELEMENTS, WHICH ARE GOING TO BE THE DIFFERENT CATEGORIES
    print('CATEGORY:', i)