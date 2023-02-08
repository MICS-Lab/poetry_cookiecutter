Poetry is a package and dependency manager. It creates an environment that is associated with your project.

Everything is detailed in [their doc](https://python-poetry.org/docs/basic-usage/), but here we help you get started. 

## Basic command lines

!!! note
    If you are inside your project, Poetry will automatically detect it. Thus, you don't have to activate your environment to run the commands below.

```bash
poetry add pandas # Add pandas as a dependency
poetry add mkdocs --dev # Add mkdocs as a dev dependency (i.e. not needed to use the package)
poetry remove pandas # Remove pandas
poetry shell # Activate the environment
poetry init # Helps you create pyproject.toml, if not done yet
poetry show # List all the available packages
poetry show pandas # See the details of a particular package (e.g., its dependencies or its version)
poetry install # Install all the project dependencies (if not done yet)
poetry update # Get the latest version of your dependencies
```

## Activate the poetry environment

To activate your new poetry environment, you can choose one of the following:

- Choose the installed poetry interpreter on Visual Studio Code (it activates your env automatically at each new terminal window). If you didn't provide VS Code the path to poetry virtualenvs, add `"python.venvPath": <path>` in your VS Code user settings file, where `path` is the output of the following command line: `poetry config virtualenvs.path`
- At the root of the project, run `poetry shell`.
- Use `poetry run` before each command line, e.g. `poetry run python your_script.py`

!!! important
    All the command lines in this documentation assume that you have activated your environment using one of these methods. E.g., instead of telling you to run `poetry run mkdocs serve`, we simply say `mkdocs serve` (note that you need to add `poetry run` in front of the command only if you have chosen the third option).

## Install your package on other environments

You can install your package on other environments. Activate your environment, then move to the project's root and run `pip install -e .` to install it with the editable mode. Now, you can import your package when running on this new environment, and it will always consider your code changes thanks to the editable mode (no need to reinstall the package).

## Details on `pyproject.toml` and `poetry.lock`

At the root of your directory is a file called `pyproject.toml`. As written [here](https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/), "modern Python packages can contain a pyproject.toml file, first introduced in PEP 518 and later expanded in PEP 517, PEP 621 and PEP 660. This file contains build system requirements and information, which are used by pip to build the package".

Poetry uses this file, and has its own specific group under `[tool.poetry]`. For instance, the dependencies are listed under `[tool.poetry.dev-dependencies]`.

The `poetry.lock` file contains information about your dependencies and the correct versions that solve the conflicts. It can be great to commit it to version control so that everyone uses identical package versions.