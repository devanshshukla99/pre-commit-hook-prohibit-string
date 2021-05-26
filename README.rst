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
        rev: [Release Version]
        hooks:
        - id: prohibit-string
            args: [--prohibit-string, "[string]"]


.. |build| image:: https://github.com/devanshshukla99/pre-commit-hook-prohibit-string/actions/workflows/main.yml/badge.svg
