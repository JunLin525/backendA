from django.http import JsonResponse

def getRoutes(request):
    routes =[
        'api/token',
        'api/token/refresh',
    ]
    return JsonResponse(router, safe=False)