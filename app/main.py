def copy_file(command_name: str) -> None:
    try:
        command, input_filename, output_filename, *_ = command_name.split()
    except Exception as e:
        print(e, "Wrong number of arguments!")
        return

    if command == "cp" and input_filename != output_filename:
        with (
            open(input_filename, "r") as inp_f,
            open(output_filename, "w") as out_f
        ):
            out_f.write(inp_f.read())
