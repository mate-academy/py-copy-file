def copy_file(command: str) -> None:
    try:
        command_type, input_file_name, output_file_name = command.split(" ")
    except ValueError:
        print("Correct input format: <command> "
              "<input file name> <output file name>")
        return

    if command_type != "cp":
        print("Incorrect command name. Type 'cp' for copy.")
        return

    if input_file_name == output_file_name:
        print("Input and output file names should be different.")
        return

    try:
        with open(input_file_name, "r") as input_file, \
             open(output_file_name, "w") as output_file:
            output_file.write(input_file.read())
    except FileNotFoundError:
        print(f"No input file with such name: {input_file_name}")
        return
