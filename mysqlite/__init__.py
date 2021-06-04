from .database import *
# __init__.py
# package import -> initializing
#   without it , still recognize as package

# from PACKAGE import * : ALL object -> import
__all__ = ["Database"]
# __all__ = []    # * import --> none exported

