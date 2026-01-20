def run_command(cmd: str):
    match cmd:
        case "start":
            return "STARTED"
        case "stop":
            return "STOPPED"
        case "status":
            return "OK"
        case _:
            return "UNKNOWN_COMMAND"


def main():
    for cmd in ["start", "status", "stop", "reboot", ""]:
        print(f"{cmd!r} -> {run_command(cmd)}")


if __name__ == "__main__":
    main()
