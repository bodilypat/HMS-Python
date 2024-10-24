<?php
    includes('../includes/functions.php'); // include function

    if(!isset($_SESSION['user_id'])){
        header("Location:login.php"); // Redirect to login if not login 
        exit();
    }

    /* Fetch categories by id for editing */
    if(isset($_get['id '])) {
        $category = getCategoryById($id);

        /* function getCategoryById($id){
               $pdo = dbconnect();
               $stmt = $pdo->prepare("SELECT * FROM categories WHERE id = $id ");
               $stmt->execute([$id]);
               return $stmt->fetch();
        } 
        */
        if(!$category) {
            die('Category not found')
        }
    }
    /* Handle form submission for updating the category */
    if($_SERVER['REQUEST_METHOD'] == 'POST') {
        $name = $_POST['name'];

        if(updateCategory($name)){
            echo "Category update successfull!";
            header("Location:manage_categories.php");
            exit();
        } else {
            echo "Failed to update category"
        }
    }
?>

<!-- Front End Management -->
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Edit Category</title>
        <link rel="styleshee" href="../assets/css/styles.css">
    </head>
    <body>
        <h1>Edit Category</h1>
        <form method="post">
            <input type="hidden" name="id" value="<?php $category['id'];?>">
            <div class="form-group">
                <label for="Name">Name</label>
                <input type="text" name="name" value="<?php echo $category['name']; ?>" required>
            </div>
            <button type="submit" name="update" value="update">Update Category</button>
        </form>
        <a href="manage_categories.php">Back to Manage Categories</a>
    </body>
</html>