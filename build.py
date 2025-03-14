import hashlib
import os
import re
import shutil
from datetime import datetime
from glob import glob
from pathlib import Path

import markdown2

HTML_TEMPLATE_FILE_PATH = Path("index_template.html")


def main():
    with open("style.css", "rb") as in_file:
        pretty_hash = hashlib.md5(in_file.read()).hexdigest()[:8]
        style_css_path = "/style-{}.css".format(pretty_hash)

    with open(HTML_TEMPLATE_FILE_PATH) as in_file:
        template_data = in_file.read().replace("{{ STYLE_CSS }}", style_css_path)

    pairs = [
        (Path("pages") / i, Path("docs") / (i[:-2] + "html"))
        for i in glob("**/*.md", root_dir="pages", recursive=True)
    ]

    old_style_css = [i for i in glob("style-*.css", root_dir="docs", recursive=False)]
    for old_file in old_style_css:
        os.remove(Path("docs") / old_file)
    shutil.copyfile("style.css", Path("docs") / "style-{}.css".format(pretty_hash))

    for source_path, output_path in pairs:
        print(f'Generating from "{source_path}" - "{output_path}"...')

        with open(source_path, encoding="utf-8") as in_file:
            markdown_contents = in_file.read()

        markdown_contents = (
            markdown_contents.replace("/docs/index.html", "/")
            .replace("/docs/en.html", "/en")
            .replace("docs/assets/", "assets/")
            .replace("{% include today %}", datetime.now().strftime("%Y-%m-%d"))
        )

        processed_markdows_contents = process_region(
            markdown_contents,
            opening="<NOT_IN_CV>",
            closing="<NOT_IN_CV_END>",
            remove=True,
        )
        os.makedirs(output_path.parent, exist_ok=True)
        write_file(
            template_data=template_data,
            markdown_contents=processed_markdows_contents,
            output_file_path=output_path,
        )

        print(f'Generated "{source_path}" - "{output_path}"!')


def process_region(data: str, *, opening: str, closing: str, remove: bool) -> str:
    while True:
        opening_index = data.find(opening)
        closing_index = data.find(closing)

        if opening_index != -1 and closing_index == -1:
            raise ValueError
        if opening_index == -1:
            return data

        if remove:
            data = data[:opening_index] + data[closing_index + len(closing) :]
            continue

        data = (
            data[:opening_index]
            + data[opening_index + len(opening) : closing_index]
            + data[closing_index + len(closing) :]
        )


def process_line(line: str) -> str:
    if line.startswith("YOUTUBE_"):
        video_id = line.split("_", 1)[-1].strip()
        return f"""<div><iframe
            allowfullscreen="true"
            frameborder="0"
            width="640"
            height="360"
            src="https://www.youtube.com/embed/{video_id}"></iframe></div>"""

    return line


def write_file(*, template_data: str, markdown_contents: str, output_file_path):
    markdown_contents = "\n".join(
        process_line(line) for line in markdown_contents.split("\n")
    )

    content = markdown2.markdown(markdown_contents)
    rendered_html = template_data.format(content=content)

    with open(output_file_path, "w", encoding="utf-8") as out_file:
        out_file.write(rendered_html)


if __name__ == "__main__":
    main()
