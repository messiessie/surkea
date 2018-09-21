# what_prefix = "“", what_suffix = "”"
# That bit of code makes the character's speech be preceded and followed by quotation marks. This
# is for convenience, so we don't have to do this ourselves for every line of dialogue we write. 

define debug = Character("Debug", who_color = "#ff00ff")

##########################################
##----------PRIMARY CHARACTERS----------##
##########################################

#Main character (not visible)
define kura = Character("Kura", what_prefix = "“", what_suffix = "”", who_color = "#a54d4d")

define oni = Character("Oni", what_prefix = "“", what_suffix = "”", image = "oni", who_color = "#ffb942")
define utagu = Character("Utagu", what_prefix = "“", what_suffix = "”", image = "utagu", who_color = "#4b42ff")
define kokoro = Character("Kokoro", what_prefix = "“", what_suffix = "”", image = "kokoro", who_color = "#bc4dba")

##########################################
##--------INCIDENTAL CHARACTERS---------##
##########################################

define maaj = Character("Maaj", what_prefix = "“", what_suffix = "”", who_color = "#40aaa2")


##########################################
##----------UTILITY CHARACTERS----------##
##########################################

# Not needed here.