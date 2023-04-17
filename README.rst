===============
Prohibit String
===============

|build|

Provides a ``pre-commit`` hook for prohibiting a string in a package, for example,
prohibiting ``from warnings import warn`` may be useful.


Usage
------

Add the following to ``.pre-commit-config.yaml``:

.. code-block:: console

    - repo: https://github.com/devanshshukla99/pre-commit-hook-prohibit-string
        rev: {github release tag}
        hooks:
        - id: prohibit-string
            args: [--prohibit-string, "{string}"]

Example to forbid ``from warnings import warn`` and ``warnings.warn``:

.. code-block:: console

  - repo: https://github.com/devanshshukla99/pre-commit-hook-prohibit-string
    rev: v1.2
    hooks:
      - id: prohibit-string
        args: [--prohibit-string, "from warnings import warn,warnings.warn"]
        exclude: ""


.. |build| image:: https://github.com/devanshshukla99/pre-commit-hook-prohibit-string/actions/workflows/main.yml/badge.svg
