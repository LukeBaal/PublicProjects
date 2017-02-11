<html>
<head>
  <link href="css/stylesheet.css" rel="stylesheet" type="text/css"/>
</head>
<body>
  <?php
    $exp = $_POST["exp"];
    //$inCount = $_POST["inCount"];
    $inCount = 4;
    $exp = str_replace("*","&&",$exp);
    $exp = str_replace("+","||",$exp);

    echo '<table>';
    for($k=1;$k<=$inCount; $k++){
      echo '<th>Input'.$k.'</th>';
    };

    echo '<th>X</th>';
    $x = pow(2,$inCount);
    for($i=0; $i < $x; $i++){
      $bin = sprintf("%0".$inCount."d", decbin($i));
      echo '<tr>';
      for($j=0; $j<strlen($bin); $j++){
        echo '<td>'.$bin[$j].'</td>';
      };
      $new_exp = str_replace("A",$bin[0],$exp);
      $new_exp = str_replace("B",$bin[1],$new_exp);
      $new_exp = str_replace("C",$bin[2],$new_exp);
      $new_exp = str_replace("D",$bin[3],$new_exp);

      //$str = $bin[0].'&&'.$bin[1].'||'.$bin[2].'&&'.$bin[3];
      eval("\$result=$new_exp;");
      if ($result){
        echo '<td>'.$result.'</td>';
      }else{
        echo '<td>0</td>';
      };



      echo '</tr>';
    };

    echo '<table>';
  ?>
</body>
</html>
