<?php

    require '../includes/functions.php';
    if($_SERVER['REQUEST_METHOD'] == 'POST'){
        $id = $_POST['id'];
        $name = $_POST['name'];
        $biography = $_POST['biography'];
        $date_of_birth = $_POST['date_of_birth'];
        
        if(updateAuthor($id, $name, $biography, $date_of_birth)){
            echo "Author updated Successfull!";
        } else {
            echo "Failed to update Author.";
        }
        $authors = getAuthors();
    }
?>
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Edit Authors</title>
        <link rel="stylesheet" href="../assets/css/styles.css">
    </head>
    <body>
         <form method="post"  action="edit_author.php?id=<?php echo $author['id'];?>" >
             <div class="form-group">
                <input type="hidden" name="id"  value="<?php echo htmlspecialchars($author['id']);?>">
             </div>
             <div class="form-group">
                <label for="name">Name</label>
                <input type="text" name="name" class="form-control" value="<?php echo htmlspecialchars($author['name']);?>" required>
             </div>
             <div class="form-group">
                <label for="biography">Biography</label>
                <textarea name="biography" required><?php echo htmlspecialchars($author['biography']);?></textarea> 
             </div>
             <div class="form-group">
                <label for="date_of_birth">Date of Birth</label>
                <input type="date" name="birth_of_date" value="<?php echo htmlspecialchars($author['date_of_birth']);?>">
             </div>
             <button type="submit">Update author</button>
         </form>
    </body>
</html>