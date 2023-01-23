def copy_file(command: str) -> None:
    cmd, source, target = command.split(" ")
    if cmd == "cp" and len(command.split(" ")) == 3 \
            and source != target:
        with (
            open(source, "r") as file1,
            open(target, "w") as file2
        ):
            file2.write(file1.read())
