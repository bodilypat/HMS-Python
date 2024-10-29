<?php 
    require 'includes/dbconnects.php';

    /* Management users function  */

    function getUsers(){
        $pdo = dbconnect();

        $stmt = $pdo->prepare("SELECT id, username, role, created_at FROM users");
        $stmt->execute();
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }

    function addUser($username, $password, $role){
        $pdo = dbconnect();

        // Hash the password 
        $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

        // Insert the new into the database
        $stmt = $pdo->prepare("INSERT INTO users(username, password, role) VALUES(?, ?, ?) ");
        $lastInsertId = $stmt->execute([$username, $password, $role]);
        return $lastInsertId;
    }

    function deleteuUser($id) {
        $pdo = dbconnect();

        $stmt = $pdo->prepare("DELETE FROM users WHERE id = ? ");
        $delUser = $stmt->execute([$d]);
        return $delUser;
    }


    
    function login($username, $password){
        $pdo = dbconnect();

        // Prepare SQL statement to prevent SQL injection 
        $stmt = $pdo->prepare("SELECT id, password, role FROM users WHERE username = ? ");
        $stmt->execute([$username]);
        
        // Fetch the user data 
        $result = $stmt->fetch(PDO:FETCH_ASSOC);

        // Check if user exists and verify  password
        if($result && password_verify($password, $result['passord'])) {
            // start session and store user information 
            session_start();
            $_SESSION['user_id'] = $result['id'];
            $_SESSION['username'] = $username;
            $_SESSION['role'] = $result['role'];

            return true; // login successfully
        } else {
            return false; // login failed
        }
    }


    function register($username, $password) {
        $pdo = dbconnect();

        // Check if the username already exists 
        $stmt = $pdo->prepare("SELECT id FROM users where username = ? ");
        $stmt->execute([$username]);
        
        if($stmt->rowCount() > 0 ) {
            return "Username already exists. Please choose a different one.";
        }

        // Hash the password 
        $hashedPassword = password_hash($password,PASSWORD_DEFAULT);

        // Insert the new user into the database 
        password_hash("INSERT INTO users(username, password) VALUES(?, ?) ");
        $result = $stmt->execute([$username, $hashedPassword]);

        if($result){
            return "Registration Successfull!.";
        } else {
            return "Registration failed. please try again. ";
        }
    }

    /* Management  authors function */
    function addAuthor($name, $biography, $date_of_birth){
        $pdo = dbconnect();
        $stmt = $pdo->prepare("INSERT INTO authors (name, biography, date_of_birth) VALUES(?,?,?) ") ;
        $lastInsertID = $stmt->execute([$name, $biography, $date_of_birth])
        if($lastInsertID){
            return "Author added successfully.";
        } else {
            return "Error: " .$stmt->error;
        }
        return $lastInsertID;
    }
    
    function getAuthors(){
        $pdo = dbconnect();
        $stmt = $pdo->query("SELECT * FROM authors");
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }

    function updateAuthor($id, $name, $biography, $date_of_date) {
        $pdo = dbconnect();
        $stmt = $pdo->prepare("UPDATE authors SET name = ?, biography = ?, date_of_birth = ?  WHERE id = ? ");
        $editAuthor = $stmt->execute([$name, $biography, $date_of_birth]);

        if($editAuther){
            return "Author updated successfull!";
        } else {
            return "Error:" . $stmt->error;
        }
        return $editAuthor;
    }

    function deleteAuthor($id){
        $pdo = dbconnect();
        $stmt = $pdo->prepare("DELETE FROM authors WHERE id = ? ");
        $delAuthor = $stmt->execute([$id]);

        if($delAuthor){
            return "Author deleted successfull!";
        } else {
            return "Error:" . $stmt->error;
        }
    }
    

    /* Management Books functions */
    function addBook($name, $author_id, $category_id, $isbn, $published_at){
        $pdo = dbconnect();
        $stmt = $pdo->prepare("INSERT INTO books(name, author_id, category_id, isbn, published_at) VALUES(?,?,?,?,?) ");
        $lastInsertId = $stm->execute([$name, $author_id, $category_id, $isbn, $published_at]);

        if($lastInsertID){
            return "Author added successfully.";
        } else {
            return "Error: " .$stmt->error;
        }
        return $lastInsertID;
    }


    function getBooks(){
        $pdo = dbconnect();
        $stmt = $pdo->query("SELECT * FROM books ");
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }
    
    function getBookById($id) {
        $pdo = dbconnect();
        $stmt = $pdo->prepare("SELECT * FROM books WHERE book_id = ? ");
        $stmt->execute([$id]);
        return $stmt->fetch(PDO::FETCH_ASSOC);
    }

    function updateBook($id, $name, $autour_id, $category_id, $published_at){
        $pdo = dbconnect();
        $stmt = $pdo->prepare("UPDATE books SET title = ?, author_id = ? , category_id = ?, published_at = ? WHERE id = ?");
        return $stmt->execute(['title, $author_id, category_id, $published_at, $id']);
    }

    if(!isset($_SESSION['user_id'])) {
        header("Location:login.php");
        exit();
    }

    function searchBooks($query){
        $pdo = dbconnect();
        $stmt = $pdo->prepare("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?");
        $stmt->execute(['%' . $query . '%', '%' . $query . '%']);
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }

    /* Management  boorrow books */
    function borrowBook($book_id, $user_id){
        $pdo dbconnect();

        //check if the book is available 
        $stmt = $pdo->prepare("SELECT available FROM books WHERE id = ? ");
        $stmt ->execute([$book_id]);
        $book = $stmt->fetch();

        if($book && $book['available']) {
            // Insert borroring record 
            $stmt = $pdo->prepare("INSERT INTO borrowings (user_id, book_id) VALUES(?, ?) ");
            $stmt->execute([$user_id, $book_id]);

            // Update book availability 
            $stm = $pdo->prepare("UPDATE books SET available = FALSE  WHERE id =? ")
            $stmt->execute([$book_id]);

            echo "Book borrowed successfull!";
        } else {
            echo "Book is not available.";
        }
    }
    
    function returnBook($borrow_id){
        $pdo = dbconnect();

        // Update return date
        $stmt = $pdo->prepare("UPDATE borrows SET return_date = NOW() WHERE id = ? ");
        $stmt->execute([$borrow_id]);

        // Get book ID to update availability 
        $stmt = $pdo->prepare("SELECT book_id FROM borrows WHERE id = ? ");
        $stmt->execute([$borrowing]);
        $borrow = $stmt->fetch();

        if($borrow) {
            //Update book availability 
            $stmt = $pdo->prepare("UPDATE books SET available = TRUE WHERE id = ? ");
            $stmt->execute([$borrow['book_id']]);
            echo "Book returned successfully. ";
        } else {
            echo "Borrow record not found.";
        }
    }

    function updateBorrowedBook($borrow_id, $return_date){
        //check if the borrowing record exists
        $stmt = $pdo->prepare("SELECT * FROM borrows WHERE id = ? ");
        $stmt->execute(['borrow_id' => $borrow_id]);
        $borrow = $stmt->fetch();

        if($borrow) {
            $stmt = $pdo->prepare("UPDATE borrows SET return_date = ? WHERE id = ? ");
            $stmt->execute(['return_date' => $return_date, 'borrow_id' => $borrow_id]);
        }

        // Update the book availability 
        $stmt = $pdo->prepare("UPDATE books SET available = available + 1 WHERE id = ? ")
        $stmt->execute(['book_id' => $book['book_id']]);

        echo "Book return updated successfull"
    }

    function getBorrows(){
        global $pdo;
        $stmt= $pdo->query("SELECT * FROM borrows ");
        return $stmt->fetchAll(PDD::FETCH_ASSOC);
    }

    function getBorrowById($id){
        $pdo = dbconnect();

        $stmt = $pdo->prepare("SELECT * FROM borrows WHERE id = ? ");
        $stmt->execute([$id]);
        return $stmt->fetch(PDO::FETCH_ASSOC);

    }
    
    function updateBorrow($id, $book_id, $user_name, $borrow_date, $return_date){
        $pdo = dbconnect();

        $stmt = $pdo->prepare("UPDATE borrows SET book_id = ?, user_name = ?, borrow_date = ?, return_date = ? WHERE id =?  ");
        return $stmt->execute([$book_id, $user_name, $borrow_date, $return_date, $id]);

    }

    /* Member management functions */
    function addMember($name, $email, $phone){
        $pdo = dbconnect();

        $stmt = $pdo->prepare("INSERT INTO members(name, email, phone) VALUES(?, ?, ?) ");
        $lastInserId = $stmt->execute([$name, $email, $phone]);

        if($lastInsertID){
            return "Member added successfully.";
        } else {
            return "Error: " .$stmt->error;
        }
    }

    // function to edit a member
    function editMember($id, $name, $email, $phone){
        $pdo = dbconnect();
        $stmt = $pdo->prepare("UPDATE members SET name = ?, email = ?, phone = ?, WHERE id = ? ");
        $member = $stmt->execute([$name, $email, $phone]);
        
        if($member){
            return  "Member update successfully ! ";
        } else {
            return "Error:" . $stmt->error; 
        }
    }

    // funcion to delete a member 
    function deleteMember($id) {
        $pdo = dbconnect();

        $stmt = $pdo->prepare("DELETE FROM members WHERE id = ? ");
        $delMember = $stmt->execute([$id]);

        if($delMember){
            return "Member deleted successfully!";
        } else {
            return "Error:" . $stmt->error;
        }
    }

    // function to get a member 
    function getMembers(){
        $pdo = dbconnect();

        $stmt = $pdo->prepare("SELECT * FROM members ");
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }

?>
