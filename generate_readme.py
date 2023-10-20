import json

projects = []

with open("list.json") as json_file:
    projects = json.load(json_file)

readme_template = """
# Language implementations Written in Rust
This is a (probably incomplete) list of %d languages implemented in Rust. It is intended as a source of inspiration and as a directory of potentially interesting projects in this vein.

Inspired by: https://github.com/alilleybrinker/langs-in-rust.

## What Can Be Included?
- Is it a language?
- Is it written in Rust?
Then it can be included in this list!

## How to add my langauge?
- Add information about your project to `list.json` file.
- Run `python generate_readme.py` to generate new README.md.
- Make a pull request and just wait until I add submit it.

## The List
| Project | Description | Stars |
| --- | --- | --- |
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_template % len(projects))
    projects.sort(key=lambda x: int(x["stars"].split("..")[0]))
    projects.reverse()

    for project in projects:
        if project["stars"] == "10_000..":
            project["name"] = "🔥 " + project["name"]
        elif project["stars"] == "1_000..10_000":
            project["name"] = "😱 " + project["name"]
        elif project["stars"] == "400..1_000":
            project["name"] = "😋 " + project["name"]
        else:
            project["name"] = "👀 " + project["name"]

        f.write("| [" + project["name"] + "](" + project["url"] +
                ") | " + project["description"] + " | `" + project["stars"] + "` |\n")
