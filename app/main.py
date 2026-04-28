def copy_file(
        command: str
) -> None:
    split = command.split(" ")
    if len(split) == 3 and split[0] == "cp" and split[1] != split[2]:
        in_name = split[1]
        out_name = split[2]
        try:
            with (
                    open(in_name, "r") as in_file,
                    open(out_name, "w") as out_file
            ):
                for line in in_file:
                    out_file.write(line)
        except FileNotFoundError:
            pass
