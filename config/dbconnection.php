<?php
$host='localhost';
$database = 'library';
$username = 'root';
$password ='';

try{
  $pdo = new PDO('mysql:host=$host,dbname=$database,$user, $pass);
  $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION;
  } cath(PDOException $e) {
    echo 'connection failed : '$e->getMessage();
}
?>
