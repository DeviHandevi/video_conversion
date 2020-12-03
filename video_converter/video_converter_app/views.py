from django.shortcuts import render
from django.http import HttpResponse

import ffmpeg
import numpy as np


# Create your views here.
def index(request):
  if request.method == 'POST':
    return HttpResponse("Converted")
  else:
    try:
      input_filepath = 'D:/Downloads/input.mp4'
      converted_video_binary, _ = (
        ffmpeg
        .input(input_filepath)
        .output('pipe:', format='matroska')
        .run(capture_stdout=True)
      )
      return HttpResponse(converted_video_binary, content_type='video/x-matroska')
    except ffmpeg.Error as e:
      print(e.stderr)
  return HttpResponse("NON POST")