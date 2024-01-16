from os.path import exists


def copy_file(command: str) -> None:
    command = command.split(" ")

    if len(command) == 3 and command[0] == "cp":
        input_file, output_file = command[1], command[2]

        if exists(input_file) and input_file != output_file:
            with (open(input_file, "r") as file_in,
                  open(output_file, "w") as file_out):
                file_out.write(file_in.read())
