<?php
$picture=$_GET['p'];
header("Content-Type: image/png");
require_once($picture);
