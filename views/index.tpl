<!DOCTYPE HTML>
<html lang="pl">
  <head>
    <meta charset="UTF-8">
    <title>{{title}}</title>

    <!-- fonts and styles --> 
    <link rel="stylesheet" type="text/css" href="/static/css/style.css"/>

    <!-- don't forget the analytics code --> 
  </head>
  <body>
    <!-- content goes here --> 
    <ul>
      %for d in data:
      <li>{{', '.join(sorted(d['districts']))}}</li>
      %end
    </ul>

    <!-- JavaScript includes --> 
    <script src="/static/js/lib/jquery-1.7.2.js"></script>
    <script src="/static/js/lib/underscore.js"></script>

    <script src="/static/js/script.js"></script>
  </body>
</html