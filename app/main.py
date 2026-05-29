# write your code here
def copy_file(command: str) -> None:
    parts = command.split(" ")
    if len(parts) != 3:
        return
    if parts[0] != "cp":
        return

    source_file = parts[1]
    end_file = parts[2]

    if source_file == end_file:
        return

    try:
        with open(source_file, "r") as source, open(end_file, "w") as final:
            final.write(source.read())
    except FileNotFoundError:
        return
