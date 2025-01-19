import requests 

endpoint= " http://127.0.0.1:8000/api/" # if you are not running  the server with the commande pyhton manage.py runserver you want get response from this particulare endpoint 


get_response = requests.get(endpoint)

print(get_response.text) #the raw text response the html
print(get_response.json()['message']) # to get only the message as json similar to the python dict 

print(get_response.status_code)


