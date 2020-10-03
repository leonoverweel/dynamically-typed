from pathlib import Path
import glob
import sys

import yaml

from revue_to_hugo import _one_sentence_per_line


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
        "date": issue_metadata["date"],
    }

    year = str(issue_metadata["date"].year)
    Path(f"content/stories/{year}").mkdir(exist_ok=True)

    with open(f"content/stories/{year}/{slug}.md", "w") as story_file:
        story_file.writelines(
            ["---\n", yaml.safe_dump(story_metadata), "---\n\n", text]
        )


def save_quick_link(text, title, slug, category, issue_metadata):
    text = text.strip("*").strip()

    quick_link_metadata = {
        "title": title,
        "category": category,
        "issue_number": issue_metadata["number"],
        "date": issue_metadata["date"],
        "emoji": text[0],
    }

    directory = f"content/quick-links/{category}"
    Path(directory).mkdir(exist_ok=True)
    date_id = issue_metadata["date"].strftime("%y%m%d")

    with open(f"{directory}/{date_id}-{slug}.md", "w") as quick_link_file:
        quick_link_file.writelines(
            [
                "---\n",
                yaml.safe_dump(quick_link_metadata),
                "---\n\n",
                _one_sentence_per_line(text[1:].strip()).strip(),
            ]
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

        if "**Quick" in text_raw:
            stories_raw, quick_links_raw = text_raw.split("**Quick")
            quick_links_raw = quick_links_raw[quick_links_raw.find("**\n") + 2 :]
            quick_links_raw = quick_links_raw[quick_links_raw.find("6c2e4))") + 7 :]
        else:
            stories_raw = text_raw
            quick_links_raw = text_raw

        def extract_lines(is_story, raw):
            raw = raw.strip()

            while raw:
                show_next = input(f"Show next? It has {len(raw)} chars. (y/n): ")
                if show_next != "y":
                    break

                lines = raw.split("\n")
                for i, line in enumerate(lines):
                    print(f"{i}: {line[:50]}...")

                num_lines = int(input("How many lines in this content? (int): "))
                content = "\n".join(lines[: num_lines + 1])

                title = input("Title: ")

                default_slug = title.lower().strip()  # lowercase
                default_slug = "".join(
                    char for char in default_slug if char.isalnum() or char == " "
                )  # alphanumeric
                default_slug = default_slug.replace(" ", "-")  # hyphenate
                slug = input(f"Slug (default: `{default_slug}`): ")
                if not slug:
                    slug = default_slug

                if is_story:
                    save_story(content, title, slug, category, issue_metadata)
                else:
                    save_quick_link(content, title, slug, category, issue_metadata)

                raw = "\n".join(lines[num_lines + 1 :])

        # Extract stories
        print("Extracting stories...")
        extract_lines(True, stories_raw)

        # Extract quick links
        print("\nExtracting quick links...")
        extract_lines(False, quick_links_raw)

        print("Done.")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        extract_issue_contents(f"content/issues/{int(sys.argv[-1]):03}.md")

    else:
        for issue_path in sorted(glob.glob("content/issues/*.md"), reverse=True):
            extract_issue_contents(issue_path)
            print("\n\n")
