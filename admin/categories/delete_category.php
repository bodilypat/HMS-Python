<?php

    include('../includes/functions.php');

    if(isset($_GET['id'])) {
        $id = $_GET['id'];

        /* Fatch category by Id */
        $category = getCategoryById($id);
        /* function getCategoryById($id){
           $pdo = dbconnect();
           $stmt = $pdo->prepare("SELECT * FROM categories WHERE id = ? ")
           $stmt->execute([$id]);
           return $stmt->fetch();
        } 
        */
        if(!category){
            die("category not found");
        }

        if($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['confirm'])) {
            if(deleteCategory($id)) {

                /* 
                function deleteCategory($id){
                   $pdo = dbconnect();
                   $stmt = $pdo->prepare("DELETE FROM categiries WHERE id = ? ");
                   $delCategory = $stmt->execute([$id]);
                   
                   if($delCategory){
                        return "Category deleted successfully!."}
                   else {
                        return "Error deleting category"; 
                    } 
                }
                */
                echo "Category deleted successfully!";
            } else {
                echo "Error Deleting Category"
            }
        }
    } else {
        echo "no category ID provided.";
        exit();
    }
?>
