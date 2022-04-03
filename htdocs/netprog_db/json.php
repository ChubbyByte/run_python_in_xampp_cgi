<?php

require('connect.php');

$sql = mysqli_query($conn, "SELECT * FROM student");

// $row = mysqli_fetch_array($sql, MYSQLI_ASSOC);
// echo json_encode($row)

$my_json_format = "[";
while($row = mysqli_fetch_array($sql, MYSQLI_ASSOC)){
  $my_json_format .= json_encode($row) . ",";
}
$my_json_format = substr_replace($my_json_format, "]", -1);

echo $my_json_format;

?>
