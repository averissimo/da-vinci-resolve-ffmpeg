from subprocess import run
from os import mkdir, path, remove

extensions = ['mp4', 'mov']

audio = [
  { "codec": 'pcm_s16le', "options": '', "skip": ['mp4'] },
  { "codec": 'pcm_u16le', "options": '', "skip": ['mp4', 'mov'] },
  { "codec": 'pcm_s24le', "options": '', "skip": ['mp4'] },
  { "codec": 'pcm_s24le', "options": '', "skip": ['mp4'] },
  { "codec": 'pcm_s32le', "options": '', "skip": ['mp4'] },
  { "codec": 'pcm_u32le', "options": '', "skip": ['mp4', 'mov'] },
  { "codec": 'pcm_f32le', "options": '', "skip": ['mp4'] },
  { "codec": 'pcm_s64le', "options": '', "skip": ['mp4'] },
  { "codec": 'pcm_f64le', "options": '', "skip": ['mp4'] },

  { "codec": 'pcm_s16be', "options": '', "skip": ['mp4'] },
  { "codec": 'pcm_u16be', "options": '', "skip": ['mp4', 'mov'] },
  { "codec": 'pcm_s24be', "options": '', "skip": ['mp4'] },
  { "codec": 'pcm_s24be', "options": '', "skip": ['mp4'] },
  { "codec": 'pcm_s32be', "options": '', "skip": ['mp4'] },
  { "codec": 'pcm_u32be', "options": '', "skip": ['mp4', 'mov'] },
  { "codec": 'pcm_f32be', "options": '', "skip": ['mp4'] },
  { "codec": 'pcm_s64be', "options": '', "skip": ['mp4', 'mov'] },
  { "codec": 'pcm_f64be', "options": '', "skip": ['mp4'] },

  { "codec": 'pcm_mulaw', "options": '', "skip": ['mp4'] },
  { "codec": 'pcm_alaw', "options": '', "skip": ['mp4'] },

  { "codec": 'flac', "mp4": '-strict -2', "options": '', "skip": ['mov']},

  { "codec": 'ac3', "options": '', "skip": [] },
  { "codec": 'aac', "options": '', "skip": [] },
  { "codec": 'libopus', "options": '', "skip": ['mov'] },
  { "codec": 'libvorbis', "options": '', "skip": [] },
  { "codec": 'libmp3lame', "options": '', "skip": [] },
  { "codec": 'libtwolame', "options": '', "skip": [] },
  { "codec": 'sonicls', "options": '-strict -2', "skip": ['mp4'] },
  { "codec": 'mp2', "options": '', "skip": [] }
]

video = [
  { "codec": 'dnxhd', "options": '-profile dnxhr_hq', "skip": ['mp4']},
  { "codec": 'prores_ks', "options": '-profile:v 3 -qscale:v 9 -vendor ap10 -pix_fmt yuv422p10le', "skip": ['mp4']},
  { "codec": 'libvpx-vp9', "options": '-crf 25 -b:v 0', 'skip': ['mov']},
  { "codec": 'libx264', "options": ''},
  { "codec": 'libx265', "options": ''},
  { "codec": 'mpeg4', "options": '-qscale:v 1'}
]

try:
  mkdir('output')
  print('output directory created')
except OSError as error:
  print('output directory already exists')

for ext in extensions:
  try:
    mkdir(path.join('output', ext))
  except OSError as error:
    continue

for ext in extensions:
  for el in video:
    if 'skip' in el.keys() and ext in el['skip']:
      continue
    for el2 in audio:
      if 'skip' in el2.keys() and ext in el2['skip']:
        continue
      print("")
      filename = el['codec'] + "-" + el2['codec'] + "." + ext
      filepath = path.join('output', ext, filename)
      additional_options = ''
      if (ext in el2.keys()):
        additional_options = additional_options + ' ' + el2[ext]
      mycmd = "ffmpeg -loglevel info -y -i trim.mp4 -t 00:00:03 -c:v {} {} -c:a {} {} {} {}".format(el['codec'], el['options'], el2['codec'], el2['options'], additional_options, filepath)
      print("$ " + mycmd)

      if path.isfile(filepath):
        print('("{}" exists... do nothing)'.format(filename))
      else:
        run(mycmd, shell = True)
      if path.getsize(filepath) == 0:
        print('  File size for ' + filename + ' is 0 bytes... Removing it')
        remove(filepath)
