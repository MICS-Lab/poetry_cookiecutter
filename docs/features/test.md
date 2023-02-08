Tests are run by [`pytest`](https://docs.pytest.org/en/7.2.x/).

## Implement new tests

Choose or add a new file into the `tests/` directory to make a new test. This filename should start with `test_` to be targeted by pytest.

Into each function of this test file, you can run multiple types of tests, e.g. you can run some `assert` statements.

You can also use some [fixtures](https://docs.pytest.org/en/7.2.x/reference/fixtures.html#fixture), i.e. tests whose output will be reused multiple times, which can be very useful when you need to load data or train your model.

```python
from mypackage import Model

@pytest.fixture
def trained_model(init_data):
    model = Model()
    model.fit()
    return model

# Here, the argument is the previous function name, but it actually contains the function output (i.e., the model)
def test_alpha_positive(trained_model):
    assert (trained_model.alpha > 0).all()

def test_is_symmetric(trained_model):
    x1, x2 = trained_model.x, -trained_model.x
    y1, y2 = trained_model(x1), trained_model(x2)

    assert torch.isclose(y1, y2, atol=1e-6).all() # To test if two tensor are equal, it's safer to use torch.isclose
```

## Run your tests

At the project's root, run:
```bash
pytest
```