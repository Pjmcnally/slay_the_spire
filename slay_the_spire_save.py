import base64


def main():
    file = r"Z:\Downloads\2_IRONCLAD.autosave"
    with open(file, 'r') as f:
        content = base64.b64decode(f.read())

    print(content)


main()
