## Requirements

- Python `>= 3.7`
- Git
- Poetry (if the command line below doesn't work, see [here](https://python-poetry.org/docs/#installation)):

    === "For Linux / MacOS"

        ``` bash
        curl -sSL https://install.python-poetry.org | python3 -
        ```

    === "For Windows (Powershell)"

        ``` bash
        (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
        ```

- Cookiecutter (don't create a new environment, it will be done by poetry):

    === "With pip"

        ``` bash
        pip install cookiecutter
        ```

    === "With conda"

        ``` bash
        conda install cookiecutter
        ```

## Usage
!!! info
    After answering a few questions, the command line below creates a new folder with everything you need inside. Especially, it created a `README.md` file that helps you understand the package organization you just created.

Run the following command line to create a new project folder. Note that it will put everything inside a new folder, thus you don't have to `mkdir` first.
```bash
cookiecutter gh:MICS-Lab/poetry_cookiecutter
```