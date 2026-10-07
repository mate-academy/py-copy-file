def copy_file(command: str) -> None:
    if not command:
        return

    input_data = command.split(" ")

    if len(input_data) != 3:
        return

    if input_data[0] != "cp":
        return

    file_to_copy = input_data[1]
    new_file = input_data[2]

    if file_to_copy == new_file:
        return

    try:
        with (open(file_to_copy, "r") as file_in,
              open(new_file, "w") as file_out):
            file_content = file_in.read()
            file_out.write(file_content)
    except FileNotFoundError:
        pass
