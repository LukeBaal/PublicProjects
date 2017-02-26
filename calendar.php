<html lang='en' xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta charset = "utf-8" />
	<title>Calendar</title>
	<link href="CalendarTable.css" rel="stylesheet" type="text/css"/>
	
</head>
<body>
	<?php
		// Get the date from the form post
		$date = $_POST["date"];
		$dataArray = [[], [], [], [], [], []];
		
		// If the month is a single digit, ignore the 0
		if ($date[5] == 0){
			$month = $date[6];
		}else{
			$month = $date[5].$date[6];
		};
		
		//$monthName = $MONTHS[$month-1];
		$m = strtotime($date.'-01');
		$d = date("Y-F-d-l", $m);
		$dArray = explode('-', $d);
		
		$lastDay = date("t", $m);
		
		//Since months don't always begin on same day, find offset
		$offset = (int) date("w", $m);
		
		echo '<table>
					<caption><strong>'.$dArray[1].'</strong></caption>
					<th>Sunday</th>
					<th>Monday</th>
					<th>Tuesday</th>
					<th>Wednesday</th>
					<th>Thursday</th>
					<th>Friday</th>
					<th>Saturday</th>';
		
		//Create the calendar table with correct day numbering
		for($i=0; $i < 6; $i++){
			echo '<tr>';
			for($j=1; $j < 8; $j++){
				echo '<td>';
				
				//if the first of the month has not occured,
				//then skip numbering for that cell
				if(($i == 0 && $j <= $offset) || ($i >= 4 && ($i*7+$j-$offset) > (int)$lastDay)){
					$dataArray[$i][] = "X";
					echo '</td>';
					continue;
				};
				
				$dataArray[$i][] = $i*7+$j-$offset;
				echo $i*7+$j-$offset.'</td>';
			};
			echo '</tr>';
		};
		echo '</table>';
		
		foreach ($dataArray as $thing){
			echo $thing[0].',';
			echo $thing[1].',';
			echo $thing[2].',';
			echo $thing[3].',';
			echo $thing[4].',';
			echo $thing[5].',';
			echo $thing[6].'</br>';
		};
		
		//-------------------------------------------------------------
		
		//SAVE TO SQL DB
		
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
		echo "connected to db!";
		//sql to create table
		/*$sql = "CREATE TABLE April ( 
		//id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
		sunday VARCHAR(30) NOT NULL,
		monday VARCHAR(30) NOT NULL,
		tuesday VARCHAR(30) NOT NULL,
		wednesday VARCHAR(30) NOT NULL,
		thursday VARCHAR(30) NOT NULL,
		friday VARCHAR(30) NOT NULL,
		saturday VARCHAR(30) NOT NULL
		)";*/
		
		/*$sql = "INSERT INTO myGuests (firstname, lastname, email)
		VALUES ('John', 'Doe', 'john@example.com')";*/
		
		//Prepare and bind
		$stmt = $conn->prepare("INSERT INTO April (sunday, monday, tuesday, wednesday, thursday, friday, saturday) 
		VALUES (?, ?, ?, ?, ?, ?, ?)");
		$stmt->bind_param("sssssss", $sun, $mon, $tue, $wed, $thu, $fri, $sat);
		
		foreach($dataArray as $week){
			$sun = (string)$week[0];
			$mon = (string)$week[1];
			$tue = (string)$week[2];
			$wed = (string)$week[3];
			$thu = (string)$week[4];
			$fri = (string)$week[5];
			$sat = (string)$week[6];
			$stmt->execute();
		};
		
		echo "New Records created!";
		
		$stmt->close();
		mysqli_close($conn); 	
	?>
</body>
</html>

