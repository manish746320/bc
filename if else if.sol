pragma solidity >=0.7.0 <0.9.0;
contract Check{
    uint i=100;
    uint j=100;
    function ifElseIf() public returns(string memory)
    {
        if(i<j)
        { 
            return "i is smaller than j";}
        else if(i>j)
        {
            return " i is greater than j"; }
        else
        {
            return " i is equal to j";
       }}}
