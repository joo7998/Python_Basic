from .database import *
# __init__.py
# package import -> initializing file
#   without it , still recognize as a package

# from package import * : whole ojb within -> import
__all__ = ["Database"] # only specified [] -> export
# __all__ = []    # import using * -> none exported
