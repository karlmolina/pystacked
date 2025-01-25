import typer
from stack.file import print_dict, read_file_to_dict, save_dict_to_file
from stack.git import create_new_branch, get_current_commit, get_current_git_branch
from stack.stackitem import StackItem

app = typer.Typer(no_args_is_help=True)

# Define the namedtuple for StackItem


@app.command()
def sync(branch_name: str):
    print("Syncing branches")


@app.command()
def add(branch_name: str):
    current_branch = get_current_git_branch()
    current_commit = get_current_commit()

    stack_items = read_file_to_dict(".stack")

    if not stack_items:
        stack_items = {current_branch: StackItem(current_branch, current_commit)}
    elif current_branch not in stack_items:
        print("Error: Current branch not found in the stack.")
        return

    create_new_branch(branch_name)
    stack_items[branch_name] = StackItem(branch_name, current_commit)
    stack_items[branch_name].parent = stack_items[current_branch]

    # Save the updated stack to the file (convert namedtuple to a list of values)
    save_dict_to_file(stack_items, ".stack")
    print_dict(stack_items)


def main():
    app()
