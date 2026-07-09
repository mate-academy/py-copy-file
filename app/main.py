def copy_file(command: str) -> None:
    try:
        cmd, current_file, new_file = command.split(" ")
    except ValueError:
        return

    if cmd == "cp" and current_file != new_file:
        try:
            with (open(current_file, "r") as source,
                  open(new_file, "w") as target):
                target.write(source.read())
        except FileNotFoundError:
            return
