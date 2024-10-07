<?php

    require '.../includess/functions.php';

    if(isset($_GET['id'])){
        deleteAuthor($_GET['id']);
        header("location: manage_author.php");
    } else {
        header("location: manage_author.php")
        exit();
    }
?>
