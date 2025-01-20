
import json  # to change the data from json to python dict 
from product.models import Product

from  django.http import JsonResponse


def api_home(request , *args , **kwargs): # this params request is a instance of Httprequests from django

    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data : 
        data['id'] = model_data.id
        data['title'] = model_data.title
        data['content'] = model_data.content 
        data['price'] = model_data.price
        """we will do the serialization means
        1/ model instance 
         2/ trun it to py dict 
          3/ return json to my client  """
    return JsonResponse(data)