def copy_file(command: str) -> None:

    token_input = command.split(" ")

    if len(token_input) != 3:
        return

    if token_input[0] != "cp":
        return

    target_file_name = token_input[1]
    new_file_name = token_input[2]

    if target_file_name == new_file_name:
        return

    try:
        with (
            open(target_file_name, "r") as file_in,
            open(new_file_name, "w") as file_out
        ):
            for line in file_in:
                file_out.write(line)
    except FileNotFoundError:
        return
