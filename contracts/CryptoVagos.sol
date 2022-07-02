// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract CryptoVagos is ERC721, ERC721Enumerable, ERC721URIStorage, Ownable {
    constructor() ERC721("CryptoVagos", "CVAGS") {}

    /// STATES ///
    uint256 public s_MAX_MINT = 7;
    uint256 public s_MAX_SUPPLY = 67;
    /// FUNCTIONS ///

    function mintVago(uint256 _numberToken) public returns (bool){
        if (totalSupply() <= s_MAX_SUPPLY) {
            _mintVago(_numberToken,msg.sender);
        }
        return true;
    }

    function setTokenURI(uint256 tokenId, string memory _tokenURI) public onlyOwner {
        _setTokenURI(tokenId, _tokenURI);
    }

    function _mintVago(uint256 _numberToken,address _address) internal {
        for (uint256 i = 0; i < _numberToken; i++) {
            uint256 Id = totalSupply();
            _safeMint(_address, Id);
            Id = Id + 1;
            
        }
        
    }

    // The following functions are overrides required by Solidity.

    function _beforeTokenTransfer(address from, address to, uint256 tokenId)
        internal
        override(ERC721, ERC721Enumerable)
    {
        super._beforeTokenTransfer(from, to, tokenId);
    }

    function _burn(uint256 tokenId) internal override(ERC721, ERC721URIStorage) {
        super._burn(tokenId);
    }

    function tokenURI(uint256 tokenId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (string memory)
    {
        return super.tokenURI(tokenId);
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721Enumerable)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}
