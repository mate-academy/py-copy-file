def copy_file(command: str) -> None:
    input_filename = command.split()[1]
    output_filename = command.split()[2]

    if input_filename != output_filename:
        with (
            open(input_filename, "r") as inp_f,
            open(output_filename, "w") as out_f
        ):
            out_f.write(inp_f.read())
    # return output_filename


print(copy_file("cp file.txt file.txt"))
