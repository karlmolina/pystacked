from typing import Optional


class StackItem:
    parent: Optional["StackItem"]

    def __init__(self, branch, cutoff):
        self.branch = branch
        self.cutoff = cutoff

    def __str__(self):
        parent = self.parent.branch if self.parent else self.branch
        return f"{self.branch} {parent} {self.cutoff}"
