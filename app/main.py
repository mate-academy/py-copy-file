import os


def copy_file(source: str, destination: str) -> None:
    if not source or not destination or source == destination:
        return
    
    if not os.path.exists(source):
        return

    if os.path.isdir(destination):
        destination = os.path.join(destination, os.path.basename(source))

    try:
        with open(source, "r", encoding="utf-8") as source_file, \
                open(destination, "w", encoding="utf-8") as dest_file:
            dest_file.write(source_file.read())
    except Exception:
        with open(source, "rb") as source_file, \
                open(destination, "wb") as dest_file:
            dest_file.write(source_file.read())


if __name__ == "__main__":
    pass

