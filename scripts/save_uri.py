
def save_uri(_uri):
    with open("uris","a") as file:
        file.write(_uri + "\n")
        return file

if __name__ == '__main__':
    save_uri()