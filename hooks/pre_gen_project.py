import re

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"
EMAIL_REGEX = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

module_name = "{{cookiecutter.module_name}}"
email = "{{cookiecutter.author_email}}"

assert re.fullmatch(
    MODULE_REGEX, module_name
), f"The module name '{module_name}' is not a valid Python module name. Please do not use '-' or spaces (or any other invalid character), use '_' instead."

assert re.fullmatch(
    EMAIL_REGEX, email
), f"The email adress '{email}' has an incorrect format."
