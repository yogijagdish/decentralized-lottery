//SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";
import "@openzeppelin/contracts/access/Ownable.sol";


contract Lottery is Ownable {

    address payable[] public players;
    uint256 entranceRate = 50 * 10 ** 18;
    AggregatorV3Interface public ethUSDPriceFeed;
    uint256 randomNumber;
    address payable public winner;

    enum LotteryState {
        OPEN,
        CLOSED,
        PROCESSING_WINNER
    }

    LotteryState public lotteryState;

    constructor (address _priceFeed) public {
        lotteryState = LotteryState.CLOSED;
        ethUSDPriceFeed = AggregatorV3Interface(_priceFeed);
    }
    function Enter() public payable {
        require(lotteryState == LotteryState.OPEN);
        require(msg.value > entranceFee(),"sorry not enough fees");
        players.push(payable(msg.sender));
    }
    function endLottery() public onlyOwner{
        randomNumber = uint256(
            keccak256(
                abi.encodePacked(
                    msg.sender,
                    block.difficulty,
                    block.timestamp
                )
            )
        ) % players.length;
        winner = players[randomNumber];
        winner.transfer(address(this).balance);
        players = new address payable[](0);
    }
    function entranceFee() public view returns(uint256){
        (,int256 answer,,,) = ethUSDPriceFeed.latestRoundData();
        uint256 adjustedPrice = uint256(answer) * 10 ** 10;
        uint256 entrancePrice = (50*10**18)/adjustedPrice;
        return entrancePrice;
        
    }
    function startLottery() public onlyOwner{
        require(lotteryState == LotteryState.CLOSED,"cannot start new lottery yet!!!");
        lotteryState = LotteryState.OPEN;
    }
}