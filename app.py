import sys
from config import DEBUG, LOG_LEVEL

def log(message):
    level = f"[{LOG_LEVEL}]" if LOG_LEVEL else ""
    print(f"[LOG]{level} {message}", file=sys.stderr)

def greet(name):
    return f"Hello, {name}!"

def farewell(name):
    return f"Goodbye, {name}!"

def main():
    if DEBUG:
        log("Debug mode enabled")
    log("Starting app")
    print(greet("World"))
    print(farewell("World"))
    log("App finished")

if __name__ == "__main__":
    main()
