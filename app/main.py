def copy_file(command: str) -> None:
    try:
        com, original_file, copy_file = command.split()
    except ValueError:
        return

    if com == "cp" and original_file != copy_file:
        try:
            with open(original_file, "r") as src_file, open(
                copy_file, "w"
            ) as dst_file:
                content = src_file.read()
                dst_file.write(content)
        except FileNotFoundError:
            return
