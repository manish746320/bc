pragma solidity >=0.7.0 <0.9.0;
   contract Demo{
      string public s1 = "Tanya ";
      string public s2 = "Panchal";
      string public new_str;

      function concatenate() public {
         new_str = string(abi.encodePacked(s1, s2));
       }
}
