# build.py

import os
from jinja2 import Environment, FileSystemLoader

LOCAL_PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_PATH = os.path.join(LOCAL_PATH, 'src/templates')
INCLUDE_PATH = os.path.join(LOCAL_PATH, 'src/includes')
DIST_PATH = os.path.join(LOCAL_PATH, 'dist')

template_env = Environment(
    autoescape=False,
    loader=FileSystemLoader(TEMPLATE_PATH),
    trim_blocks=False)

templates = os.listdir(TEMPLATE_PATH)

for template in templates:
    print(template_env.get_template(template).render({"var_name": "This is my var name"}))