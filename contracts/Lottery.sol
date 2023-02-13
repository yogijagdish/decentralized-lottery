//SPDX-Lisence-Identifier: MIT
pragma solidity ^0.8;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";


contract Lottery {

    address payable[] public players;
    uint256 entranceRate = 50;
    AggregatorV3Interface public ethUSDPriceFeed;

    constructor(_priceFeed) {
        ethUSDPriceFeed = AggregatorV3Interface(_priceFeed);
    }
    function startLottery() public {
        require(entranceRate < entranceFee(),"sorry not enough fees");
        players.push(msg.sender);
    }
    function endLottery() public{}
    function entranceFee() public view returns(uint256){
        (,int256 answer,,,) = ethUSDPriceFeed.latestRoundData();
        uint256 adjustedPrice = uint256(answer);
        uint256 entrancePrice = (50*10**18)/adjustedPrice;
        return entrancePrice;
        
    }
    function calculateEntrance() public{}
}