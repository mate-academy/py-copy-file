def copy_file(command: str) -> None:
    operator, existing_file, new_file = command.split(" ")
    if operator == "cp" and new_file != existing_file:
        with (open(existing_file, "r") as file_in,
              open(new_file, "w") as file_out):
            for line in file_in:
                file_out.write(line + "\n")
