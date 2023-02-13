//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";


contract Lottery {

    address payable[] public players;
    uint256 entranceRate = 50 * 10 ** 18;
    AggregatorV3Interface public ethUSDPriceFeed;

    enum LotteryState {
        OPEN,
        CLOSED,
        PROCESSING_WINNER
    }

    LotteryState public lotteryState;

    constructor(address _priceFeed) {
        lotteryState = LotteryState.CLOSED;
        ethUSDPriceFeed = AggregatorV3Interface(_priceFeed);
    }
    function Enter() public payable {
        require(lotteryState == LotteryState.OPEN);
        require(msg.value > entranceFee(),"sorry not enough fees");
        players.push(payable(msg.sender));
    }
    function endLottery() public{}
    function entranceFee() public view returns(uint256){
        (,int256 answer,,,) = ethUSDPriceFeed.latestRoundData();
        uint256 adjustedPrice = uint256(answer) * 10 ** 10;
        uint256 entrancePrice = (50*10**18)/adjustedPrice;
        return entrancePrice;
        
    }
    function startLottery() public{
        require(lotteryState == LotteryState.CLOSED,"cannot start new lottery yet!!!");
        lotteryState = LotteryState.OPEN;

    }
}