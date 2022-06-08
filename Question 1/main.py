import re
import os


def file_string_change(filename: str, old_string: str, new_string: str):
    with open(filename) as f:
        s = f.read()
        s = re.sub(old_string, new_string, s)

    with open(filename, 'w') as f:
        f.write(s)


file_string_change('autoexec.cfg', 'bind \"a\" \"mc_attack\"', 'bind "s" "mc_attack"')
file_string_change('autoexec.cfg', 'bind \"s\" \"dota_stop\"', 'bind "n" "dota_stop"')

os.startfile('C:\\Program Files (x86)\\Steam\\steam.exe')
