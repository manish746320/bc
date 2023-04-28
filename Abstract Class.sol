pragma solidity ^0.5.0;

contract A {
   function getResult() public view returns(uint);
}
contract B is A {
   function getResult() public view returns(uint) {
      uint a = 100;
      uint b = 201;
      uint result = a * b;
      return result;
   }
}
