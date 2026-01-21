def copy_file(command: str) -> None:
    command = command.split()

    if len(command) != 3 or command[0] != "cp":
        return
    source = command[1]
    target = command[2]

    if source == target:
        return

    try:
        with (open(source, "r") as file_in,
              open(target, "w") as file_out):
            for line in file_in:
                file_out.write(line)
    except FileNotFoundError:
        return
