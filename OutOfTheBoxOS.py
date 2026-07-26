# This is ware Out of the Box Starts!
# Notes, this is something that contains Code form AI, not saying its fully coded by AI, Ai was only used for helping with finding imports for features and also help with finding bugs in code.

# Imports!

import time
import os
import math
from datetime import datetime
import subprocess

# This is ware are code starts!

def show_boot_screen():
    """Display the boot sequence"""
    print("Welcome to my Operating system Shood boot any second now!")
    print("Also No this is not a custom kernel (in a way) but no real os to boot into qemu or Virtualbox/ware!")
    time.sleep(0.2)  
    print("Importing time")
    time.sleep(0.2)  
    print("importing os")
    time.sleep(0.2)  
    print("importing math")
    time.sleep(0.2)
    print("\n[Unboxing finished, enjoy!]\n")

def show_help():
    """Show available commands"""
    print("\n=== Available Commands ===")
    print("  help          - Show this help message")
    print("  exit/quit     - Exit the terminal")
    print("  ls/dir        - List files in current directory")
    print("  cd <dir>      - Change directory")
    print("  pwd           - Print working directory")
    print("  echo <text>   - Print text")
    print("  time          - Show current time")
    print("  clear         - Clear the screen")
    print()

def list_files():
    """List files in current directory"""
    try:
        files = os.listdir(".")
        for file in files:
            print(file)
    except Exception as e:
        print(f"Error: {e}")

def change_directory(args):
    """Change to a different directory"""
    if not args:
        print("Usage: cd <directory>")
        return
    try:
        os.chdir(args[0])
        print(f"Changed to: {os.getcwd()}")
    except FileNotFoundError:
        print(f"Directory not found: {args[0]}")
    except Exception as e:
        print(f"Error: {e}")

def run_terminal():
    """Main terminal loop"""
    while True:
        try:
            user_input = input(">>> ").strip()
            
            if not user_input:
                continue
            
            # Split input into command and arguments
            parts = user_input.split()
            command = parts[0].lower()
            args = parts[1:] if len(parts) > 1 else []
            
            # Command dispatch
            if command == "exit" or command == "quit":
                print("Goodbye!")
                break
            elif command == "help":
                show_help()
            elif command == "ls" or command == "dir":
                list_files()
            elif command == "cd":
                change_directory(args)
            elif command == "pwd":
                print(f"Current directory: {os.getcwd()}")
            elif command == "echo":
                print(" ".join(args))
            elif command == "time":
                print(f"Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            elif command == "clear":
                os.system("clear" if os.name == "posix" else "cls")
            else:
                print(f"Unknown command: {command}")
        
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    show_boot_screen()
    run_terminal()
