def copy_file(command: str) -> None:
    _, input_name, output_name = command.split(" ")

    if input_name == output_name:
        return

    with (open(input_name, "r") as input_file,
          open(output_name, "w") as output_file):
        data = input_file.read()

        output_file.write(data)
