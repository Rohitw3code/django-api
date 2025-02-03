from django.http import HttpResponse , JsonResponse



def home_page(request):
    print("home page requested")
    return JsonResponse({'a':1})
