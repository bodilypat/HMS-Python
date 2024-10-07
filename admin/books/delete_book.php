<?php

    require '../includes/functions.php';
    if(isset($_GET['id'])){
        deleteBook($_GET['id']);
        header("Location:manage_books.php");
        exit();
    } else {
        header("Location:manage_books.php");
        exit();
    }
?>