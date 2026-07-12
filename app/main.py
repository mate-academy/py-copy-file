def copy_file(parameters: str) -> None:
    if not parameters:
        return None
    whole_command = list(parameters.split(" "))
    if whole_command[0] != "cp" or len(whole_command) < 3:
        return None

    origin_name = whole_command[1]
    copy_name = whole_command[2]

    try:
        with open(origin_name, "r") as of, open(copy_name, "w") as copy:
            for line in of.readlines():
                copy.write(line)
    except FileNotFoundError:
        print(f"No such file or directory: {origin_name}")
