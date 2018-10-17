from django.http import HttpResponse, HttpRequest

def reverse(request):
    if request.method == 'POST':
        return HttpResponse("Well well well, It's getting better")

    return HttpResponse("Failed :'(")
