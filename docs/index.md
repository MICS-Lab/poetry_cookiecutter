This repository eases the creation of a new Python package. Using [`cookiecutter`](https://cookiecutter.readthedocs.io/en/stable/index.html), it will copy the project template and personalize it according to the answers to a few questions (e.g. the project name) so that you can get started quickly.

## Features
- Easy dependency management with [`Poetry`](https://python-poetry.org/).
- Pretty documentation with [`Mkdocs material`](https://squidfunk.github.io/mkdocs-material/).
- Package installable on any local environment (package structure).
- Deployment on [`PyPI`](https://pypi.org/) in a few seconds, if needed.
- Tests with [`pytest`](https://docs.pytest.org/en/7.1.x/).
- Formatting with [`black`](https://github.com/psf/black).
- Standardised project organization (`data` folder, `config` folder, ...).

## Project structure

```txt
.
|-- LICENSE
|-- README.md
|-- config             # where you store config files
|-- data               # where you store your data
|-- docs               # your documentation
|   |-- index.md
|   `-- ...
|-- mkdocs.yml         # documentation config
|-- poetry.lock        # poetry related file (do not update)
|-- <your-module-name> # folder containing your code
|   |-- __init__.py
|   `-- ...
|-- pyproject.toml     # project dependency settings and config
|-- setup.py           # setup file to pip install the project
`-- tests              # folder to write your package tests
    `-- test_instance.py
```