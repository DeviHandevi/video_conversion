# Video Converter Web API
## Requirements
- Python 3.8
- Django
- Django REST Framework

## How to Run
``` bash
# Install dependencies
pipenv install

cd video_converter

# Apply the migrations for project app(s)
python manage.py migrate

# Serve on localhost:8000
python manage.py runserver
```

## How To
### Input
URL: `http://127.0.0.1:8000/video_converter_app/` (POST)

Input parameters:
- `file`: binary file (e.g. 'input.mp4')
- `format`: (optional) video output format (e.g. webm, matroska, avi)
- `preset`: (optional) compression (e.g. ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow, placebo)
- `crf`: (optional) Constant Rate Factor. The range of the CRF scale is 0–51, where 0 is lossless, 23 is the default, and 51 is worst quality possible. (e.g. 0, 23, 51)

Reference: https://trac.ffmpeg.org/wiki/Encode/H.264#:~:text=preset%20and%20tune-,Preset,compression%20is%20quality%20per%20filesize)

### Output
```bin
Eߣ�B��B��B�B�B��matroskaB��B��S�g�������M�t���E��M��S��I�fS���M��S��T�kS���M��S��T�gS��B�bI�f���Mٰ�*ױ�B@M��Lavf58.64.100WA�Lavf58.64.100s��/�d��@O�ށ)^$V�T�kPV���߾@��ׁsň*"�+�Ia���"���und��V_MPEG4/ISO/AVC��#ツ
...
```

### Notes
- The API receives binary file video and three preset parameters
- Multiple requests do not pauses one another

## Thanks To
- https://pypi.org/project/ffmpeg-python/
- https://trac.ffmpeg.org/wiki/Encode/H.264
