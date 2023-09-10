-------------------------------------
# Stardew Valley Mods fix for SteamDeck
-------------------------------------

> what's the issue?
    some mods do no work out of the box
    the issue is the Uppercase on the filenames
    that's only a problem on Linux
    eg: "Texture_1.png" instead "texture_1.png"
    
> what's the fix?
    this scripts finds all the PNG textures
    and renames them to lowercase

> usage:
    copy this python script in your Stardew Valley "Mods" folder
    then in a terminal: python fixmods.py

