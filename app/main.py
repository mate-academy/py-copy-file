def copy_file(command: str) -> None | str:
    command_name, input_filename, output_filename, *_ = command.split()

    if command_name != "cp":
        return (
            f"Wrong command has been entered '{command_name}'"
            f" (only the 'cp' command is accepted)"
        )

    if input_filename == output_filename:
        return

    with (open(input_filename, "r") as original,
          open(output_filename, "w") as copy):
        copy.write(original.read())
