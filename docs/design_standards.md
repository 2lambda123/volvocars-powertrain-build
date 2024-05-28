# Design standard

## Imports

Allowed imports in production code is:

- Built-in packages
- Third party packages
- Libraries

If you need a function from another executable script, refactor it into a library and import it from both places.

Allowed imports in test code is:

- Built-in packages
- Third party packages
- Test libraries
- Functions from the code that is being tested

Use to full path when importing.

## Style guides

- The source code should follow [PEP-8](https://www.python.org/dev/peps/pep-0008/).
  - Exceptions to these rules are defined in the `<module>/tox.ini` and `<module>/.pylintrc` files
- Docstring documentation shall be done according to [PEP257 style guide](https://www.python.org/dev/peps/pep-0257/).

## Style guide verification

Test that the code is following the PEP-8 standards using [flake8](https://pypi.org/project/flake8/) by running 'flake8 <module>' and [pylint](https://www.pylint.org/) by running 'pylint <module>'.

The ignored folders should have their own configurations, to keep some kind of standard. For example the documentation folder:

- run 'flake8 <module>/doc' from the repo root folder. The rules are defined in `<module>/doc/tox.ini`
- run 'pylint <module>.doc --rcfile=<module>/doc/.pylintrc' from the project root folder. The rules are defined in `doc/.pylintrc`

Plugins that should be used with flake8:

- flake8-docstrings

## Comments

Comments inside the code (not docstrings) should explain WHY something is implemented the way it is, not WHAT the implementation does. An exception to this rule is regular expressions, which can be documented (but shall always tested).

Instead of commenting about what the code does, write relevant tests that shows this.

Commented and unused code shall be removed.

## Executable scripts

All python scripts that are executed from Jenkins or as stand-alone scripts should be located in the `<module>` in the project root folder

The executable scripts shall use argparse if any argument is needed for the execution of the script.

## Libraries

Common code should be located in the `<module>/lib` folder
If a library is only used by other libraries, it is allowed to put the files in a `<module>/lib/<library>` folder.

If the libraries requires arguments, they shall not be set as required in argparse. Instead, they shall have a check to see if they are present when needed. This is to make it easier to import the libraries if they are sometimes but not always using the library.

The library folders should all have an `__init__.py` containing doc string.

Placement of functions:

- If a function from an executable script is needed elsewhere, refactor it into a library and import it from both places.
- Only functions used by the library itself, functions that uses the library or functions used by more than one script should be in a library.
- Do not move a function to a library because you think it will be used by other scripts later. Wait until you can refactor both scripts to use the function.

## Tests

All tests shall be located in the `<module>/test` folder.
Unit tests shall be named `test_<submodule>.py` and function tests shall be named `func_<submodule>.py`
Example: `lib/gerrit.py` shall have a `<module>/test/test_gerrit.py`

Additional files needed by the tests shall be located in a separate folder: `test/<submodule>/<files>`

The test shall test WHAT the module is doing, not HOW. That means that you shall test as many public functions as possible, but do not explicitly test private functions (def `__<function>`). Instead of testing the private functions, test the public functions in such a way that the private functions are being tested as well. This makes it much easier to refactor how the code is implemented while keeping tests for what it does unmodified.

Some duplication of code is acceptable in the test code, as this should be more focused on DAMP (Descriptive And Meaningful Phrases) than DRY (Don't repeat yourself) code. While we want both, it sometimes makes the test code hard to read, and then DAMP should be prioritized in the test code.

Mocking inside of unit tests shall be limited to external systems (such as gerrit), and other processes (such as matlab). Mocking inside of function tests shall be limited to external systems (such as gerrit).

The code shall be unit tested using the python package unittest. The unit tests are run by `pytest.exe /\*\*/test\_\*.py` in the project root folder. The unit tests are run by `pytest.exe /\*\*/func\_\*.py` in the project root folder. All tests can be run by `python -m unittest discover -s `.
