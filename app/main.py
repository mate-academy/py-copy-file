def copy_file(command: str) -> None:
    try:
        cp, file_in, file_out = command.split()
        if cp != "cp":
            raise ValueError()
        if file_in != file_out:
            with (
                open(file_in, "r") as src_file,
                open(file_out, "w") as dst_file,
            ):
                for line in src_file:
                    dst_file.write(line)
    except ValueError:
        pass
    except OSError:
        pass
