from metadata_template import metadata_template
from pathlib import Path
import json
from convert_to_base64 import convert_to_base64
from save_uri import save_uri

def write_metadata(max_nft_amount):
    for i in range(max_nft_amount):
        nft_metadata = metadata_template
        metadata_file_path = (
            "./metadata/" + str(i) + ".json"
        )
        if Path(metadata_file_path).exists():
            print("{} already exists!".format(metadata_file_path))
        else:
            print("creating metadata file: {}".format(metadata_file_path))
            nft_metadata["name"] = i
            nft_metadata["description"] = "CryptoVago #{}".format(i)
            image_path = "./metadata/{}.png".format(i)
            image_to_upload = convert_to_base64(image_path)
            nft_metadata["image"] = "data:image/png;base64," + image_to_upload
            with open(metadata_file_path, "w",encoding = "utf-8") as write_file:
                json.dump(nft_metadata, write_file)
                write_file.close()
                print(metadata_file_path)
                uri = convert_to_base64(metadata_file_path)
                save_uri('data:application/json;base64,' + uri)

write_metadata(67)