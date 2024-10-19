<?php

    include('../includes/functions.php');

    if($isset($_GET['id'])) {
        $borrow_id = $_GET['id'];

        /* Fetch borrows to confirm deletion */
        $borrow = getBorrowById($borrow_id);

        if(!$borrow){
            die("Borrow not found");
        }

        if($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['confirm'])){
            if(deleteBorrow($borrow_id)){
                echo "Borrow deleted successfull!";
                header("Location:view_borrows.php");
                exit();
            } else {
                echo "Error deleting borrow";
            }
        }
    } else {
        echo "No Borrow ID provided";
    }
?>