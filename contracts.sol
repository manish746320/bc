pragma solidity ^0.8.0;
contract Storage
{
uint public setData;
function set(uint x) public{
setData = x;
}
function get() public view returns (uint) {
    return setData;
}}
