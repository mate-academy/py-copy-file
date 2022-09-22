def copy_file(command):
    command = command.split()

    match command:
        case ["cp", name_in, name_out]:
            if name_in == name_out:
                return

            with (open(name_in, "r") as file_in,
                  open(name_out, "w") as file_out):
                for line in file_in:
                    file_out.write(line)

        case ["cp", *arguments]:
            raise ValueError(f"Invalid syntax: command cp takes "
                             f"2 arguments, {len(arguments)} given.")

        case _:
            raise ValueError(f"Invalid command: {command[0]}")
