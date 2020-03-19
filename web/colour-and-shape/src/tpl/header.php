<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>The Colours and the Shapes<?php echo isset($title)?" - $title":""; ?></title>
    <style>
      html { 
          height: 100%;
          padding: 0;
          margin: 0;
      }
      body {
          background-color: #fff8f8;
          height: 100%;
          padding: 0;
          margin: 0;
      }
      #wrapper {
          width: 600px;
          margin: 0 auto;
          padding-top: 20px;
      }
      #footer {
          position: fixed;
          bottom: 0px;
      }
      #menu ul {
          list-style-type: none;
      }
      #menu ul li {
          display: inline-block;
          height: 20px;
          border: 1px solid #000000;
          margin: 0;
          padding: 10px;
      }
    </style>
  </head>
  <body>
    <div id="wrapper">
    <div id="menu">
     <ul>
      <li><a href="/" title="Index">Index</a></li>
      <li><a href="/colours.php" title="The Colours">The Colours</a></li>
      <li><a href="/shapes.php" title="The Shapes">The Shapes</a></li>
     </ul>
    </div>
