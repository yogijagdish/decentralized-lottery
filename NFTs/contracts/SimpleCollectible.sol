// SPDX-License-Identifier: MIT

pragma solidity ^0.6.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract SimpleCollectible is ERC721 {

    uint256 public tokenCollector;

    // syntax for ERC-721 : constructor(no parameters) erc721('name','symbol')
    constructor() public ERC721("Doggie","dog") {
        tokenCollector = 0;
    }

    function publicCollectible (string memory tokenURI) public returns(uint256){
        uint256 newToken = tokenCollector;
        _safeMint(msg.sender,newToken);
        _setTokenURI(newToken,tokenURI);
        tokenCollector = tokenCollector + 1;
        return newToken;
    }
}