def copy_file(command: str) -> None:
    files_list = command.split(" ")
    input_file = files_list[1]
    output_file = files_list[2]

    if str(input_file) != str(output_file):
        with (open(input_file, "r") as input_object,
              open(output_file, "w") as output_object):
            content = input_object.read()
            output_object.write(content)
