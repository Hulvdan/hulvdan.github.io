from pathlib import Path

import markdown

HTML_TEMPLATE_FILE_PATH = Path("index_template.html")
MARKDOWN_CONTENTS_PATH = Path("index.md")
OUTPUT_FILE = Path("docs/index.html")


with open(HTML_TEMPLATE_FILE_PATH) as in_file:
    template_data = in_file.read()
with open(MARKDOWN_CONTENTS_PATH) as in_file:
    markdown_contents = in_file.read()

markdown_contents = markdown_contents.replace("docs/assets/", "assets/")

content = markdown.markdown(markdown_contents, extensions=["sane_lists"])
rendered_html = template_data.format(content=content)

with open(OUTPUT_FILE, "w") as out_file:
    out_file.write(rendered_html)
