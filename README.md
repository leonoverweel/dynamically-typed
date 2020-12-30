# Dynamically Typed

This is the website for [Dynamically Typed](https://dynamicallytyped.com/), my newsletter.
This repository only contains scripts for downloading issues and transforming them into [Hugo](https://gohugo.io)-compatible Markdown files and to split them up into individual stories and links.
For the source of the Hugo website, see the `website` directory.

## Setup

Set up a Python 3 environment and install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

This repository contains two scripts: `revue_to_hugo.md` to download and transform a new issue, and `rescrape.py` to rescrape all issues.

### Downloading one issue

To download and transform an issue:

```bash
python revue_to_hugo.py issue_id
```

Where `issue_id` is the 6-digit identifier at the end of the Revue link for the issue.
This script will also append the ID to `issue_ids.txt`, for future rescraping.

### Extracting content

To extract links and stories from an issue and dump them in the appropriate `website/content` folders:

```bash
python extract.py issue_number
```

### Rescraping

To rescrape all issues whose IDs are in `issue_ids.txt`, for example when some metadata formatting changes:

```bash
python rescrape.py
```

## Copyright

Written contents from Dynamically Typed (in the `website/content` folder) are &copy; Leon Overweel / [Nubic](https://nubic.tech).