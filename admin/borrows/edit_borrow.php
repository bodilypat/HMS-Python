<?php

    include('../incldues/functions.php');

    if(isset($_GET['id'])){
        $borrow_id = $_GET['id'];
        $borrow = getBorrowById($borrow_id);

        if(!$borrow){
            die("Artist not foudn");
        }

        if($_SERVER['REQUEST_METHOD'] === 'POST') {
            // Get form data 
            $book_id = $_POST['book_id'];
            $user_name = $_POST['user_id'];
            $borrow_date = $_POST['borrow_date'];
            $return_date = $_POST['return_date'];

            if(updateBorrow($book_id, $user_id, $borrow_date, $return_date)){
                echo "Borrow updated successfully! ";
                /* optionally redirect to another page */
                header('Location:view_borrow;');
                exit();
            } else {
                echo "Error update borrow.";
            }
        }
    } else {
        echo "No book ID provided."
    }
?>

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Edit Borrow</title>
    </head>
    <body>
        <h1>Edit Borrow</title>
        <form action="edit_borrow.php" method="POST">
            <input type="hidden" name="borrow_id" required>
            <div class="form-group">
                <label for="book">Book</label>
                <select name="book_id"  value="<?php echo $borrow['book_id'];?>" required>
                    <?php 
                    /* Fetch data Books */
                        $books = getBooks();
                        foreach($books as $book): ?>
                            <option value="<?php echo $book['book_id'];?>"><?php echo $book['book_name'];?></option>
                    <?php endforeach; ?>
                </select>
            </div>
            <duv class="form-group">
                <label for="user">User:</label>
                <select name="user_id" value="<?php echo $borrow['user_id'];?>" required>
                    <?php 
                    /* Fetch data Users */
                        $users = getUsers();
                        foreach ($users as $user): ?>
                            <option value="<?php echo $user['user_id'];?>"><?php echo $user['$user_name'];?></option>
                    <?php endforeach; ?>
                </select>
            </div>
            <div class="form-group">
                <label for="BorrowDate">Borrow Date</label>
                <input type="datetime-locate" name="borrow_date" value="<?php echo $borrow['borrow_date'];?>" >
            </div>
            <div class="form-group">
                <label for="ReturnDate">Return Date</label>
                <input type="datetime-locate" name="return_date" value="<?php echo $borrow['return_date'];?>">
            </div>
            <button type="submit" name="update" value="update borrow">update</button>
        </form>
        <a href="view_borrow.php"></a>
    </body>
</html>

    