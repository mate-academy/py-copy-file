def copy_file(command_name: str) -> None:
    try:
        command, input_filename, output_filename, *_ = command_name.split()
    except Exception as e:
        print(e, "Wrong number of arguments!")
        return

    if command == "cp" and input_filename != output_filename:
        with (
            open(input_filename, "r") as input_file,
            open(output_filename, "w") as output_file
        ):
            output_file.write(input_file.read())
