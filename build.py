from pathlib import Path

import markdown

HTML_TEMPLATE_FILE_PATH = Path("index_template.html")
MARKDOWN_CONTENTS_PATH = Path("README.md")
CV_OUTPUT_FILE = Path("docs/index.html")
JAMS_OUTPUT_FILE = Path("docs/jams.html")


def main():
    with open(HTML_TEMPLATE_FILE_PATH) as in_file:
        template_data = in_file.read()
    with open(MARKDOWN_CONTENTS_PATH) as in_file:
        markdown_contents = in_file.read()

    markdown_contents = markdown_contents.replace("docs/assets/", "assets/")

    # Making for CV
    cv_markdown_contents = process_region(
        markdown_contents,
        opening="<NOT_IN_CV>",
        closing="<NOT_IN_CV_END>",
        remove=True,
    )
    write_file(
        template_data=template_data,
        markdown_contents=cv_markdown_contents,
        output_file_path=CV_OUTPUT_FILE,
    )

    # Making for Game Jams
    jams_markdown_contents = process_region(
        markdown_contents,
        opening="<NOT_IN_CV>",
        closing="<NOT_IN_CV_END>",
        remove=False,
    )
    write_file(
        template_data=template_data,
        markdown_contents=jams_markdown_contents,
        output_file_path=JAMS_OUTPUT_FILE,
    )


def process_region(data: str, *, opening: str, closing: str, remove: bool) -> str:
    while True:
        opening_index = data.find(opening)
        closing_index = data.find(closing)

        if opening_index != -1 and closing_index == -1:
            raise ValueError
        if opening_index == -1:
            return data

        if remove:
            data = data[:opening_index] + data[closing_index + len(closing):]
            continue

        data = (
            data[:opening_index]
            + data[opening_index + len(opening): closing_index]
            + data[closing_index + len(closing):]
        )


def write_file(*, template_data: str, markdown_contents: str, output_file_path):
    content = markdown.markdown(markdown_contents, extensions=["sane_lists"])
    rendered_html = template_data.format(content=content)

    with open(output_file_path, "w") as out_file:
        out_file.write(rendered_html)


if __name__ == "__main__":
    main()
