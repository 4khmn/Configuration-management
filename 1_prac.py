import os
import shlex
import argparse

username = os.environ.get("USERNAME") or os.environ.get("USER")

vfs_name = "MyVFS";

def parse_command(command: str):
    return shlex.split(command)

while True:
    user_input = input(f"{username}@{vfs_name}> ")

    if not user_input.strip():
        continue

    args = parse_command(user_input)

    command = args[0]
    command_args = args[1:]

    if command == "exit":
        print("Выход из виртуальной файловой системы")
        break
    elif command == "ls":
        print(f"[ls] Аргументы: {command_args}")
    elif command == "cd":
        print(f"[cd] Аргументы: {command_args}")
    else:
        print(f"Неизвестная команда: {command}")