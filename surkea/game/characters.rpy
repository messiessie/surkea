# what_prefix = "“", what_suffix = "”"
# That bit of code makes the character's speech be preceded and followed by quotation marks. This
# is for convenience, so we don't have to do this ourselves for every line of dialogue we write. 

define debug = Character("Debug", who_color = "#ff00ff")

##########################################
##----------PRIMARY CHARACTERS----------##
##########################################

define kura = Character("Kura", what_prefix = "“", what_suffix = "”", image = "kura", who_color = "#a54d4d")
define oni = Character("Oni", what_prefix = "“", what_suffix = "”", image = "oni", who_color = "#e8760b")
define utagu = Character("Utagu", what_prefix = "“", what_suffix = "”", image = "utagu", who_color = "#4b42ff")
define kokoro = Character("Kokoro", what_prefix = "“", what_suffix = "”", image = "kokoro", who_color = "#bc4dba")

##########################################
##--------INCIDENTAL CHARACTERS---------##
##########################################

# Meant for non-sprited characters.

define maaj = Character("Maaj", what_prefix = "“", what_suffix = "”", who_color = "#40aaa2")

##########################################
##----------UTILITY CHARACTERS----------##
##########################################

# Meant for characters that haven't been introduced, e.g. "Strange Girl"
# Normally replaced in-script by the actual character.