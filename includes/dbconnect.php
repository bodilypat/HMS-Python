<?php

    /* Database credentials */
    $host = 'localhost';
    $db = 'dblibrary';
    $user = 'root';
    $pass = '';
    $charset = 'utf8mb4';

    /* Data Source Name (DSN) */
    $dsn = "mysql:host=$host;dbname=$db;charset=$charset";

    /* PDO options */
    $options = [
        PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        PDO::ATTR_EMULATE_PREPARES    => false,
    ];

    try {
        /* Create a new PDO instance */
        $pdo  = new PDO($dsn, $user, $pass, $options);
        echo "Connected successfully";
        /* For debugging purposes */
    } catch (\PDOException $e){
        /* Handle connection error */
        throw new \PDOException($e->getMessage(), (int)$e->getCode());
    }
?>
