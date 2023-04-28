pragma solidity >=0.7.0 <0.9.0;
contract Arrray{
    uint[] nums=[1,2,33,21];

    function getlength() public returns(uint){
        return nums.length;
    }

	function pop() public{
		delete nums[1];
	}
	function push() public returns (uint[] memory){
		nums.push(7);
		return nums;
	}
function push1(uint i) public{
       		 nums.push(i);
    	}
}
