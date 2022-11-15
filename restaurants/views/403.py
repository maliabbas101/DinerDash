from django.shortcuts import render


def error_403(request, exception):
    print(request.GET)
    return render(request, '403.html')
