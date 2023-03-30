def copy_file(command: str) -> None:
    if len(command.split()) == 3:
        parameter, old_file, new_file = command.split()

        if (parameter == "cp"
                and old_file != new_file):
            with (open(old_file, "r") as file_in,
                  open(new_file, "w") as file_out):
                file_out.write(file_in.read())
        else:
            raise ValueError("Parameter must be 'cp'")
