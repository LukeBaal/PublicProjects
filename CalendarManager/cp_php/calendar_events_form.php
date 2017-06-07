<html lang='en' xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta charset = "utf-8" />
	<title>Calendar</title>
	<link href="CalendarTable.css" rel="stylesheet" type="text/css"/>

</head>
<body>
	<?php
		$day = $_POST["day"];
		$day = strtotime($day);
		$dayName = (string)date("l", $day);
		$dayName = strtolower($dayName);
		$day = (string)date("j", $day);
		$info = $_POST["info"];
		$info = nl2br($info);

		//SQL Code
		$server = "localhost";
		$user = "root";
		$pass = "4salt7";
		$dbname = "Calendar";

		//Create connection
		$conn = new mysqli($server, $user, $pass, $dbname);

		//Check connection
		if ($conn->connect_error){
			die("Connection failed: ".$conn->connect_error);
		};

		$sql = "UPDATE April SET ".$dayName."='".$day."</br>".$info."'
		WHERE ".$dayName."='".$day."'";
		
		if($conn->query($sql) === TRUE){
			echo "Recorded updated";
		}else{
			echo "Error updating: ".$conn->error;
		};
		$sql = "SELECT sunday, monday, tuesday, wednesday, thursday,
		friday, saturday
		FROM April";
		$result = $conn->query($sql);

		if($result->num_rows > 0){
			echo '<table>
			<caption>April</caption>
			<th>Sunday</th>
			<th>Monday</th>
			<th>Tuesday</th>
			<th>Wednesday</th>
			<th>Thursday</th>
			<th>Friday</th>
			<th>Saturday</th>';
			while($row = $result->fetch_assoc()){
				echo "<tr>";
				foreach($row as $val){
					echo "<td>".$val."</td>";
				};
				echo "</tr>";
			};
			echo "</table>";
		}else{
			echo "0 results";
		};

		$conn->close();
	?>
</body>
</html>
