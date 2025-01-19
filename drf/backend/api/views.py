from  django.http import JsonResponse


def api_home(requests  , *args , **kwargs):
    return JsonResponse({"message" : " HI THERE ITS yassine api's "})


