pragma solidity ^0.5.12;

contract Sample{
    function getSum(uint a, uint b) public pure returns (uint){
        return a+b;
    }

    function getSum(uint a, uint b, uint c) public pure returns (uint){
        return a+b+c;
    }

    function callSumWithTwoArguments() public pure returns (uint){
        return getSum(4,9);
    }

     function callSumWithThreeArguments() public pure returns (uint){
        return getSum(4,9,6);
    }
}
