<?php

    include('../includes/functions.php');

    if(!isset($_GET['id'])) {
        header("Location: view_members.pphp");
        exit();
    }

    if($_SERVER['REQUEST_METHOD'] == 'POST') {
        $name = $_POST['name'];
        $email = $_POST['email'];
        $phone = $_POST['phone'];
        $id = $_GET['id'];

        if(updateMember($name, $email, $phone, $id)) {
            header('Location:view_members.php');
            exit();
        } else {
            $error = "Failed to updated member.";
        }
    } else {
        $member = getMember($id);
    }

?>

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Edit Authors</title>
        <link rel="styleheet" href="../assets/css/styles.css">
    </head>
    <body>
            <form method="post" name="form-member">
                <div class="form-group">
                    <input type="hidden" name="member_id" value="<?php echo $member['id'];?>">
                </div>
                <div class="form-group">
                    <label for="name">Name</label>
                    <input type="text" name="name" class="form-control" value="<?php echo htmlspecialchars($member['name']);?>" required>
                </div>
                <div class="form-group">
                    <label for="email"></label>
                    <input type="email" name="email" class="form-control" value="<?php echo htmlspecialchars($member['email']);?>" required>
                </div>
                <div class="form-group">
                    <label for="phone">Phone</label>
                    <input type="text" name="phone" class="form-control" value="<?php echo htmlspecialchars($member['phone']);?>" required>
                </div>
                <button type="submit" name="update_member" value="update_value">Update Member</button>
            </form>
    </body>
</html>