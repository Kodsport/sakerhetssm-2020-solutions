<?php
$title = 'The Shapes';
require_once('tpl/header.php');
?>
<h1>The Shapes</h1>
<table>
  <tbody>
    <tr>
      <td><img src="/img/gallery/view.php?p=triangle.png" src="Triangle"></td>
      <td><img src="/img/gallery/view.php?p=square.png" src="Square"></td>
    </tr>
    <tr>
      <td><img src="/img/gallery/view.php?p=pentagon.png" src="Pentagon"></td>
      <td><img src="/img/gallery/view.php?p=hexagon.png" src="Hexagon"></td>
    </tr>
    <tr>
      <td><img src="/img/gallery/view.php?p=octagon.png" src="Octagon"></td>
      <td><img src="/img/gallery/view.php?p=circle.png" src="Circle"></td>
    </tr>
  </tbody>
</table>
<?php
require_once('tpl/footer.php');
?>