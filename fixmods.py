import glob
import re
import os

"""
-------------------------------------
Stardew Valley Mods fix for SteamDeck
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

"""

files_renamed = 0

for old_path in glob.glob("**/*.png", recursive = True):

    file_name = os.path.basename(old_path)
    file_name_lower = file_name.lower()
    new_path = re.sub(file_name,file_name_lower,old_path)

    if new_path != old_path and os.path.exists(new_path) == False:
            command = f'mv "{old_path}" "{new_path}"'
            os.system(command)
            print(command)
            files_renamed+=1

print("\n>>> DONE <<<")
if files_renamed>0:
    print(f"{files_renamed} files renamed")
else:
    print("no files need renaming")



