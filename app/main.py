def copy_file(command: str) -> None:
    file_names = command.split(" ")[1:]
    file_to_copy_name = file_names[0]
    new_file_name = file_names[1]

    if file_to_copy_name != new_file_name:
        with (open(file_to_copy_name, "r") as file_in,
              open(new_file_name, "w") as file_out):
            for line in file_in:
                file_out.write(f"{line}")
