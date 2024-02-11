def copy_file(command: str) -> None:
    cmd, input_name, output_name = command.split(" ")

    if cmd == "cd" and input_name != output_name:

        with (open(input_name, "r") as input_file,
              open(output_name, "w") as output_file):
            data = input_file.read()

            output_file.write(data)
