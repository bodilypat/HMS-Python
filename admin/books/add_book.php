<?php

    require '../includes/functions.php';

    if($_SERVER['REQUEST_METHOD'] =='POST'){
        $title = $_POST['title'];
        $author_id = $_POST['author_id'];
        $publisher_id = $_POST['publisher_id'];
        $isbn = $_POST['isbn'];
        $available = $POST['available'] ;
    }
?>
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Add Book</title>
    </head>
    <body>
        <h2>Add Book</h2>
        <?php if(isset($error)) echo "<p style='color:red;'>$error</p>"; ?>
        <form method="post" name="form-purchase">
            <div class="form-group">
                <label for="title">Title</label>
                <input type="text" name="title" class="form-control" placeholder="Title" required>
            </div>

            <div class="form-group">
                <label for="author">Author</label>
                <select name="author_id" required>
                    <?php $authors = getAuthors(); foreach($authors as $author): ?>
                            <option value="<?php echo $author['id'];?>"><?php echo $author['name'];?></option>
                    <?php endforeach; ?>
                </select>
            </div>

            <div class="form-group">
                <label for="publisher">Publisher</label>
                <select name="publisher_id" required>
                    <?php $publishers = $getPulishers(); foreach($publishers as $publisher): ?>
                        <option value="<?php echo $publisher['id'];?>"><?php echo $publisher['name'];?></option>
                    <?php endforeach; ?>
                </section>
            </div>

            <div class="form-group">
                <label for="ISBN">ISBN</label>
                <input type="text" name="isbn" class="form-control" placeholder="ISBN" required>
            </div>
            <div class="form-group">
                <label for="status">Status</label>
                <select name="status" required>
                    <option value="available">available</option>
                    <option value="notavailable">not avaialable</option>
                </select>
            </div>
            <button type="submit" >Add Book</button>
        </form>
        <a href="manage_books.php">Manage Books</a>
    </body>
</html>