import os
import sys


def walker(path):
    """
    A simple function to return the paths and the files under the path
    return paths, files
    """
    walkers = os.walk(path) if os.path.exists(
        path) else None  # if the path exists, walker is os.walk(path), else is NoneTypeObject
    try:
        base = next(walkers)
    except:
        return ([], [])  # it mean's walker is None
    root, paths, files = base
    return paths, files
