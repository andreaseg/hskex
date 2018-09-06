import os
import re

regex = re.compile('\s*\[code\]\[(.+)\]\((.+)\)')
regex_lines = re.compile('\s*\[code\]\[(.+)\]\((.+)\)\[\s*lines\s*=\s*(\d+)\s*-\s*(\d+)\s*\]')
for file in os.listdir("./"):
    if file.endswith(".md"):
        r = open(file, "r")
        if not os.path.exists("target"):
            os.makedirs("target")
        w = open("target/" + file, "w")
        for line in r:
            m = regex_lines.match(line)
            if m:
                if os.path.isfile(m.group(2)):
                    f = open(m.group(2), "r")
                    w.write("```" + m.group(1) + "\n")
                    for i, line in enumerate(f):
                        if i + 1 >= int(m.group(3)) and i < int(m.group(4)):
                            w.write(line)
                    w.write("\n```\n")
                    f.close()
                else:
                    w.write("Missing file: " + m.group(2) + "\n")
                continue
            m = regex.match(line)
            if m:
                if os.path.isfile(m.group(2)):
                    f = open(m.group(2), "r")
                    w.write("```" + m.group(1) + "\n")
                    for line in f:
                        w.write(line)
                    w.write("\n```\n")
                    f.close()
                else:
                    w.write("Missing file: " + m.group(2) + "\n")
            else:
                w.write(line)
        r.close()
        w.close()
        