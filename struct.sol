pragma solidity >=0.7.0 <0.9.0;
contract test{
    struct Book{
        string title;
        string author;
        string name;
        uint book_id;
    }
   Book book;
   function setBook() public{
       book = Book('SOLIDITY','JOHN','fantasy world',101);
   }

   function getBookId() public view returns(uint){
        return book.book_id;
   }

    function getName() public view returns(string memory){
        return book.name;
   }

   function getBookDeets() public view returns(string memory,string memory,string memory){
       return(book.title,book.name,book.author);
   }
}
