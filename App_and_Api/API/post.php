<?php
   $con=mysqli_connect("127.0.0.1", "root", "Rootpass21!", "secHomeAutomation");

   if (mysqli_connect_errno($con)) {
      echo "Failed to connect to MySQL: " . mysqli_connect_error();
   }

   $device_name = $_POST['device_name'];
   
   $result = mysqli_query($con,"INSERT INTO deviceInfo (device_name) VALUES ('$device_name')");
   $row = mysqli_fetch_array($result);
   $data = $row[0];

   if($data){
      echo $data;
   }
   mysqli_close($con);
?>
