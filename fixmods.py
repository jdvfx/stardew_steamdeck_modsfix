"""
-------------------------------------
Stardew Valley Mods fix for SteamDeck
-------------------------------------
"""

import glob
import re
import os

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



