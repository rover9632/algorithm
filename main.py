# coding=utf-8

import sys
import importlib
import re
from os import path


if __name__ == "__main__":
    pattern = re.compile(r"[/\\]{1,2}")
    modlue_path = path.relpath(sys.argv[1])
    mdl = importlib.import_module(pattern.sub(r".", modlue_path)[:-3])
    mdl.main(sys.argv[2:])
