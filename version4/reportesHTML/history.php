<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>
	
<?php
	$directorio = opendir("."); //ruta inicial
	while ($archivo=readdir($directorio))
	{
		if (is_dir($archivo))//verifica si es o no un directorio
		{
			echo "[".$archivo . "]<br/>";
		}
		else
		{
			?>
			<ul>
				
				<li> <a href=<?php $archivo ?> > <?php $archivo ?> </a> </li> <?php;?>
			</ul>
		<?php
		}
	}
?>
</body>
</html>

