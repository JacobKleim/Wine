import argparse
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader, select_autoescape

import utils


def main():
    load_dotenv()

    parser = argparse.ArgumentParser()

    parser.add_argument('-f', '--path_drinks_file',
                        help='Путь к файлу с данными',
                        default=os.environ.get('PATH_DRINKS_FILE'))

    args = parser.parse_args()

    wines_filepath = args.path_drinks_file

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    winery_age = utils.get_past_years()

    rendered_page = template.render(
        drinks=utils.group_wines_by_category(wines_filepath),
        winery_age=winery_age,
        year_form=utils.get_year_form(winery_age)
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
