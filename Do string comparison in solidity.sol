pragma solidity >=0.7.0 <0.9.0;
contract Demo{
    string str1="TANYA";
    string str2='TANYA';

    bool public isEqual;
    
    function cmp() public
    {
        isEqual=keccak256(abi.encodePacked(str1))==keccak256(abi.encodePacked(str2));
    }
}
