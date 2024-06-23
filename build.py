from pathlib import Path
import shutil
from jinja2 import Environment, FileSystemLoader

templates = ['index.html', 'hits.html']


def build(templates=templates, outdir='dist/www', static='static'):
    Path(outdir).mkdir(parents=True, exist_ok=True)
    j_env = Environment(loader=FileSystemLoader(searchpath="./templates"))

    for template in templates:
        rendered = j_env.get_template(str(template)).render()
        with open(Path('.').joinpath(outdir, template), 'w') as f:
            f.writelines(rendered)


    if static:
       shutil.copytree(
           Path('.').joinpath(static),
           Path('.').joinpath(outdir, static),
           dirs_exist_ok=True
       )


build()
