-------------------------------------
# Stardew Valley Mods fix for SteamDeck
-------------------------------------

**What's the issue?**<br>
    Some mods do no work out of the box.<br>
    The issue is the Uppercase on the filenames<br>
    That's only a problem on Linux where files names are case sensitive<br>
    eg: ```Texture_1.png``` instead ```texture_1.png```<br>
    
**What's the fix?**<br>
    this scripts finds all the PNG textures<br>
    and renames them to lowercase<br>

**Usage:**<br>
    First, backup your Mods folder, just in case.<br>
    Copy this python script in your Stardew Valley "Mods" folder<br>
    Then in a terminal: ```python fixmods.py```<br>

