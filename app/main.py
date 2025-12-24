def copy_file(command: str) -> None:
    try:
        cmd, source, target = command.split()

        if cmd != "cp" or source == target:
            return

        with open(source, "r") as src, open(target, "w") as dst:
            dst.write(src.read())

    except Exception:
        return
