import jsonlines
import argparse
from pathlib import Path


parser = argparse.ArgumentParser()
parser.add_argument('source', help='source jsonlines file')
parser.add_argument('destination', help='destination directory')
args = parser.parse_args()
source = Path(args.source)
destination = Path(args.destination)

with jsonlines.open(source) as reader:
    for obj in reader:
        author = obj['author']
        work_title = obj['title']
        section_title = obj['section_title']
        section_content = obj['section_content']
        author = author.replace('/', '\\')
        work_title = work_title.replace('/', '\\')
        section_title = section_title.replace('/', '\\')
        author = author[:50]
        work_title = work_title[:50]
        section_title = section_title[:50]
        output_dir = destination/author/work_title
        output_dir.mkdir(parents=True, exist_ok=True)
        output_file = output_dir/(section_title + '.txt')
        text = '\n\n'.join(section_content)

        output_file.touch()
        output_file.write_text(text)
