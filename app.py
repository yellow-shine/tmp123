import sys

def log(message):
    print(f"[LOG] {message}", file=sys.stderr)

def greet(name):
    return f"Hello, {name}!"

def farewell(name):
    return f"Goodbye, {name}!"

def main():
    log("Starting app")
    print(greet("World"))
    print(farewell("World"))
    log("App finished")

if __name__ == "__main__":
    main()
