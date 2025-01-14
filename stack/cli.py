import typer

from stack.file import read_file_to_tuples, save_tuples_to_file
from stack.git import get_commit_of_branch, get_current_commit, get_current_git_branch

app = typer.Typer(no_args_is_help=True)


@app.command()
def sync(branch_name: str):
    print("Syncing branches")


BRANCH = 0
PARENT = 1
CUTOFF = 2


@app.command()
def add():
    current_branch = get_current_git_branch()
    current_commit = get_current_commit()
    a = read_file_to_tuples(".stack")
    if not a:
        a = [(current_branch, current_branch, current_commit)]
    else:
        parent = a[-1][BRANCH]
        commit_at_parent = get_commit_of_branch(parent)
        a.append((current_branch, a[-1][BRANCH], commit_at_parent))
    save_tuples_to_file(a, ".stack")


def main():
    app()
