import os


def copy_file(source: str, destination: str) -> None:
    if not source or not destination or source == destination:
        return
    
    if not os.path.exists(source) or not os.path.isfile(source):
        return

    if os.path.isdir(destination):
        destination = os.path.join(destination, os.path.basename(source))

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
    except Exception:
        pass


if __name__ == "__main__":
    pass

