pragma solidity >=0.7.0 <0.9.0;
contract SS{
    string str1="M.SC I.T PART 2";
    string str2='K.C COLLEGE, COLABA';
    string str3=new string(20);
    function getstr1() public returns(string memory)
    {
        return str1;   }
    function getstr2() public returns(string memory)
    {
        return str2;  }
    function getstr3() public returns(string memory)
    {
        return str3;
    }}
