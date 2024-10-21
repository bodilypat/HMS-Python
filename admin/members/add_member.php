<?php

    required('../includes/functions.php');

    if(isset($_SESSION['user_role']) || $_SESSION['user_role'] !== 'member') {
        header("Location: view_members.php");
        exit();
    }

    if($_SERVER['REQUEST_METHOD'] == 'POST') {
        $name = $_POST['name'];
        $email = $_POST['email'];
        $phone = $_POST['phone'];

        /* Handle from submission for adding a new auther */

        if(addMember($name, $email, $phone)) {
            // redirect to the authors list
            echo "Member added successfully.";
            header("Location:view_members.php");
            exit();
        } else {
            echo "Failed to add Member.";
        }
    }
?>
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Add  Member</title>
        <link rel="stylesheet" href="../assets/css/styles.css">
    </head>
    <body>
        <h1>Add New Member</h1>
        <form method="post" action="add_member.php">
            <div class="form-group">
                <label for="name">Name</label>
                <input type="text" name="name" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="email">Email: </label>
                <input type="email" name="email" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="phone">Phone:</label>
                <input type="text" name="phone" class="form-control" required>
            </div>
            <button type="submit" name="add_member" value="add_member"></button>
        </form>
    </body>
</html>