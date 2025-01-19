def copy_file(command: str) -> None:
    command_parts = command.split(" ")
    if command_parts[0] != "cp" or len(command_parts) != 3:
        print("invalid input")
        return
    input_file = command_parts[1]
    output_file = command_parts[2]

    if str(input_file) != str(output_file):
        with (open(input_file, "r") as input_object,
              open(output_file, "w") as output_object):
            content = input_object.read()
            output_object.write(content)
