from pathlib import Path
import base64

def convert_to_base64(filepath):
    print("Loading image file")
    with Path(filepath).open("rb") as fp:
        base64_img = base64.b64encode(fp.read())
        return base64_img.decode('utf-8')

if __name__ == '__main__':
    convert_to_base64()

#convert_to_base64("C:/Users/Henry Alberto/Desktop/Dunno/metadata/0.png")