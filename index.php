<?php

    include('../includes/functions.php'); // include the login function 

    if($_SERVER['REQUEST_METHOD'] == 'POST') {
        $usernamee = $_POST['username'];
        $password = $_POST['password'];

        /* Call login function  */
        if(login($username, $password)) {
            // Redirect to a protected  page ( dashboard )
            header("Location:index.php");
            exit();
        } else {
            $error = "Invalid username or password.";
        }
    }
?>
<!-- Front End  -->
<!DOCTYPE html>
<html lan="en">
    <head>
        <meta charset="UTF-8">
        <title>Login</title>
        <link rel="stylesheet" href="../assets/css/styles.css">
    </head>
    <body>
        <header>
            <h1>Login to Library Management system</h1>
        </header>
        <main>
            <form action="login.php" method="POST">
                <div>
                    <label for="username">Username: </label>
                    <input type="text" name="username" required>
                </div>
                <div>
                    <label for="password">Password: </label>
                    <input type="password" name="password" required>
                </div>
                <button type="submit">Login</button>
            </form>
            <?php
                if(isset($error)) : ?>
                    <p style="color:red;"><?php htmlspecialchars($error); ?></p>
            <?php endif; ?>
        </main>
    </body>
</html>