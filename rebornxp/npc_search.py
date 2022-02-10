def npc_id_and_name(file_name):
    with open(file_name) as npcs1:
        all_npcs = {}
        all_lines = npcs1.readlines()
        for line in all_lines:
            if "<npc" in line:
                line_parts = line.split('"')
                id = line_parts[1]
                name = line_parts[3].lower()
                all_npcs[name] = id
    return all_npcs

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir("../npcs/") if isfile(join("../npcs/", f))]
npcs = {}
for file in onlyfiles:
    file_npcs = npc_id_and_name(f"../npcs/{file}")
    npcs = {**npcs, **file_npcs}

print(npcs.get("wolf".lower()))

