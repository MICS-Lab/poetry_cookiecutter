# Poetry Cookiecutter

This repository eases the creation of a new Python package. Using [`cookiecutter`](https://cookiecutter.readthedocs.io/en/stable/index.html), it will copy the project template and personalize it according to the answers to a few questions (e.g. the project name) so that you can get started quickly.

## Features
- Easy dependency management with [`Poetry`](https://python-poetry.org/).
- Pretty documentation with [`Mkdocs material`](https://squidfunk.github.io/mkdocs-material/).
- Package installable on any local environment (package structure).
- Deployment on [`PyPI`](https://pypi.org/) in a few seconds, if needed.
- Tests with [`pytest`](https://docs.pytest.org/en/7.1.x/).
- Formatting with [`black`](https://github.com/psf/black).
- Standardised project organization (`data` folder, `config` folder, ...).

## Template usage

### Cookiecutter installation
If not done yet, install `cookiecutter` using one of the following command lines:

```bash
pip install cookiecutter     # install with pip
conda install cookiecutter   # install with conda
```

### Get the template
Run the following command line to create a new project folder:
```bash
cookiecutter gh:MICS-Lab/poetry_cookiecutter
```
After answering a few questions, it creates a new folder with everything you need inside.
Especially, it created a `README.md` file that helps you understand the package organization you just created.