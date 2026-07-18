import os


def copy_file(command: str) -> None:
    content = command.split()

    if len(content) != 3:
        return
    if content[1] == content[2]:
        return
    if content[0] != "cp":
        return

    source_file = content[1]
    new_file = content[2]

    if not os.path.exists(source_file):
        return

    with (
        open(source_file, "r") as to_copy,
        open(new_file, "w") as to_insert
    ):
        file_content = to_copy.read()
        to_insert.write(file_content)
