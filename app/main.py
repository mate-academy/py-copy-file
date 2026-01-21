def copy_file(command: str) -> str:
    parts = command.split()

    if len(parts) == 3 and parts[0] == "cp":
        source_code, destination_code = parts[1], parts[2]

        if source_code != destination_code:
            with open(source_code) as f, open(destination_code, "wt") as m:
                m.write(f.read())

            return f"File {source_code} copied to {destination_code}"
