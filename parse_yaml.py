from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

document = """
  a: 1
  b:
    c: 3
    d: 4
"""
print(load(document, Loader=Loader))