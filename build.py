import re
from pathlib import Path
from xml.etree.ElementTree import SubElement
from datetime import datetime

import markdown
from markdown.blockprocessors import BlockProcessor

HTML_TEMPLATE_FILE_PATH = Path("index_template.html")
RU_MARKDOWN_CONTENTS_PATH = Path("README.md")
EN_MARKDOWN_CONTENTS_PATH = Path("README_EN.md")
RU_CV_OUTPUT_FILE = Path("docs/index.html")
EN_CV_OUTPUT_FILE = Path("docs/en.html")


class YouTubeExtension(markdown.Extension):
    def extendMarkdown(self, md):
        md.parser.blockprocessors.register(
            YouTubeBlockProcessor(md.parser), 'youtube', 175
        )


class YouTubeBlockProcessor(BlockProcessor):
    RE_FENCE_START = r'^{% include youtube '
    RE_FENCE_END = r' %}$'

    def test(self, parent, block):
        return re.match(self.RE_FENCE_START, block)

    def run(self, parent, blocks):
        original_block = blocks[0]
        blocks[0] = re.sub(self.RE_FENCE_START, '', blocks[0])

        # Find block with ending fence
        for block_num, block in enumerate(blocks):
            if not re.search(self.RE_FENCE_END, block):
                continue

            # remove fence
            video_id = block.split(" ", 1)[0]

            blocks[block_num] = re.sub(self.RE_FENCE_END, '', block)
            # render fenced area inside a new div
            div = SubElement(parent, 'div')
            iframe = SubElement(div, 'iframe')

            iframe.set('width', f"640")
            iframe.set('height', f"390")
            iframe.set('src', f"https://www.youtube.com/embed/{video_id}")
            iframe.set('allowfullscreen', "true")
            iframe.set('frameborder', "0")

            div.set('class', 'embed-container')

            for i in range(0, block_num + 1):
                blocks.pop(0)

        # No closing marker!  Restore and do nothing
        # blocks[0] = original_block
        return False  # equivalent to our test() routine returning False


def main():
    with open(HTML_TEMPLATE_FILE_PATH) as in_file:
        template_data = in_file.read()

    pairs = (
        (RU_MARKDOWN_CONTENTS_PATH, RU_CV_OUTPUT_FILE),
        (EN_MARKDOWN_CONTENTS_PATH, EN_CV_OUTPUT_FILE),
    )

    for source_path, output_path in pairs:
        print(f'Generating from "{source_path}" - "{output_path}"...')

        with open(source_path, encoding='utf-8') as in_file:
            markdown_contents = in_file.read()

        markdown_contents = markdown_contents  \
            .replace("/docs/index.html", "/")  \
            .replace("/docs/en.html", "/en")  \
            .replace("docs/assets/", "assets/")  \
            .replace("{% include today %}", datetime.now().strftime("%Y-%m-%d"))

        processed_markdows_contents = process_region(
            markdown_contents,
            opening="<NOT_IN_CV>",
            closing="<NOT_IN_CV_END>",
            remove=True,
        )
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
            data = data[:opening_index] + data[closing_index + len(closing):]
            continue

        data = (
            data[:opening_index]
            + data[opening_index + len(opening): closing_index]
            + data[closing_index + len(closing):]
        )


def write_file(*, template_data: str, markdown_contents: str, output_file_path):
    content = markdown.markdown(
        markdown_contents, extensions=["sane_lists", YouTubeExtension()]
    )
    rendered_html = template_data.format(content=content)

    with open(output_file_path, "w", encoding="utf-8") as out_file:
        out_file.write(rendered_html)


if __name__ == "__main__":
    main()
