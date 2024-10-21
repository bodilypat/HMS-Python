<?php

    include('../includes/functions.php');

    if(isset($_GET['id'])){
        $id = $_GET['id'];
        
        /* Fetch members to confirm deletion */
        $member = getMemberById($id);

        if(!$member) {
            die("Member not found");
        }

        if($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['confirm'])) {
            if(deleteMember($id)) {
                echo "Member deleted successfull!";
                /* Optionally redirect to member page */
                header("Location: view_members.php");
                exit();
            } else {
                echo "Error deleting Member.";
            }
        }
    } else {
        echo "No member ID provided.";
    }
?>
