from typing import Optional


class StackItem:
    parent: Optional["StackItem"]

    def __init__(self, branch, cutoff):
        self.branch = branch
        self.cutoff = cutoff
