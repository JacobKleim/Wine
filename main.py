import argparse
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader, select_autoescape

import utils


def main():
    load_dotenv()

    parser = argparse.ArgumentParser()

    parser.add_argument('-f', '--file_path',
                        help='Путь к файлу с данными',
                        default=os.environ.get('FILE_PATH'))

    args = parser.parse_args()

    wines_file = args.file_path

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    date = utils.get_past_years()

    rendered_page = template.render(
        drinks=utils.convert_by_category(wines_file),
        date=date,
        year=utils.get_year_form(date)
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
