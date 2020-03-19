<?php
require_once('db.php');
require_once('tpl/header.php');
?>
<h1>Submit Ticket</h1>
<p>
Here you can submit a ticket if you need help.
We solve our tickets within 0.5 seconds thanks to our AI and blockchain powered support system so expect your ticket to be solved really quickly.
</p>
<?php
if(isset($_POST['ticket_name'])) {
    $ticket_id = rand ( 100000 , 999999 );
    ?>
    Your ticket has been submitted. Your ticket ID is <?php echo $ticket_id; ?>.
    <?php
} else {
    ?>
<form action="" method="post">
Name: <input type="text" name="ticket_name"><br>
Email: <input type="email" name="ticket_email"><br>
How can we help you?<br><textarea name="ticket_text" rows="10", cols="40"></textarea><br>
<input type="submit" value="Submit ticket"><br>
</form>
<?php
}
?>
<?php
require_once('tpl/footer.php');
?>
