<?php
$path=realpath('./up/');

if (empty($_REQUEST['pass']) or $_REQUEST['pass']!='qwerty') {
	die('wrong secret'.PHP_EOL);
}

if (!empty($_FILES['file']) and $file=$_FILES['file']) {
	$path=$path.'/'.$file['name'];
	move_uploaded_file($file['tmp_name'],$path );
}
?>
