def copy_file(command: str) -> None:
    if len(command.split()) == 3:
        cmd = command.split()[0]
        file_in = command.split()[1]
        file_out = command.split()[2]

        if cmd == "cp" and file_in != file_out:
            try:
                with open(file_in, "r") as source, open(
                    file_out, "w"
                ) as destination:
                    content = source.read()
                    destination.write(content)
            except FileNotFoundError:
                print("The source file was not found in working directory")
