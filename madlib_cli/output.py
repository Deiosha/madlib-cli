import re


def open_and_write(file_path):
    with open(file_path, 'w') as file:
        pass


def open_and_read(file_path):
    with open(file_path, 'r') as file:
        print(file.read())


def read_template(file_path):
    with open(file_path, 'r') as file:
        # print(file.read().strip())
        return file.read().strip()


def parse_template(template):
    pattern = r"{(.*?)}"
    parts = tuple(re.findall(pattern, template))
    stripped = re.sub(pattern, "{}", template)
    return stripped, parts


def merge(str, adj):
    merged = str.format(*adj)
    print(merged)
    return merged


if __name__ == '__main__':
    path = '../assets/dark_and_stormy_night_template.txt'
    template_txt = read_template(path)
    parse_template(template_txt)
