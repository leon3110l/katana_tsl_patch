from pathlib import Path
import re
import os

regex = re.compile("class (.*)\(.*\):")

for path in Path(os.path.dirname(__file__)).glob("*.py"):
    # print(path.name)
    with open(path) as file:
        match = regex.findall(file.read())
        print('from .' + path.name.replace(".py", "") + ' import ' + ', '.join(match))