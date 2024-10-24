<?php
    session_start();
    include('../includes/functions.php');

    /*  Check if the user is logged in */
    if(!isset($_SESSION['user_id'])){
        header("Location: login.php"); // Redirect to login if not logged in
        exit();
    }

    // Handle form submission

    if($_SERVER['REQUEST_METHOD'] == 'POST') {
        $name = $POST['name'];

        // call function addCategory 
        if(addCategory($name)){
            echo " add category successfully";
            header("Location:manage_books.php");
        } else {
            echo "Failed add category";
        }

        // Redirect to the manage categories  after successfully addition 
        header("Location: manage_categories.php");
        exit();
    }
?>

<!-- Front end management -->
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Add Category</title>
        <link rel="stylesheet" href="../assets/css/styles.css">
    </head>
    <body>
        <h1>Add New Category</h1>
        <form method="post">
            <div class="form-group">
                <label for="name">Category:</label>
                <input type="text" name="name" class="form-control" placeholder="Category Name required">
            </div>
            <button type="submit" name="add" value="add">Add Category</button>
        </form>
    </body>
<html>