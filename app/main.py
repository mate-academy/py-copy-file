import os


def copy_file(command):
    parts = command.split()
    if len(parts) != 3 or parts[0] != 'cp':
        print("Invalid command format. Use: cp <source> <destination>")
        return

    src, dst = parts[1], parts[2]

    if src == dst:
        print("Source and destination files are the same. No action taken.")
        return

    if not os.path.isfile(src):
        print(f"Source file {src} does not exist.")
        return

    try:
        with open(src, 'r') as f_src:
            with open(dst, 'w') as f_dst:
                f_dst.write(f_src.read())
        print(f"File {src} copied to {dst}.")
    except Exception as e:
        print(f"Failed to copy {src} to {dst}: {e}")