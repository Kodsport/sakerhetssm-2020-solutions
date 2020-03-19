<?php
$db = new SQLite3('/tmp/db.sqlite');
$db->query("CREATE TABLE IF NOT EXISTS tickets (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, ticket TEXT);");
$db->query("CREATE TABLE IF NOT EXISTS flag (id INTEGER PRIMARY KEY AUTOINCREMENT, flag TEXT);");

// Seed data
@$db->query("INSERT INTO tickets VALUES (8316017200881170786, 'ZetaTwo', 'calle.svensson@zeta-two.com', 'The AI is a lie');");
@$db->query("INSERT INTO tickets VALUES (5039345887675068379, 'ZetaTwo', 'calle.svensson@zeta-two.com', 'The blockchain is fake');");
@$db->query("INSERT INTO flag VALUES (1337, 'SSM{mayb3_n0t_dat_perfect0_4fter_ALL}');");
