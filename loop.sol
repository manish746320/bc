pragma solidity >=0.7.0 <0.9.0;

contract while1{
uint[] data;
uint8 j=0;
function loop() public returns(uint[] memory)
{
    while (j<10)
    {
        j++;
        data.push(j);
    }
    return data;
}
}
