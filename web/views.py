from django.shortcuts import render, redirect
from web.models import ShortenedURL


def shorten(request):
    context = {}
    if request.POST:
        ShortenedURL.objects.create(original=request.POST['original'], shortened='https://www.payperks.com')
        context = {
            'message': 'Your shortened URL is %s. Have Fun!'
        }

    return render(request, 'web/index.html', context)


def go(request):
    return redirect('https://www.payperks.com')