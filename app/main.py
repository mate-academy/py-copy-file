def copy_file(command: str) -> None:
    try:
        cp_part, source_filename, target_filename = command.split(" ")
        print(cp_part, source_filename, target_filename)
        if cp_part == "cp" and source_filename != target_filename:
            with (
                open(source_filename) as source_file,
                open(target_filename, "w") as target_file
            ):
                for line in source_file.readlines():
                    target_file.write(line)
    except ValueError:
        pass
    except FileNotFoundError:
        pass
