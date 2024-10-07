<?php 
    require 'includes/dblibrary.php';
    
    /* Function manage Books */
    function addBook($title, $author_id, $category_id, $isbn, $published_at){
        global $pdo;
        stmt = $pdo->prepare("INSERT INTO books(title, author_id, category_id, isbn, published_at) VALUES(?,?,?,?,?) ");
        return $stm->execute([$title, $author_id, $category_id, $isbn, $published_at]);
    }

    function listBooks(){
        global $pdo;
        $stmt = $pdo->query("SELECT * FROM books ");
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }

    function updateBook($id, $title, $autour_id, $category_id, $pulished_at){
        global $pdo;
        $stmt = $pdo->prepare("UPDATE books SET title = ?, author_id = ? , category_id = ?, published_at = ? WHERE id = ?");
        return $stmt->execute(['title, $author_id, category_id, $published_at, $id']);
    }

    function getBookDetails($bookId){
        global $pdo;
        $stmt = $pdo->prepare("SELECT * FROM books WHERE book_id = ? ");
        $stmt->execute([$bookId]);
        return $stmt->fetch(PDO::FETCH_ASSOC);
    }


    function borrowBook($userID, $bookID){
        global 4pdo;
        $loadDate = date('Y-m-d');
        $dueDate = date('Y-m-d', strtotime('+14 days'));
        $stmt = $pdo->prepare("INSERT INTO load(user_id, book_id, load_date, due_dae) VALUES(?, ?, ?, ?, ? ) ");
        $stmt->execute([$userId, $bookId, $loadDate, $dueDate]);

        /* update book availability */
        $stmt = $pdo->prepare("UPDATE books SET available = available-1 WHERE book_id = ? ");
        return $stmt->execute([$bookId]);
    }

    function returnBook($loadId){
        global $pdo;
        $returnDate = date('y-m-d');

        /* Update load record */
        $stmt = $pdo->prepare("UPDATE loads SET returned_date = ? WHERE load_id = ? ");
        $stmt->execute(['returnDate, $loadId']);

        /* Get book_id for availability update */
        $stmt = $pdo->prepare("SELECT book_id FROM loans WHERE load_id = ?");
        $stmt->execute([$loadId]);
        $bookId = $stmt->fetchColumn();

        /* Update book availability */
        $stmt = $pdo->prepare("UPDATE BOOKS SET available = available + 1 WHERE book_id = ?");
        return $stmt->execute([$bookId]);
    }

    function searchBooks($query){
        global $pdo;
        $stmt = $pdo->prepare("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?");
        $stmt->execute(['%' . $query . '%', '%' . $query . '%']);
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }

    function deleteBook($id){
        global $pdo;
        $stmt = $pdo->prepare("DELETE FROM books WHERE id = ? ");
        return $stmt->execute([$id]);
    }