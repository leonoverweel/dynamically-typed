from pathlib import Path
import glob
import sys

import yaml


categories = {
    "Productized Artificial Intelligence 🔌": "productized-ai",
    "Machine Learning Research 🎛": "ml-research",
    "Artificial Intelligence for the Climate Crisis 🌍": "climate-ai",
    "Cool Things ✨": "cool-things",
}


def save_story(text, title, slug, category, issue_metadata):
    story_metadata = {
        "title": title,
        "category": category,
        "issue_number": issue_metadata["number"],
        "data": issue_metadata["date"],
    }

    year = str(issue_metadata["date"].year)
    Path(f"content/stories/{year}").mkdir(exist_ok=True)

    with open(f"content/stories/{year}/{slug}.md", "w") as story_file:
        story_file.writelines(
            ["---\n", yaml.safe_dump(story_metadata), "---\n\n", text]
        )


def extract_issue_contents(issue_path):
    print(str.upper(f"Extracting contents from `{issue_path}`..."))

    # Load issue
    with open(issue_path, "r") as issue_file:
        meta_raw, issue_text = issue_file.read().split("\n---\n")
    issue_metadata = yaml.safe_load(meta_raw)

    for section in issue_text.split("\n## "):
        section_lines = section.strip().split("\n")
        name = section_lines[0]
        text_raw = "\n".join(section_lines[1:]).strip()

        if not name in categories:
            print(f"Skipping unknown section `{name}`.")
            continue

        category = categories[name]
        print(f"\nExtracting section `{category}`...")

        stories_raw, quick_links_raw = text_raw.split("**Quick")

        # Extract stories
        stories_raw = stories_raw.strip()
        while stories_raw:
            show_story = input(
                f"Show next story? It has {len(stories_raw)} chars. (y/n): "
            )
            if show_story != "y":
                break

            story_lines = stories_raw.split("\n")
            for i, line in enumerate(story_lines):
                print(f"{i}: {line[:50]}...")

            num_lines = int(input("How many lines in this story? (int): "))
            story = "\n".join(story_lines[: num_lines + 1])

            title = input("Title: ")

            default_slug = title.lower().strip()  # lowercase
            default_slug = "".join(
                char for char in default_slug if char.isalnum() or char == " "
            )  # alphanumeric
            default_slug = default_slug.replace(" ", "-")  # hyphenate
            slug = input(f"Slug (default: `{default_slug}`): ")
            if not slug:
                slug = default_slug

            save_story(story, title, slug, category, issue_metadata)
            stories_raw = "\n".join(story_lines[num_lines + 1 :])

        print("Done.")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        extract_issue_contents(f"content/issues/{int(sys.argv[-1]):03}.md")

    else:
        for issue_path in sorted(glob.glob("content/issues/*.md"), reverse=True):
            extract_issue_contents(issue_path)
            print("\n\n")
