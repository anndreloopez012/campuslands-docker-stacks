<?php
header('Content-Type: application/json');
echo json_encode(["stack" => "Laravel + MySQL", "nota" => "Si no existe artisan, el contenedor crea un proyecto Laravel real al iniciar."]);
