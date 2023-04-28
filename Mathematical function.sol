pragma solidity >=0.7.0 <0.9.0;

contract Sample{
    function callAddMod() public pure returns (uint){
        return addmod(3,4,5);
//3+4 % 5
    }

   function callMulMod() public pure returns (uint){
        return mulmod(3,4,5);
    }
//3*4 % 5
}
