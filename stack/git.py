import subprocess
import sys


def run_git_command(command):
    """Runs a git command and returns the output."""
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")
        print(f"Output: {e.output}")
        sys.exit(1)


def get_current_git_branch():
    try:
        # Run the git command to get the current branch name
        result = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        raise Exception(f"Error getting current branch: {e.stderr.strip()}")


def create_new_branch(branch_name: str):
    try:
        # Run the Git command to create a new branch
        subprocess.run(["git", "checkout", "-b", branch_name], check=True)
        print(f"Branch '{branch_name}' created and switched to it.")
    except subprocess.CalledProcessError as e:
        print(f"Error creating branch: {e.stderr.strip()}")


def get_current_commit():
    try:
        # Run the Git command to get the current commit hash
        commit_hash = (
            subprocess.check_output(["git", "rev-parse", "HEAD"])
            .strip()
            .decode("utf-8")
        )
        return commit_hash
    except subprocess.CalledProcessError as e:
        print(f"Error getting current commit: {e}")
        return None


def get_commit_of_branch(branch_name):
    try:
        # Run the Git command to get the commit hash of the given branch
        commit_hash = (
            subprocess.check_output(["git", "rev-parse", branch_name])
            .strip()
            .decode("utf-8")
        )
        return commit_hash
    except subprocess.CalledProcessError as e:
        print(f"Error getting commit of branch '{branch_name}': {e}")
    return None


def list_branches_at_commit(commit_hash):
    try:
        # Run the git command to get all branches containing the commit
        result = subprocess.run(
            ["git", "branch", "--contains", commit_hash],
            capture_output=True,
            text=True,
            check=True,
        )

        # Split the output into lines and clean up extra spaces
        branches = result.stdout.strip().split("\n")

        if branches:
            print(f"Branches containing commit {commit_hash}:")
            for branch in branches:
                print(branch.strip())
        else:
            print(f"No branches contain commit {commit_hash}.")

    except subprocess.CalledProcessError as e:
        print(f"Error executing git command: {e}")
    except FileNotFoundError:
        print("Git is not installed or not found in the system path.")


def get_parent_of_branch(branch_name):
    try:
        # Run the Git command to get the parent branch of the given branch
        parent_branch = (
            subprocess.check_output(
                ["git", "rev-parse", "--abbrev-ref", f"{branch_name}^"]
            )
            .strip()
            .decode("utf-8")
        )
        return parent_branch
    except subprocess.CalledProcessError as e:
        print(f"Error getting parent branch of '{branch_name}': {e}")
    return None
