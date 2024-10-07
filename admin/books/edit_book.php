<?php

    require '../includes/functionsf.php';

    if($_SERVER['REQUEST_METHOD'] == 'POST'){
        $id = $_POST['id'];
        $name = $_POST['name']
        $author_id = $_POST['author_id'];
        $publisher_id = $_POST['publisher_id'];
        $isbn = $_POST['isbn'];
        $status = $_POST['status'];

        if(updateBook($id, $name, $authors_id, $publisher_id, $isbn, $status)) {
            echo "Book updated successfully!";
        } else {
            echo "Failed to update purchase.";
        }
    } else {
        /* Fetch current purchase details */
        $id = Get['id'];
        $book  = $getBooks();
    }
?>

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Edit Book</title>
    </head>
    <body>
        <form method="post" name="form-books">
            <div class="form-group">
                <input type="hidden" name="book_id" value="<?php htmlspecialchars($book['id']);?>">
            </div>
            <div class="form-group">
                <label for="author">Author</label>
                <select name="author_id" required>
                    <option value="">select authors"<option>
                        <?php $authors = getAuthors(); 
                            foreach($authors as $author){
                                $selected = ($book['id'] == $book['author_id']) ? 'selected' : '';
                                echo"<option value=\"{$book['id']}\" selected>({$author['name']}</option>";
                            }
                        ?>
                </select>
            </div>
            <div class="form-group">
                <label for="publisher_at">Publisher</label>
                <input type="text" name="publisher_at" class="form-control" placeholder="publisher" required>
            </div>
            <div class="form-group">
                <label for="ISBN">ISBN</label>
                <input type="text" name="isbn" class="form-control" placeholder="ISBN" required>
            </div>
            <div class="form-group">
                <label for="available">Available</label>
                <select name="avaliable" required>
                    <option value="">Status</option>
                    <option value="1">Available</option>
                    <option value="0">Not availabel</option>
                </select>
            </div>
            <button type="submit">Update Book</button>
        </form>
        <a href="view_books.php">Cancel</a>
    </book>
</html>