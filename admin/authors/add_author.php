<?php

    require '../includes/functions.php';

    /* Check if the user is logged in and is an admin */
    if(!isset($_SESSION['user_role']) || $_SESSION['user_role'] !== 'admin') {
        header("Location: index.php");
        exit();
    } 

    if($_SERVER['REQUEST_METHOD'] == 'POST'){
        $name = $_POST['name'];;
        $biography = $_POST['biography'];
        $date_of_birth = $_POST['date_of_birth']

        /* Handle frpom submission for addding a new author */
        if(addAuthor($name, $biography, $date_of_birth))    {
            header("Location:view_authors.php"); // redirect to the authors list
            exit();
        } else {
            echo "Falied to add author.";
        }
    }
?>

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Add Author</title>
        <link rel="stylesheet" href="../assets/css/styles.css">
    </head>
    <body>
        <h1>Add New Author</h1>
        <form method="POST" action="add_author.php">
            <div class="form-group">
                <label for="Name">Name</label>
                <input type="text" name="name" class="form-control" placeholder="Name" required>
            </div>
            <div class="form-group">
                <label for="biography">Biography</label>
                <textarea name="biography" class="form-control" required></textarea>
            </div>
            <div class="form-group">
                <label for="Date_of_Birth">Date of Birth</label>
                <input type="text" name="date_of_birth" class="form-control" required>
            </div>
            <button type="text">Add Author</button>
        </form>
    </body>
</html>
    