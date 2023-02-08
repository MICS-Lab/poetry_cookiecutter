# Poetry Cookiecutter

This repository eases the creation of a new Python package. Using [`cookiecutter`](https://cookiecutter.readthedocs.io/en/stable/index.html), it will copy the project template and personalize it according to the answers to a few questions (e.g. the project name) so that you can get started quickly.

## Documentation

All the requirements and features are described in the [documentation](https://mics-lab.github.io/poetry_cookiecutter/).

## Features
- Easy dependency management with [`Poetry`](https://python-poetry.org/).
- Pretty documentation with [`Mkdocs material`](https://squidfunk.github.io/mkdocs-material/).
- Package installable on any local environment (package structure).
- Deployment on [`PyPI`](https://pypi.org/) in a few seconds, if needed.
- Tests with [`pytest`](https://docs.pytest.org/en/7.1.x/).
- Formatting with [`black`](https://github.com/psf/black).
- Standardized project organization (`data` folder, `config` folder, ...).

## Requirements
First, ensure you have Python installed (version `>= 3.7`) and Git. Next, install `PyPoetry` and `cookiecutter` (if not done yet):
### Poetry installation

The official installer can be found below (for Linux, macOS, or Windows WSL users):

```
curl -sSL https://install.python-poetry.org | python3 -
```

If you use Windows without WSL, or if the above command line was not working, choose another installer [(see their documentation)](https://python-poetry.org/docs/#installation).

### Cookiecutter installation
Install `cookiecutter` using one of the following command lines:

```bash
pip install cookiecutter     # install with pip
conda install cookiecutter   # install with conda
```

## Usage

Run the following command line to create a new project folder:
```bash
cookiecutter gh:MICS-Lab/poetry_cookiecutter
```
After answering a few questions, it creates a new folder with everything you need inside.