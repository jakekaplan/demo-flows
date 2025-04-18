import subprocess

from prefect import flow


def get_git_info() -> tuple[str, str]:
    """
    Get the current git branch and commit hash.

    Returns:
        A tuple containing (branch_name, commit_hash)
    """
    try:
        # Get current branch
        branch_process = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True,
            text=True,
            check=True
        )
        branch = branch_process.stdout.strip()

        # Get current commit hash
        commit_process = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=True
        )
        commit = commit_process.stdout.strip()

        return branch, commit
    except subprocess.CalledProcessError as e:
        print(f"Error executing git command: {e}")
        return "unknown", "unknown"

@flow(log_prints=True)
def git_flow() -> None:
    branch, commit = get_git_info()
    print(f"Current branch: {branch}")
    print(f"Current commit: {commit}")
    print(f"NEW STUFF!!!!")

if __name__ == '__main__':
    git_flow()