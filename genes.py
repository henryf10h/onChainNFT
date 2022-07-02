# GENERATE RANDOM NUMBER, READ IT AND ASSIGN TWO PAIRS FOR EACH GENE.

# GENES :
# borde[51], ojos[25], bocas[45], cyb[58], inferior[74], six[86], cuerpo[19].

def genes(num):
    genes = []
    for i in range(8):
        a = str(num)[:2]
        b = str(num)[2:] 
        num = int(b)
        genes.append(int(a))
    return genes

if __name__ == '__main__':
    genes()
