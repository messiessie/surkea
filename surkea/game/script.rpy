default persistent.kokoroClear = False
default persistent.utaguClear = False
default persistent.allClear = False

# The game starts here.
label start:

    call S_01_C from _call_S_01_C

    return

label splashscreen:
  image white = Solid("#fff")
  scene black
  $ renpy.pause(1)
  $ renpy.movie_cutscene("video/Somnova_Intro.webm")
  show movie
  play movie "video/Somnova_Intro.webm"
  $ persistent.loaded = False