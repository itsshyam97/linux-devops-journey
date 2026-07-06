<?php

$host = "mysql";
$user = "shyam";
$password = "password123";
$database = "compose_db";

$conn = new mysqli($host, $user, $password, $database);

if ($conn->connect_error) {
    die("<h2>Connection Failed: " . $conn->connect_error . "</h2>");
}

echo "<h1>🎉 Connected to MySQL successfully!</h1>";

$result = $conn->query("SELECT NOW() AS `current_time`");

$row = $result->fetch_assoc();

echo "<h2>Current DB Time:</h2>";
echo $row['current_time'];

$conn->close();

?>
