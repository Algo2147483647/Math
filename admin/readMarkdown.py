import numpy as np
import os
import pickle

class Cell:
    def __init__(self, concept, file):
        self.concept = concept
        self.content = []
        self.file = file
        self.kid = []
        self.parent = []

def readMarkdown(path):
    root = Cell('', '')
    cellLib = {"": root}
    stack = [(root, -2)]

    for file_name in os.listdir(path):
        with open(path + file_name, 'r', encoding = 'utf-8') as file:
            content = file.read()
            content = content.split('\n')

        for s in content:
            # Tab length
            tab = len(s) - len(s.lstrip())

            if(tab == len(s)):
                continue

            while(tab <= stack[-1][1]):
                stack.pop()

            if(s[tab:tab+2] == "* "):
                title = s.strip()[2:]

                if (title in cellLib):
                    newNode = cellLib[title]
                    if (tab == 0):
                        newNode.file = file_name
                else:
                    newNode = Cell(title, file_name)
                    cellLib[title] = newNode

                # add kid into tree
                stack[-1][0].kid.append(newNode)
                newNode.parent.append(stack[-1][0])
                # stack push
                stack.append((newNode, tab))
            else:
                stack[-1][0].content.append(s)

    for e in cellLib.values():
        if (e in root.kid and len(e.parent) != 1):
            root.kid.remove(e)
            e.parent.remove(root)

    with open("html/DAG.pkl", "wb") as f:
        pickle.dump(cellLib, f)