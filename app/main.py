def copy_file(command) -> None:
    try:
        parts = command.split()
        if len(parts) == 3 and parts[0] == "cp":
            cp, input_file, output_file = parts
            if input_file == output_file:
                return
            else:
                with open(input_file,
                          "r") as infile, open(output_file,
                                               "w") as outfile:
                    data = infile.read()
                    outfile.write(data)
        else:
            return
    except FileNotFoundError:
        return
