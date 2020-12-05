import ffmpeg
import numpy as np

input_filepath = 'D:/Downloads/input.mp4'
output_filepath = 'D:/Downloads/output.avi'

# stream = ffmpeg.input('./input.mp4')
# stream = ffmpeg.output(stream, './output.avi')
# ffmpeg.run(stream)

# try:
#   stream = ffmpeg.input(input_filepath)
#   stream = ffmpeg.output(stream, output_filepath)
#   ffmpeg.run(stream)
# except ffmpeg.Error as e:
#   print(e.stderr)

# try:
#   out, _ = (
#     ffmpeg
#     .input(input_filepath)
#     .output('pipe:', format='rawvideo', pix_fmt='rgb24')
#     .run(capture_stdout=True)
#   )
#   video = (
#     np
#     .frombuffer(out, np.uint8)
#   )
#   print(video)
# except ffmpeg.Error as e:
#   print(e.stderr)

try:
  converted_video_binary, _ = (
    ffmpeg
    .input(input_filepath)
    .output('pipe:', format='h264')
    .run(capture_stdout=True)
  )
  print(converted_video_binary)
except ffmpeg.Error as e:
  print(e.stderr)