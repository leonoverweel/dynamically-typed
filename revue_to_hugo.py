import sys
import textwrap
from urllib import request

from bs4 import BeautifulSoup
import html2text


# CSS classes used by Revue
CLS_BLOCKQUOTE = "revue-blockquote"
CLS_H2 = "header-text"
CLS_IMG = "img"
CLS_P = "revue-p"
CLS_UL = "ul"
CLS_OL = "ol"


def transform_element(html_element):
    """Transform an HTML element from Revue into markdown text and return it."""

    cls = html_element["class"][0]

    # Skip empty elements
    if html_element.text == "" and cls != CLS_IMG:
        return ""

    converter = html2text.HTML2Text()
    converter.body_width = 0

    # Blockquotes
    if cls == CLS_BLOCKQUOTE:
        text = converter.handle(str(html_element)).strip()

        # Make text one sentence per line
        text = text.replace(". ", ".\n> ")
        text = text.replace("! ", "!\n> ")
        text = text.replace("? ", "?\n> ")

    # Headers
    elif cls == CLS_H2:
        text = f"## {html_element.text.strip()}"

    # Images
    elif cls == CLS_IMG:
        url = html_element.attrs["src"]
        alt = html_element.attrs["alt"]
        text = f"![{alt}]({url})\n\n_{alt}_"

    # Paragraphs
    elif cls == CLS_P:
        text = converter.handle(str(html_element))

        # Make text one sentence per line
        text = text.replace(".** ", ".**\n")
        text = text.replace("!** ", "!**\n")
        text = text.replace("?** ", "?**\n")

        text = text.replace(". ", ".\n")
        text = text.replace("! ", "!\n")
        text = text.replace("? ", "?\n")

    # Unordered lists
    elif cls == CLS_UL:
        text = converter.handle(str(html_element))

        # Remove indent
        text = text.replace("  * ", "* ")

    # Ordered lists
    elif cls == CLS_OL:
        text = converter.handle(str(html_element))

        # Remove indent
        text = "\n".join([line.strip() for line in text.split("\n")])

    else:
        raise ValueError("Unimplemented class")

    return f"{text.strip()}\n\n"


def load_issue(issue_id, base_url="https://dynamicallytyped.com"):
    """Download an issue and return its HTML contents."""

    url = f"{base_url}/issues/0-{issue_id}"
    req = request.Request(
        url, headers={"User-Agent": "Totally a real browser and not a bot, yep"}
    )

    return request.urlopen(req).read().decode("utf-8")


def revue_to_md(issue_id):
    html_doc = load_issue(issue_id)
    soup = BeautifulSoup(html_doc, "html.parser")

    # Clean content to make it ready for transformer

    # (html2text needs semantic HTML for blockquotes)
    quotes = soup.find_all(class_=CLS_BLOCKQUOTE)
    for tag in quotes:
        tag.name = "blockquote"

    # (only selecting on classes so we add class="ul" to <ul>s)
    uls = soup.find_all(name="ul")
    for tag in uls:
        tag.attrs["class"] = [CLS_UL]

    # (same for <ol>s)
    ols = soup.find_all(name="ol")
    for tag in ols:
        tag.attrs["class"] = [CLS_OL]

    # (images)
    images = soup.find_all("img", width="600")
    for tag in images:
        if tag.attrs["alt"] != "Dynamically Typed":
            tag.attrs["class"] = [CLS_IMG]

    # Extract relevant content
    content = soup.find_all(
        class_=lambda cls: cls
        in [CLS_BLOCKQUOTE, CLS_H2, CLS_IMG, CLS_P, CLS_UL, CLS_OL]
    )

    # Transform content
    title = soup.title.text.split("|")[0]
    date = soup.find("time").attrs["datetime"].split("T")[0]
    revue_link = soup.find("link", {"rel": "canonical"}).get("href")
    number = title.split(":")[0].strip("#")
    markdown = "".join(transform_element(tag) for tag in content).strip()

    # Add Hugo info
    hugo_info = textwrap.dedent(
        f"""
        ---
        title: "{title}"
        date: {date}
        number: {number}
        aliases:
          - {revue_link}
        ---
        """
    ).strip()

    return number, hugo_info + "\n\n" + markdown


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(
            "Usage: `python revue_to_md.py issue_id`, where the latter is the 6-digit ID in the URL."
        )
        exit()

    issue_number, markdown = revue_to_md(sys.argv[1])
    issue_name = f"dynamically-typed-{int(issue_number):03}"

    with open(f"content/issues/{issue_name}.md", "w") as out_file:
        out_file.write(markdown)
