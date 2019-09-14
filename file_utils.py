def readFile(path: str) -> str:
    with open(path, "r") as file:
        data = file.read()
    return data

def writeFile(path: str, contents: str):
    with open(path, "w") as file:
        file.write(contents)
