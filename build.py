# build.py

import os
from jinja2 import Environment, FileSystemLoader

TEMPLATE_PATH_NAME = "templates"
OUTPUT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'versions')
SRC_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src')
TEMPLATE_PATH = os.path.join(SRC_PATH, TEMPLATE_PATH_NAME)

template_env = Environment(
    autoescape=False,
    loader=FileSystemLoader(SRC_PATH),
    trim_blocks=False)

templates = os.listdir(TEMPLATE_PATH)

for template_name in templates:
    template = template_env.get_template(os.path.join(TEMPLATE_PATH_NAME, template_name))

    output_file = open(os.path.join(OUTPUT_PATH, template_name), "w")
    output_file.write(template.render({}))
    output_file.close()