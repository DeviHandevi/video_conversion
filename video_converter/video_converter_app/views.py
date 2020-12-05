from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse

import ffmpeg
import numpy as np

from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@api_view(['POST'])
@csrf_exempt
def index(request):
  try:
    # Get file
    request_file = request.FILES['file']
    file_path = request_file.temporary_file_path()

    # Get three user defined presets
    presets = {}
    p_format = request.data.get('format', False)
    if p_format:
      presets['format'] = p_format

    p_preset = request.data.get('preset', False)
    if p_preset:
      presets['preset'] = p_preset
      
    p_crf = request.data.get('crf', False)
    if p_crf:
      presets['crf'] = p_crf

    # Convert video using the presets
    converted_video_binary, _ = (
      ffmpeg
      .input(file_path)
      .output('pipe:', **presets)
      .run(capture_stdout=True)
    )
    return HttpResponse(converted_video_binary)
  except ffmpeg.Error as e:
    return Response(e.stderr)
