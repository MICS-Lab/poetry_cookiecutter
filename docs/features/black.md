Formatting is run with [`black`](https://github.com/psf/black). As written in their doc, Black gives you speed, determinism, and freedom from pycodestyle nagging about formatting. You will save time and mental energy for more important matters.

Blackened code looks the same regardless of the project you're reading. Formatting becomes transparent after a while and you can focus on the content instead.

Black makes code review faster by producing the smallest diffs possible.

## Using Black with the command line

At the project's root, you can run the command line below to format all your code.
```bash
black .
```

## Format on save
The best option is to format your code on save so that you don't have to think about executing Black anymore.

!!! note
    After configuring the format on save, it will run Black on your current file each time you save it.

### On Visual Studio Code
Make sure you have the Python extension (from Microsoft). Then, open your settings (__Code -> Preferences -> Settings__) and update the following:

- Choose black as the provider (search for `Python › Formatting: Provider`)
- Enable formatting on save (search for `Editor: Format On Save`).

## Update the settings

Black settings can be found in `pyproject.toml` under `[tool.black]`.
