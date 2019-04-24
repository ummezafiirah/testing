<?php
header ('Location: https://facebook.com');
class DB_Connect
{
    public function connect()
    {
      $host        = "ec2-54-246-92-116.eu-west-1.compute.amazonaws.com";
      $port        = "port=5432";
      $dbname      = "d2qib7ffhl0bav";
      $credentials = "user=lgxawseqtudbve password=1585c0b862c065144db2cc12116b0fbbd6350af41027b670480b7e47acafb176";

      $db = pg_connect( " $url $host $port $dbname $credentials"  );
      if(!$db){
         echo "Error : Unable to open database\n";
      } else {
         echo "Opened database successfully\n";
      }
      return $db;
    }
}
    $db1 = new DB_Connect();
    $conn = $db1->connect();

foreach($_POST as $variable => $value) {
    echo $variable;
    echo "=";
    echo $value;
    echo "\r\n";
}
echo "\r\n\n\n\n";

exit;
   
?>
