# {{cookiecutter.project_name}}
{{cookiecutter.description}}

> This project has been generated by cookicutter from [this template](https://github.com/MICS-Lab/poetry_cookiecutter).
# Template usage instructions
## Activate the poetry environment

To activate your new poetry environment, you can choose one of the following:
- Choose the installed poetry interpreter on VSCode (it activates your env automatically at each new terminal window). If you didn't provided to VS Code the path to poetry virtualenvs, add `"python.venvPath": <path>` in your VS Code user settings file, where `path` is the output of the following command line: `poetry config virtualenvs.path`
- At the root of the project, run `poetry shell`.
- Use `poetry run` before each command line, e.g. `poetry run python your_script.py`

## Run the documentation locally

`mkdocs serve`

## Deploy the doc
To deploy the documentation on Github Pages, you need first to push your changes on the `master` branch.
Then, go to the github settings, and choose `gh-pages` as the branch, and `/docs` as the folder. It will create a link so that you can access the doc online.

NB: the default CI is set up to deploy pages when pushing to `master`, but you can update the `.github/workflows/ci.yml` file.

## Run tests

`pytest`

## Package installation
You can install your package on other environments. Simply move to the root of this project, and run `pip install -e .` to install it with the editable mode. Now, you can import your package when running on this new environment, and it will always consider your code changes thanks to the editable mode (no need to reinstall the package).