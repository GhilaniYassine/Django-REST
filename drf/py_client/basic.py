import requests 

endpoint= " http://127.0.0.1:8000/api/" # if you are not running  the server with the commande pyhton manage.py runserver you want get response from this particulare endpoint 
#endpoint_google = "https://www.google.com/search?q=google+currency+converter&oq=google+curre&gs_lcrp=EgZjaHJvbWUqDAgAEAAYRhiCAhiABDIMCAAQABhGGIICGIAEMgYIARBFGDkyBwgCEAAYgAQyBwgDEAAYgAQyBwgEEAAYgAQyBwgFEAAYgAQyBwgGEAAYgAQyBwgHEAAYgAQyBwgIEAAYgAQyBwgJEAAYgATSAQgzNDk2ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8"

get_response = requests.get(endpoint , params= {"abc" : 123} , json = {"query" : " hello world!"})

#print(get_response.text) #the raw text response the html
print(get_response.json() ) # to get only the message as json similar to the python dict 

#print(get_response.status_code)


 ## echo things form a given  somthing 