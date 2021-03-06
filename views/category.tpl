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
    <header>
      <div id="top-block">
          <p class="left">Strona główna</p>
          <p class="right">Szukaj</p>
      </div>

      <br class="clear" />

      <img alt="Logo Miejskiego Kukloka" title="Logo Miejskiego Kukloka" src="/static/img/logo.png" class="center" />
    </header>

    <section>
      <h2>
        AKTYWNOŚĆ MEDIÓW I MIASTA W TEMACIE: <span id="chosen-categories"></span>
      </h2>

    </section>

    <section id="stats-pane">
    </section>

    <br class="clear" />
    <p>&nbsp;</p>

    <!-- JavaScript includes --> 
    <script src="/static/js/lib/jquery.js"></script>
    <script src="/static/js/lib/underscore.js"></script>
    <script src="/static/js/lib/mustache.js"></script>

    <script src="/static/js/tmpl.js"></script>
    <script src="/static/js/category.js"></script>
  </body>
</html
