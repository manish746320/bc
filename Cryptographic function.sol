pragma solidity >=0.7.0 <0.9.0;

contract Test{
    function callsha256() public pure returns(bytes32 result){
        return sha256("Tanya");
    }

    function callkeccak256() public pure returns(bytes32 result){
        return keccak256("Tanya");
    }
}
