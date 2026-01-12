import os
import sys

from app import App

def main():
    try:
        app = App()
        app.run()
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()