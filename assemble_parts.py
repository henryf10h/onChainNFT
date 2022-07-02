from parts import PARTS
from PIL import Image
from genes import genes
from randomness import random_number

def assemble(number_of_vagos):
    for i in range(number_of_vagos):
        adn = genes(random_number(i))
        print(adn)
        im0 = Image.open(PARTS["face"]["img"][adn[0] % 4]).convert("RGBA")
# WORKING BODY
        bg = Image.new("RGBA",size=(700,700),color=PARTS["bg"][adn[1]%5])
        face = im0.copy()
        eyes = Image.open(PARTS["eyes"]["img"][adn[2]%5]).convert("RGBA")
        hair = Image.open(PARTS["hair"]["img"][adn[3]%11]).convert("RGBA")
        mouth = Image.open(PARTS["mouth"]["img"][adn[4]%4]).convert("RGBA")
        acc = Image.open(PARTS["acc"]["img"][adn[5]%7]).convert("RGBA")
        nouse = Image.open(PARTS["nouse"]["img"][adn[6]%1]).convert("RGBA")
        ear = Image.open(PARTS["ear"]["img"][adn[7]%4]).convert("RGBA")
# ASSEMBLY
        bg.paste(face,mask=face)
        bg.paste(hair,mask=hair)
        bg.paste(eyes,mask=eyes)
        bg.paste(mouth,mask=mouth)
        bg.paste(nouse,mask=nouse)
        bg.paste(ear,mask=ear)
        bg.paste(acc,mask=acc)
# SHOW
        #bg.show()
# SAVE VAGOS V2
        bg.save("./metadata/{}.png".format(i))

assemble(67)