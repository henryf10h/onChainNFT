from brownie import network, accounts, config, CryptoVagos

def main():
    net = network.show_active()
    print(net)
    account1 = accounts.add(config['wallets']['from_key'])
    return CryptoVagos.deploy({'from': account1 })

#https://github.com/eth-brownie/brownie/issues/1031

# 0x080c0F31a3Ede1C011B43C648924F61da3216621
#0x9D174E531794e87a27D6Acae53fC91C38f923917