## Requirements

- [x] Python `>= 3.7`
- [x] Git
- [x] Poetry (if the command lines below don't work, see [here](https://python-poetry.org/docs/#installation)):

    === "For Linux / MacOS"

        ``` bash
        curl -sSL https://install.python-poetry.org | python3 -
        ```

    === "For Windows (Powershell)"

        ``` bash
        (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
        ```

- [x] Cookiecutter:

    === "With pip"

        ``` bash
        pip install cookiecutter
        ```

    === "With conda"

        ``` bash
        conda install cookiecutter
        ```

## Usage

Run the following command line to create a new project folder:
```bash
cookiecutter gh:MICS-Lab/poetry_cookiecutter
```
!!! info
    After answering a few questions, it creates a new folder with everything you need inside. Especially, it created a `README.md` file that helps you understand the package organization you just created.