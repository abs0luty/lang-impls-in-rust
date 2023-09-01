import json
import requests

projects = []

with open("list.json") as json_file:
  data = json.load(json_file)

  for project in data:
    projects.append({
      "name": project["name"],
      "url": project["url"],
      "description": project["description"],
    })

with open("README.md", "w") as f:
  f.write("#  Languages Written in Rust\n")
  f.write("This is a (probably incomplete) list of %d languages implemented in Rust. It is intended as a source of inspiration and as a directory of potentially interesting projects in this vein.\n\n" % len(projects))
  f.write("Inspired by: https://github.com/alileybrinker/langs-in-rust.\n")
  f.write("_The difference is that here stars don't matter, every project here has an equal weight + this repository is updated very often._\n")
  f.write("## What Can Be Included?\n")
  f.write("- Is it a language?\n")
  f.write("- Is it written in Rust?\n")
  f.write("Then it can be included in this list!\n")
  f.write("## How to add my langauge?\n")
  f.write("- Add information about your project to `list.json` file.\n")
  f.write("- Run `cargo run` to generate new README.md.\n")
  f.write("- Make a pull request and just wait until I add submit it.\n")
  f.write("## The List\n")
  f.write("| Project | Description |\n")
  f.write("| --- | --- |\n")

  print(projects)
  projects.sort(key=lambda x: x["name"])

  for project in projects:
    f.write("| [" + project["name"] + "](" + project["url"] + ") | " + project["description"] + " |\n")
