def copy_file(command: str) -> None:
    if len(command.split(" ")) == 3:
        cmd, source, target = command.split(" ")
        if cmd == "cp" and source != target:
            with (
                open(source, "r") as src_file,
                open(target, "w") as tg_file
            ):
                tg_file.write(src_file.read())
