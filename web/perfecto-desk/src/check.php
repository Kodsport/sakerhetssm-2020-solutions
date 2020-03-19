<?php
require_once('db.php');
require_once('tpl/header.php');
?>
<h1>Check Ticket Status</h1>
<p>
Here you can check the status of your ticket. We solve our tickets within 0.5 seconds thanks to our AI and blockchain powered support system so expect your ticket to already be resolved.
</p>
<?php
if(isset($_POST['ticket_id'])) {
    $ticket_id = $_POST['ticket_id'];
    $query = "SELECT * FROM tickets WHERE id = '$ticket_id';";
    $result = @$db->query($query);
    if($result) {
        $row = $result->fetchArray();
    } else {
        $row = false;
    }
    
    if($row) {
        ?>
        <p>Name: <?php echo $row['name'];?><br>Email: <?php echo $row['email'];?><br>Ticket: <?php echo $row['ticket'];?></p>
        <?php
    } else {
        ?>
        <p>We could not find that ticket. The issue must already have been resolved, which is expected of our excellent system of course. Not that we think you do, but if you need further assistance, please submit a new ticket.</p>
        <?php
    }
} else {
    ?>
<form action="" method="post">
Ticket ID: <input type="text" name="ticket_id"> <input type="submit" value="Check ticket"><br>
</form>
<?php
}
?>
<?php
require_once('tpl/footer.php');
?>
