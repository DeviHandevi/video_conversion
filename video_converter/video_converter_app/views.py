from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse

import ffmpeg
import numpy as np

from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

# def handle_uploaded_file(f):
#   with open('some/file/name.txt', 'wb+') as destination:
#     for chunk in f.chunks():
#       destination.write(chunk)
#   return 

# Create your views here.
@api_view(['POST'])
@csrf_exempt
def index(request):
  try:
    request_file = request.FILES['file']
    file_path = request_file.temporary_file_path()

    converted_video_binary, _ = (
      ffmpeg
      .input(file_path)
      .output('pipe:', **{
        'format': 'matroska',
        'pix_fmt': 'rgb24',
        'vframes': 100,
      })
      .run(capture_stdout=True)
    )
    # converted_video_binary, _ = (
    #   ffmpeg
    #   .input(file_path)
    #   .output('pipe:', format='matroska')
    #   .run(capture_stdout=True)
    # )
    # return Response(type(converted_video_binary).__name__)
    return HttpResponse(converted_video_binary)
  except ffmpeg.Error as e:
    return Response(e.stderr)
