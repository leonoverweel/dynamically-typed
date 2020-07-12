from revue_to_hugo import revue_to_md

with open("issue_ids.txt", "r") as ids_file:
    for line in ids_file:
        issue_id = line.strip()
        print(f"Rescraping issue `{issue_id}`...", end=" ", flush=True)

        issue_number, markdown = revue_to_md(issue_id)
        with open(f"content/issues/{issue_number}.md", "w") as out_file:
            out_file.write(markdown)

        print(f"Done, scraped #{issue_number}")
