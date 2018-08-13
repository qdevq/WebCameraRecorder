from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, "index.html")


@csrf_exempt
def upload_video(request):
    if request.method == 'POST':
        with open('test.webm', 'wb') as vf:
            video_stream = request.read()
            vf.write(video_stream)
    return JsonResponse({'status': 'OK'})


def last_video(request):
    with open('test.webm', 'rb') as vf:
        response = HttpResponse(vf.read())
    response['Content-Disposition'] = 'attachment; filename=test.webm'
    return response
