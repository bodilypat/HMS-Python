<?php

    require '../includes/functions.php';

    $books = getBooks();
?>
<!DOCTYPE html>
<html lang="en" >
    <head>
        <meta charset="UTF-8">
        <title>Books Management</title>
        <link rel="stylesheet" href="../assets/css/styles.css">
    </head>
    <body>
        <h1>Books List</h1>
        <a href="add.book.php">Add Book</a>
        <table border="1" >
            <thead>
                <tr>
                     <th>ID</th>
                     <th>title</th>
                     <th>author</th>
                     <th>pulisher</th>
                     <th>ISBN</th>
                     <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                <?php foreach($books as $book): ?>
                <tr>
                     <td><?php htmlspecialchars($book['id']);?></td>
                     <td><?php htmlspecialchars($book['title']);?></td>
                     <td><?php htmlspecialchars($book['author']);?></td>
                     <td><?php htmlspecialchars($book['pulisher']);?></td>
                     <td><?php htmlspecialchars($book['isbn']);?></td>
                     <td>
                        <a href="edit_book.php?id=<?php $book['id']?>">Edit</a>
                        <a href="delete_book.php?id=<?php $book['id']?>" class="btn btn-danger btn-sm" 
                           onClick="return confirm('Are you sure ? ')">Delete</a>
                     </td>
                </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
        <a href="add_book.php" class="btn btn-primary">Add Now Book</a>
    </body>
</html>