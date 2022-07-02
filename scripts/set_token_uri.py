from brownie import accounts, config, Contract, network
#from uri_to_id import uri_to_id
import time

ABI = [       
    {   
        'inputs': [],
        'name': "constructor",        
        'stateMutability': "nonpayable",
        'type': "constructor"
    },
    {
        'anonymous': False,
        'inputs': [
            {
                'indexed': True,
                'internalType': "address",
                'name': "owner",
                'type': "address"
            },
            {
                'indexed': True,
                'internalType': "address",
                'name': "approved",
                'type': "address"
            },
            {
                'indexed': True,
                'internalType': "uint256",
                'name': "tokenId",
                'type': "uint256"
            }
        ],
        'name': "Approval",
        'type': "event"
    },
    {
        'anonymous': False,
        'inputs': [
            {
                'indexed': True,
                'internalType': "address",
                'name': "owner",
                'type': "address"
            },
            {
                'indexed': True,
                'internalType': "address",
                'name': "operator",
                'type': "address"
            },
            {
                'indexed': False,
                'internalType': "bool",
                'name': "approved",
                'type': "bool"
            }
        ],
        'name': "ApprovalForAll",
        'type': "event"
    },
    {
        'anonymous': False,
        'inputs': [
            {
                'indexed': True,
                'internalType': "address",
                'name': "previousOwner",
                'type': "address"
            },
            {
                'indexed': True,
                'internalType': "address",
                'name': "newOwner",
                'type': "address"
            }
        ],
        'name': "OwnershipTransferred",
        'type': "event"
    },
    {
        'anonymous': False,
        'inputs': [
            {
                'indexed': True,
                'internalType': "address",
                'name': "from",
                'type': "address"
            },
            {
                'indexed': True,
                'internalType': "address",
                'name': "to",
                'type': "address"
            },
            {
                'indexed': True,
                'internalType': "uint256",
                'name': "tokenId",
                'type': "uint256"
            }
        ],
        'name': "Transfer",
        'type': "event"
    },
    {
        'inputs': [
            {
                'internalType': "address",
                'name': "to",
                'type': "address"
            },
            {
                'internalType': "uint256",
                'name': "tokenId",
                'type': "uint256"
            }
        ],
        'name': "approve",
        'outputs': [],
        'stateMutability': "nonpayable",
        'type': "function"
    },
    {
        'inputs': [
            {
                'internalType': "address",
                'name': "owner",
                'type': "address"
            }
        ],
        'name': "balanceOf",
        'outputs': [
            {
                'internalType': "uint256",
                'name': "",
                'type': "uint256"
            }
        ],
        'stateMutability': "view",
        'type': "function"
    },
    {
        'inputs': [
            {
                'internalType': "uint256",
                'name': "tokenId",
                'type': "uint256"
            }
        ],
        'name': "getApproved",
        'outputs': [
            {
                'internalType': "address",
                'name': "",
                'type': "address"
            }
        ],
        'stateMutability': "view",
        'type': "function"
    },
    {
        'inputs': [
            {
                'internalType': "address",
                'name': "owner",
                'type': "address"
            },
            {
                'internalType': "address",
                'name': "operator",
                'type': "address"
            }
        ],
        'name': "isApprovedForAll",
        'outputs': [
            {
                'internalType': "bool",
                'name': "",
                'type': "bool"
            }
        ],
        'stateMutability': "view",
        'type': "function"
    },
    {
        'inputs': [
            {
                'internalType': "uint256",
                'name': "_numberToken",
                'type': "uint256"
            }
        ],
        'name': "mintVago",
        'outputs': [
            {
                'internalType': "bool",
                'name': "",
                'type': "bool"
            }
        ],
        'stateMutability': "nonpayable",
        'type': "function"
    },
    {
        'inputs': [],
        'name': "name",
        'outputs': [
            {
                'internalType': "string",
                'name': "",
                'type': "string"
            }
        ],
        'stateMutability': "view",
        'type': "function"
    },
    {
        'inputs': [],
        'name': "owner",
        'outputs': [
            {
                'internalType': "address",
                'name': "",
                'type': "address"
            }
        ],
        'stateMutability': "view",
        'type': "function"
    },
    {
        'inputs': [
            {
                'internalType': "uint256",
                'name': "tokenId",
                'type': "uint256"
            }
        ],
        'name': "ownerOf",
        'outputs': [
            {
                'internalType': "address",
                'name': "",
                'type': "address"
            }
        ],
        'stateMutability': "view",
        'type': "function"
    },
    {
        'inputs': [],
        'name': "renounceOwnership",
        'outputs': [],
        'stateMutability': "nonpayable",
        'type': "function"
    },
    {
        'inputs': [],
        'name': "s_MAX_MINT",
        'outputs': [
            {
                'internalType': "uint256",
                'name': "",
                'type': "uint256"
            }
        ],
        'stateMutability': "view",
        'type': "function"
    },
    {
        'inputs': [],
        'name': "s_MAX_SUPPLY",
        'outputs': [
            {
                'internalType': "uint256",
                'name': "",
                'type': "uint256"
            }
        ],
        'stateMutability': "view",
        'type': "function"
    },
    {
        'inputs': [
            {
                'internalType': "address",
                'name': "from",
                'type': "address"
            },
            {
                'internalType': "address",
                'name': "to",
                'type': "address"
            },
            {
                'internalType': "uint256",
                'name': "tokenId",
                'type': "uint256"
            }
        ],
        'name': "safeTransferFrom",
        'outputs': [],
        'stateMutability': "nonpayable",
        'type': "function"
    },
    {
        'inputs': [
            {
                'internalType': "address",
                'name': "from",
                'type': "address"
            },
            {
                'internalType': "address",
                'name': "to",
                'type': "address"
            },
            {
                'internalType': "uint256",
                'name': "tokenId",
                'type': "uint256"
            },
            {
                'internalType': "bytes",
                'name': "_data",
                'type': "bytes"
            }
        ],
        'name': "safeTransferFrom",
        'outputs': [],
        'stateMutability': "nonpayable",
        'type': "function"
    },
    {
        'inputs': [
            {
                'internalType': "address",
                'name': "operator",
                'type': "address"
            },
            {
                'internalType': "bool",
                'name': "approved",
                'type': "bool"
            }
        ],
        'name': "setApprovalForAll",
        'outputs': [],
        'stateMutability': "nonpayable",
        'type': "function"
    },
    {
        'inputs': [
            {
                'internalType': "uint256",
                'name': "tokenId",
                'type': "uint256"
            },
            {
                'internalType': "string",
                'name': "_tokenURI",
                'type': "string"
            }
        ],
        'name': "setTokenURI",
        'outputs': [],
        'stateMutability': "nonpayable",
        'type': "function"
    },
    {
        'inputs': [
            {
                'internalType': "bytes4",
                'name': "interfaceId",
                'type': "bytes4"
            }
        ],
        'name': "supportsInterface",
        'outputs': [
            {
                'internalType': "bool",
                'name': "",
                'type': "bool"
            }
        ],
        'stateMutability': "view",
        'type': "function"
    },
    {
        'inputs': [],
        'name': "symbol",
        'outputs': [
            {
                'internalType': "string",
                'name': "",
                'type': "string"
            }
        ],
        'stateMutability': "view",
        'type': "function"
    },
    {
        'inputs': [
            {
                'internalType': "uint256",
                'name': "index",
                'type': "uint256"
            }
        ],
        'name': "tokenByIndex",
        'outputs': [
            {
                'internalType': "uint256",
                'name': "",
                'type': "uint256"
            }
        ],
        'stateMutability': "view",
        'type': "function"
    },
    {
        'inputs': [
            {
                'internalType': "address",
                'name': "owner",
                'type': "address"
            },
            {
                'internalType': "uint256",
                'name': "index",
                'type': "uint256"
            }
        ],
        'name': "tokenOfOwnerByIndex",
        'outputs': [
            {
                'internalType': "uint256",
                'name': "",
                'type': "uint256"
            }
        ],
        'stateMutability': "view",
        'type': "function"
    },
    {
        'inputs': [
            {
                'internalType': "uint256",
                'name': "tokenId",
                'type': "uint256"
            }
        ],
        'name': "tokenURI",
        'outputs': [
            {
                'internalType': "string",
                'name': "",
                'type': "string"
            }
        ],
        'stateMutability': "view",
        'type': "function"
    },
    {
        'inputs': [],
        'name': "totalSupply",
        'outputs': [
            {
                'internalType': "uint256",
                'name': "",
                'type': "uint256"
            }
        ],
        'stateMutability': "view",
        'type': "function"
    },
    {
        'inputs': [
            {
                'internalType': "address",
                'name': "from",
                'type': "address"
            },
            {
                'internalType': "address",
                'name': "to",
                'type': "address"
            },
            {
                'internalType': "uint256",
                'name': "tokenId",
                'type': "uint256"
            }
        ],
        'name': "transferFrom",
        'outputs': [],
        'stateMutability': "nonpayable",
        'type': "function"
    },
    {
        'inputs': [
            {
                'internalType': "address",
                'name': "newOwner",
                'type': "address"
            }
        ],
        'name': "transferOwnership",
        'outputs': [],
        'stateMutability': "nonpayable",
        'type': "function"
    }
]

def uri_to_id(_id):
    with open("./uris","r") as file:
         for i in enumerate(file):
            #[(0,"sleep"),(1,"awake")]
             if i[0] == _id:
                #print(i[1])
                return i[1]

def main():
    net = network.show_active()
    print(net)
    account = accounts.add(config['wallets']['from_key'])
    pix_vagos = Contract.from_abi("CryptoVagos", "0xd21d16CeB7cD96E1b6C87B0F0308f9a65C213605", ABI)
    for i in range(pix_vagos.totalSupply()):
        pix_vagos.setTokenURI(i,uri_to_id(i),{'from': account })
        print('setting up URI for token id #{}'.format(i))
        time.sleep(1)

