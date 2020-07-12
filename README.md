# Dynamically Typed

This is the website for [Dynamically Typed](https://dynamicallytyped.com/), my newsletter.
For now, this repository only contains scripts for downloading issues and transforming them into [Hugo](https://gohugo.io)-compatible Markdown files.
In the future it'll also have scripts to extract more richt content (like individual stories and quick links) and render a Hugo-based static website.

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

### Rescraping

To rescrape all issues whose IDs are in `issue_ids.txt`, for example when some metadata formatting changes:

```bash
python rescrape.py
```
