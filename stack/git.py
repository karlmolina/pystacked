import subprocess


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
        print(f"Error getting current branch: {e.stderr.strip()}")
        return None


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
        commit_hash = subprocess.check_output(["git", "rev-parse", branch_name]).strip().decode("utf-8")
        return commit_hash
    except subprocess.CalledProcessError as e:
        print(f"Error getting commit of branch '{branch_name}': {e}")
        return None
