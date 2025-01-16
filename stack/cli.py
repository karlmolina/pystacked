import typer
from collections import namedtuple
from stack.file import print_tuples, read_file_to_tuples, save_tuples_to_file
from stack.git import get_commit_of_branch, get_current_commit, get_current_git_branch
from stack.stackitem import StackItem

app = typer.Typer(no_args_is_help=True)

# Define the namedtuple for StackItem

@app.command()
def sync(branch_name: str):
    print("Syncing branches")


@app.command()
def add():
    current_branch = get_current_git_branch()
    current_commit = get_current_commit()

    # Read existing stack from file
    stack_items = read_file_to_tuples(".stack")

    if not stack_items:
        stack_items = {current_branch: StackItem(current_branch, current_commit)}
    else:
        # Get the parent branch from the last stack item
        parent_item = stack_items[-1]
        if parent_item.branch == current_branch:
            print("Already at top of stack")
            print_tuples(stack_items)
            return

        # Get the commit hash of the parent branch
        commit_at_parent = get_commit_of_branch(parent_item.branch)
        new_item = StackItem(current_branch, parent_item.branch, commit_at_parent)
        stack_items.append(new_item)

    # Save the updated stack to the file (convert namedtuple to a list of values)
    save_tuples_to_file([item for item in stack_items], ".stack")
    print_tuples(stack_items)


def main():
    app()
