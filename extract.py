import glob
import sys


def extract_issue_contents(issue_path):
    extract_issue = input(f"Do you want to extract issue `{issue_path}`? (y/n): ")
    if extract_issue != "y":
        print(f"Skipping issue `{issue_path}`\n")
        return

    print("Extracting...\n")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        extract_issue_contents(f"content/issues/{int(sys.argv[-1]):03}.md")

    else:
        for issue_path in sorted(glob.glob("content/issues/*.md"), reverse=True):
            extract_issue_contents(issue_path)
