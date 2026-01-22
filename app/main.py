def copy_file(command: str) -> None:
    if len(command.split()) != 3:
        return

    cmd, input_name, output_name = command.split()
    if cmd != "cp" or input_name == output_name:
        return

    try:
        with (open(input_name, "r") as file_in,
              open(output_name, "w") as file_out):
            for line in file_in:
                file_out.write(line)
    except FileNotFoundError as e:
        print("File not found:", e)
