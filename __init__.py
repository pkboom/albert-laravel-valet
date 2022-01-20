from albert import *
import re
from os import path
from os import walk

__title__ = "Laravel valet"
__version__ = "0.4.0"
__triggers__ = "va "
__authors__ = "pkboom"

icon = "{}/icon.png".format(path.dirname(__file__))

_dirs = [
    '/home/y/code',
]

def handleQuery(query):
    if not query.isTriggered or not query.isValid:
        return

    projects = []

    for _dir in _dirs:
        for root, dirs, files in walk(_dir):
            for dir in dirs:
                projects.append(path.join(root, dir))
            break

    regexp = query.string.strip().replace(" ", ".*")

    items = []

    for project in projects:
        if re.search(regexp, project[(project.rfind('/') + 1):]): 
            items.append(Item(
                id=project,
                icon=icon,
                text=project[(project.rfind('/') + 1):],
                actions=[TermAction(
                    text="This action runs valet.", 
                    script='cd {} && valet share'.format(project), 
                )],
            ))

    return items
