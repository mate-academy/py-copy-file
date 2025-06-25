def copy_file(command: str) -> None:
    command_list = command.strip().split()

    if not is_valid_command(command_list):
        return

    _, file_in_name, file_out_name = command_list

    if file_in_name == file_out_name:
        return

    try:
        with (open(file_in_name, "r") as file_in,
              open(file_out_name, "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError as e:
        print(f"File not found: {e.filename}")


def is_valid_command(command_list: list[str]) -> bool:
    return len(command_list) == 3 and command_list[0] == "cp"
