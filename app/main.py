def copy_file(cmd: str) -> None:
    from_file_name, to_file_name = cmd.split()[1:]
    if from_file_name == to_file_name:
        return
    with (
        open(from_file_name, "r") as file_in,
        open(to_file_name, "w") as file_out
    ):
        file_out.writelines(file_in.readlines())
