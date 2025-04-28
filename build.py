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

        os.makedirs(output_path.parent, exist_ok=True)
        write_file(
            template_data=template_data,
            markdown_contents=markdown_contents,
            output_file_path=output_path,
        )

        print(f'Generated "{source_path}" - "{output_path}"!')


def process_line(line: str) -> str:
    line = line.replace(" -> ", " ⇒ ")

    if line.startswith("IMAGES "):
        images = [i.strip() for i in line.removeprefix("IMAGES ").split() if i]
        line = """<div data-nanogallery2='{{"thumbnailWidth": "150", "thumbnailHeight": "150","thumbnailAlignment": "left", "thumbnailOpenImage": true}}'>{}</div>"""
        line = line.format(
            "".join(
                '<a href="assets/{}" data-ngthumb="assets/{}"></a>'.format(i, i)
                for i in images
            )
        )

    if line.startswith("YOUTUBE_"):
        video_id = line.split("_", 1)[-1].strip()

        loop = 0
        if video_id.startswith("LOOP_"):
            video_id = video_id.split("_", 1)[-1].strip()
            loop = 1

        return f"""<p><iframe
            allowfullscreen="true"
            frameborder="0"
            width="480"
            rel=0
            loop={loop}
            style="max-width: 100%; aspect-ratio: 16 / 9;"
            src="https://www.youtube.com/embed/{video_id}"
            ></iframe></p>"""

    return line


def write_file(*, template_data: str, markdown_contents: str, output_file_path):
    markdown_contents = "\n".join(
        process_line(line) for line in markdown_contents.split("\n")
    )

    content = markdown2.markdown(
        markdown_contents.replace(" - ", " — "), extras=["markdown-in-html"]
    )
    rendered_html = template_data.format(content=content)

    with open(output_file_path, "w", encoding="utf-8") as out_file:
        out_file.write(rendered_html)


if __name__ == "__main__":
    main()
