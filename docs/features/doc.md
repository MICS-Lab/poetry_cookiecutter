## Serve locally
The documentation can be served locally with `mkdocs serve`. It will be reloaded each time you save a file.

## Basic usage

We explain briefly how to use and update the documentation. For more details, read about [Mkdocs Material](https://squidfunk.github.io/mkdocs-material/creating-your-site/).


### Docs folder
`docs` is the folder containg all the documentation pages. Each page is either a markdown (`.md`) file or a notebook (`.ipynb`) file.

The markdown files can also be in subdirectories. 

!!! note
    Once you added a new file, don't forget to add it in the `nav` so that it becomes accessible (see "Config file" below).

### Config file

`mkdocs.yml` is the config file for the documentation. Inside `nav`, one can add new pages. For instance:

```yaml
nav:
  - Home: index.md
  - Getting Started: getting_started.md
  - Tutorials:
    - tutorials/preprocessing.ipynb
    - tutorials/training.ipynb
```

### Writing math

You can write some formulas in Latex. You can use the inlince syntax (`$...$` or `\(...\)`) or the block syntax on separate lines (`$$...$$` or `\[...\]`).

For instance, `$f_2(x) \in \mathbb{R}$` makes $f_2(x) \in \mathbb{R}$.

### Automatic API

If you added dosctrings to your code, you can make automatically a nice API of your package. For that, add **` ::: <package>.<f>`** in one of your `.md` file, where `<package>` is your package name, and `<f>` is a function/method/class to be documented.

This is an doctsring example:

```python
from typing import List, Dict, Callable, Optional

def apply_dict_values(names: List[str], fun: Callable, alpha: Optional[int] = 1) -> Dict[str, str]:
    """Applies a function to all names. The function outputs are returned as values of a dictionary (whose keys are names).

    Args:
        names: A list of names.
        fun: A function to be applied to each name.
        alpha: Second argument of `fun`.

    Returns:
        A dictionnary whose keys are names and values are the result of the function.
    """
    return {name: fun(name, alpha) for name in names}
```

Options can be added, for instance:
```md
::: <package>.<f>
    options:
      show_root_heading: true
```

For more details, see [Mkdocstrings](https://mkdocstrings.github.io/).

## Deploy on Github pages

To deploy the documentation on Github Pages, you need first to push your changes on the `master` branch.
Then, go to the github settings, and choose `gh-pages` as the branch, and `/docs` as the folder. It will create a link so that you can access the doc online.

!!! note
    The default CI is set up to deploy pages when pushing to `master`, but you can update the `.github/workflows/ci.yml` file.