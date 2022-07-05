import os, sys
try:
    __import__("rkb1").Main()
    except Exception as e:
    exit(str(e))