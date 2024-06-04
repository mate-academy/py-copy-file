def copy_file(command: str) -> None:
    cp, source, output = command.split()
    if cp == "cp" and source != output:
        with (open(source, "r") as source_file,
              open(output, "w") as output_file):
            output_file.write(source_file.read())
