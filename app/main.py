import os


def copy_file(source: str, destination: str) -> None:
    if not source or not destination or source == destination:
        return

    if not os.path.exists(source):
        return

    if os.path.isdir(destination):
        destination = os.path.join(destination, os.path.basename(source))
    else:
        dest_dir = os.path.dirname(destination)
        if dest_dir and not os.path.exists(dest_dir):
            os.makedirs(dest_dir, exist_ok=True)

    try:
        with open(source, "r", encoding="utf-8") as source_file:
            content = source_file.read()
        with open(destination, "w", encoding="utf-8") as dest_file:
            dest_file.write(content)
    except UnicodeDecodeError:
        with open(source, "rb") as source_file:
            content = source_file.read()
        with open(destination, "wb") as dest_file:
            dest_file.write(content)


if __name__ == "__main__":
    pass

