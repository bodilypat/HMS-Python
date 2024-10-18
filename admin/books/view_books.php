<?php

    include('../includes/functions.php');

    $books = getBooks();
?>
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>View Books</title>
    </head>
    <body>
        <h1>Book</h1>
        <a href="add_book.php">Add New book</a>
        <table border="1">
            <tr>
                 <th>Title</th>
                 <th>Book Name</th>
                 <th>Author</th>
                 <th>Pulishred_date</th>
                 <th>isbn</th>
                 <th>available</th>
                 <th>Actions</th>
            </tr>
            <?php foreach($books as $book): ?>
            <tr>
                 <td><?php echo $book['title'];?></td>
                 <td><?php echo $book['book_name'];?></td>
                 <td><?php echo $book['author_name'];?></td>
                 <td><?php echo $book['pulishered_data'];?></td>
                 <td><?php echo $book['isbn'];?></td>
                 <td><?php echo $book['available'];?></td>
                 <td>
                      <a href="edit_book.php?id<?php $book['id'];?>">Edit</a>
                      <a href="delete_book.php?id<?php $book['id'];?>" onClick="return confirm('Are you sure');">Delete</a>
                 </td>
            </tr>
            <?php endforeach; ?>
        </table>
    </body>
</html>