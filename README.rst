================
Prohibit Strings
================

|build|

This package provides a ``pre-commit`` hook for prohibiting certain string.

Useage
------

Add the following to ``.pre-commit-config.yaml``:

.. code-block:: console

    - repo: https://github.com/devanshshukla99/pre-commit-hook-prohibit-string
        rev: [Release Version]
        hooks:
        - id: prohibit-string
            args: [--prohibit-string, "[string]"]


.. |build| image:: https://github.com/devanshshukla99/pre-commit-hook-prohibit-string/actions/workflows/main.yml/badge.svg
