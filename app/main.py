def copy_file(command: str) -> str:
    split_command = command.split()

    if len(split_command) < 3:
        return "It looks like some of the required entries are missing"
    cp_command, file_in_name, file_out_name = split_command

    if file_in_name == file_out_name or cp_command != "cp":
        return "Something has gone wrong. Please check command entry"

    with (
        open(file_in_name, "r") as file_in,
        open(file_out_name, "w") as file_out,
    ):
        file_content = file_in.read()
        file_out.write(file_content)
