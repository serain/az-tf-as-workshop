import glob
import os
from jinja2 import Environment


TEMPLATE = open('template/slideshow.html.j2').read()


sections = []
walked = sorted(list(os.walk('sections')), key=lambda tup: tup[0])

for folder in walked:
    files = folder[2]
    for _file in sorted(files):
        section = open(f'{folder[0]}/{_file}').read()
        print(folder[0], _file)
    
        if _file != '00-housekeeping.md' and not section.startswith('---'):
            section = '---\n' + section

        sections.append(section)


with open('slideshow.html', 'w+') as sfh:
    print(Environment().from_string(TEMPLATE).render(sections=sections), file=sfh)
