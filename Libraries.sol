pragma solidity ^0.8.0;

import "./MathUtils.sol";

contract calculator{
    using MathUtils for uint;

    function getSum(uint a, uint b) public pure returns(uint){
        return a.add(b);
    }
}
