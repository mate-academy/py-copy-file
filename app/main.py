def copy_file(command: str) -> bool:
    try:
        parts = command.strip().split()
        if len(parts) != 3:
            print("✗ Error: Invalid command format")
            return False

        cmd, source, destination = parts

        if cmd.lower() != "cp":
            print(f"✗ Error: Unknown command '{cmd}'")
            return False

        if source == destination:
            print("Info: Source and destination are the same")
            return False

        with open(source, "r") as file_in, open(destination, "w") as file_out:
            for line in file_in:
                file_out.write(line)

            return True

    except FileNotFoundError:
        print("Error: Source file not found")
        return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False
