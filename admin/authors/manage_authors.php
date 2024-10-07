<?php

    require '../includes/functions.php';

    $id = $_GET['id'];
    $name = $_POST['name'];
    $biography = $_POST['biography'];
    $date_of_birth = $_POST['date_of_birth'];

    /* Process form submission */
    if($_SERVER['REQUEST_METHOD'] === 'POST') {
        if(isset($_POST['add'])){
            addAuthor($name, $biography, $date_of_birth);
        } elseif (isset($_POST['update'])) {
            updateAuthor($id, $name, $biography, $date_of_birth);
        }
    }

    /* Handle deletions via GET request */

    if(isset($_GET['delete'])){
        deleteAuthor($_GET['delete']);
        header("Location: manage_authors.php"); // Redirect to avoid resubmission
        exit();
    }

    $authors = getAuthors();
?>
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Manage Authors</title>
        <link rel="stylesheet" href="../assets/css/styles.css">
    </head>
    <body>
        <h1>Manage Authors</h1>
        <form action="" method="post">
            <div class="form-group">
                <label for="name">Name</label>
                <input type="text" name="name" class="form-control" placeholder="Name" required>
            </div>
            <div class="form-group">
                <label for="biography">Biography</label>
                <textarea name="biography" name="biography" class="form-control" placeholder="Bigraphy" required>
            </div>
            <div class="form-group">
                <label for="DateOfBirth">Date of Birth</label>
                <input type="date" name="date_of_birth" class="form-control" placeholder="Date of birth" required>
            </div>
            <button type="submit" name="add">Add Author</button>
        </form>

        <h2>Author List</h2>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Biography</th>
                    <th>Date of Birth</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <?php foreach($authors as $author): ?>
            <tbody>
                <tr>
                    <td><?php htmlspecialchars($author['id']);?></td>
                    <td><?php htmlspecialchars($author['name']);?></td>
                    <td><?php htmlspecialchars($author['biography']);?></td>
                    <td><?php htmlspecialchars($author['date_of_date']);?></td>
                    <td>
                        <a href="edit_author.php?id=<?php $author['id']; ?>">Edit</a>
                        <a href="delete_author.php?id=<?php $author['id']; ?>" 
                           class="btn btn-danger btn-sm" onClick="return confirm('Are you sure ?')">Delete</a>
                    </td>
                </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
        <a href="add_author.php" class="btn btn-primary">Add New Author</a>
    </body>
</html>