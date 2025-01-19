
import json 

from  django.http import JsonResponse


def api_home(request , *args , **kwargs): # this params request is a instance of Httprequests from django

    body = request.body #byte string of json data 
    data = {}
    try :
        data = json.loads(body) #takes a string of jason data and turns into a python dict 

    except : ## the reason behinde the try is bloc is that it is possible that the body its not a contains a json  

        pass

    print(data.keys)
    
    #data['headers'] = request.headers # back then was request.META
    data['headers'] = dict(request.headers  )
    data['content_type']= request.content_type
    data['params'] = dict(request.GET)
    print(request.headers)
    return JsonResponse(data)
    

