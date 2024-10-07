<?php

    require '../includes/function.php';

    if($_SERVER['REQUEST_METHOD'] === 'POST'){

        $book_id = $_POST['book_id'];
        $borrow_name = $_POST['borrow_name'];
        $borrow_date = $_POST['borrow_date'];
        $due_date = $_POST['due_date'];


        if(isset($_POST['borrow'])) {
            borrowBook($book_id, $borrow_name, $borrow_date,$due_date);
        } elseif (isset($_POST['return'])){
            returnBook($_POST['id']);
        }
    }
?>

$borrows = getBorrows();
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Manage Borrows</title>
    </head>
    <body>
        <h1>Manage Borrowed Books</h1>
        <form name="book_id"  required>

            <div class="form-group">
                <select name="book_id" required>
                    <option value="">Select Book</option>
                        <?php $books = getBooks(); foreach($books as $book): ?>                
                            <option value="<?php $book['id'] ?>"><?php htmlspecialchars($book['name']) ?></option>                        
                        <?php endforeach; ?>
                </select>
            </div>

            <div class="form-group">
                <label for="borrowname">Borrow Name</label>
                <select name="member_id" required>
                    <option value="">member name</option>
                    <?php $members = getMembers(); foreach($members as $member): ?>
                        <option value="<?php $member['id']?>"><?php htmlspecialchars($member['name'])?></option>
                    <?php endforeach; ?>
                </select>
            </div>

            <div class="form-group">
                <label for="brrow_date">Borrow Date</label>
                <input type="date" name="borrow_date" class="form-control" required>
            </div>
            
            <div class="form-group">
                <label for="due_date">Due Date</label>
                <input type="text" name="due_date" class="form-control" required>
            </div>
            <button type="submit" name="borrow">Borrow Book</button>
        </form>

        <h1>Borrowed Books List</h1>
        <table>
            <tr>
                 <th>ID</th>
                 <th>Book Title</th>
                 <th>Borrower Name</th>
                 <th>Borrow Date</th>
                 <th>Due Date</th>   
                 <th>Return Date</th>
                 <th>Actions</th>
            </tr>
            <?php foreach($borrows as $borrow): ?>
            <tr>
                 <td><?php htmlspecialchars($borrw['id'])?></td>
                 <td><?php htmlspecialchars($borrow['title'])?></td>
                 <td><?php htmlspecialchars($borrow['borrower_name'])?></td>
                 <td><?php htmlspecialchars($borrow['due_date'])?></td>
                 <td><?php htmlspecialchars($borrow['due_date'])?></td>
                 <td><?php htmlspecialchars($borrow['return_date'])?></td>
                 <td>
                    <?php if(is_null($borrow['return_dae'])): ?>
                        <form action="" method="POST" style="display:inline; ">
                            <input type="hidden" name="id" value="<?php $borrow['id'] ?>">
                            <button type="submit" name="return">Return</button>
                        </form>
                    <?php else: ?>
                        returned
                    <?php endif; ?>
                 </td>
            </tr>
            <?php endforeach; ?>
        </table>
    </body>
</html>