from io import StringIO
from inspect import cleandoc
from contextlib import redirect_stdout

from pre_commit_hooks.prohibit_string import match, main


def test_match_func(tmp_path):
    test_file = tmp_path / "check_prohibit.py"
    test_file.write_text(cleandoc(
        """
        import os
        import numpy as np
        import warnings


        def testing_something():
            return 1
        """))
    with StringIO() as buf, redirect_stdout(buf):
        result = match("import warnings", test_file)
        out = str(buf.getvalue())
        assert result == 1
        assert out.endswith('check_prohibit.py:2: Prohibited string (import warnings)\n') is True


def test_main_func(tmp_path):
    test_file = tmp_path / "check_prohibit.py"
    test_file.write_text(cleandoc(
        """
        import os
        import numpy as np
        import warnings
        import re

        def testing_something():
            return 1
        """))

    with StringIO() as buf, redirect_stdout(buf):
        result = main([f"{test_file}", "--prohibit-string", "import warnings"])
        assert result == 1
        out = str(buf.getvalue())
        assert out.endswith('check_prohibit.py:2: Prohibited string (import warnings)\n') is True
