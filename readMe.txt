>>>>>>>>>>>   on chain token URI   <<<<<<<<<<<<<

proceed as this:

> get image file from pendrive - no, create new pixel art for this

> convert png file to svg file - to many files does not work
use remote app - we are storing pngs

> save png in bytes64 format for token metadata
make python script to set metadata for every Vagabundo
for image and JSON - convert json into string with '', then encode it. Save 
the  encoded data into file and pass it to the function tokenURI as URI - call setURI function from
openzeppelin ERC721URIStorage.sol

> call setTokenURI for every Vagabundo and add onchain metadata
need to pay fees

> check on Opensea and ask for help if necessary