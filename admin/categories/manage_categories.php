<?php

    include('../includes/functions.php'); // Include the function 

    if(!isset($_SESSION['user_id'])) {
        header('Location:login.php'); // Redirect to login if not login
    }

    /* Fetch categories from the database */
    $categories = getCategories();
    /* function getCategories(){
            $pdo = dbconnect();
            $stmt = $pdo->prepare("SELECT * FROM categories ");
            $stmt->execute();
            return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } */          
?>
<!-- Front End Management -->
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Edit Category</title>
        <link rel="stylesheet" href="../assets/css/styles.css">
    </head>
    <body>
        <h1>Edit Category</h1>
        <a href="add_category.php"></a>
        <table>
                <tr>
                     <th>ID</th>
                     <th>Category Name</th>
                     <th>Actions</th>
                </tr>
                <?php foreach($categories as $category): ?>
                <tr>
                     <td><?php echo htmlspecialchars($category['id']);?></td>
                     <td><?php echo htmlspecialchars($category['name']);?></td>
                     <td>
                        <a href="edit_category.php?id=<?php echo $category['id'];?>">Edit</a>
                        <a href="delete_category.php?id=<?php echo $category['name'];?>" 
                           onClick="return confirm('Are you sure want to delete this category');">Delete</a>
                     </td>
                </tr>
                <?php endforeach; ?>
        </table>
    </body>
</html>
