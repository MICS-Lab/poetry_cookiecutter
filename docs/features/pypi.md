Publishing on [PyPI](https://pypi.org/) is very easy with Poetry. If needed, everything is detailed [here](https://python-poetry.org/docs/libraries/#packaging) in their documentation.

!!! note
    Before publishing a new version of your package, we advise you to ensure all your tests run properly.

## Configure your PyPI account

This step has to be done only once.

- Create an account on [PyPI](https://pypi.org/).
- Configure your PyPI credentials as written [here](https://python-poetry.org/docs/repositories/#configuring-credentials).

## (Optional) Setting a new version and release

- Update the `version` attribute under the `[tool.poetry]` group of your `pyproject.toml` file to set a new version, e.g. `version = "1.3.2"`
- Create a new tag associated with this version on GitHub (for the tag name, we advise adding a `v` before the version):
```bash
git tag <tagname> # create a tag, e.g. v1.3.2
git push origin <tagname> # push a tag to remote
```
- On the GitHub interface, go to the "Release" section of your repository and "Draft a new release" (choose the tag defined above).

## Publish on PyPI

!!! note
    If you already published on PyPI: you should make a new version, i.e. at least change the `version` in your `pyproject.toml` file, as written above.

```bash
poetry publish --build
```