<?php

    include('../includes/functions.php');

    if($_SERVER['REQUEST_METHOD'] === 'POST'){
        $book_id = $_POST['book_id'];
        $user_name = $_POST['user_name'];
        $borrow_date = $_POST['borrow_date'];
        $return_date= $_POST['return']

        /* Call the function to borrow the book  */
        if(borrowBook($book_id, $user_name, $borrow_date, $return_date )) {
            header("Location: view_books.php");
            exit();
        } else {
            echo "Failed to borrow the book.";
        }
    }
?>

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Borrow Book</title>
    </head>
    <body>
        <h1>Borrow a Book</h1>
        <form method="POST">
            <div class="form-group">
                <label for="Book">Book:</label>
                <select name="book_id" required>
                    <?php
                        /* Fetch data books */
                        $books = getBooks();
                        foreach($books as $book): ?>
                            <option value="<?php echo $book['book_id'];?>"><?php echo $book['book_name'];?></option>
                    <?php endforeach; ?>
                </select>
            </div>
            <div class="form-group">
                <label for="user">User</label>
                <select value="user_id" required>
                    <?php 
                        /* Fetch data user */
                        $users = getUsers();
                        foreach($users as $user): ?>
                            <option value="<?php echo $user['user_id'];?>"><?php echo $user['user_name'];?></option>
                    <?php endforeach; ?>
                </select>
            </div>
            <div class="form-group">
                <label for="borrow_date">Borrower Date</label>
                <input type="datetime-locate" name="borrow_date" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="return_date">Return Date</label>
                <input type="return_date" name="return_date" class="form-control">
            </div>
            <button type="submit" name="add" value="add">Add Borrow</button>
        </form>        
    </body>
</html>