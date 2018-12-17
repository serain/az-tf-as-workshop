import webbrowser
import glob
import os
from jinja2 import Environment


TEMPLATE = open('template/slideshow.html.j2').read()


sections = []

walked = os.walk('sections')
next(walked)

for folder in walked:
    files = folder[2]
    for _file in files:
        section = open(f'{folder[0]}/{_file}').read()
    
        if _file != '00-housekeeping.md' and not section.startswith('---'):
            section = '---\n' + section

        sections.append(section)


with open('slideshow.html', 'w+') as sfh:
    print(Environment().from_string(TEMPLATE).render(sections=sections), file=sfh)


# webbrowser.open('slideshow.html')
