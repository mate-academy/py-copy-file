def copy_file(command: str) -> None:
    if not command.startswith("cp"):
        return

    args = command.split()[1:]
    if len(args) != 2 or args[0] is None or args[1] is None:
        return

    try:
        with (open(args[0], "r") as src_file,
              open(args[1], "w") as dst_file):
            dst_file.write(src_file.read())
    except FileNotFoundError:
        return
