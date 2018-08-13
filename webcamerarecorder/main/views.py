from django.shortcuts import render
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
