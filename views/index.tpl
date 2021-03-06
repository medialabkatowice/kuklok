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
        AKTYWNOŚĆ MEDIÓW I MIASTA W TEMATACH: <span id="chosen-categories">Wszystkie tematy</span>
      </h2>

      <div id="open-close-bar">
        <div id="show-more-categories" class="button">WYBIERZ TEMATY</div>
      </div>

      <section id="categories">
        <ul class="half left">
          <li>
            <input class="left" type="checkbox" name="Edukacja" />
            <span class="left">Edukacja</span>
          </li>
          <li>
            <input class="left" type="checkbox" name="Ekonomia" />
            <span class="left">Ekonomia</span>
          </li>
          <li>
            <input class="left" type="checkbox" name="Infrastruktura" />
            <span class="left">Infrastruktura</span>
          </li>
        </ul>        
        <ul class="half right">
          <li>
            <input class="left" type="checkbox" name="Kultura" />
            <span class="left">Kultura</span>
          </li>
          <li>
            <input class="left" type="checkbox" name="Transport" />
            <span class="left">Transport</span>
          </li>
          <li>
            <input class="left" type="checkbox" name="Zdrowie" />
            <span class="left">Zdrowie</span>
          </li>
        </ul>        
        <div id="filter-categories" class="right button">Wybierz</div>
      </section>

    </section>

    <section id="stats-pane">
    </section>

    <div id="all-stats" class="button left">Pokaż wszystkie</div>
    <br class="clear" />
    <p>&nbsp;</p>

    <!-- JavaScript includes --> 
    <script src="/static/js/lib/jquery.js"></script>
    <script src="/static/js/lib/underscore.js"></script>
    <script src="/static/js/lib/mustache.js"></script>

    <script src="/static/js/tmpl.js"></script>
    <script src="/static/js/script.js"></script>
  </body>
</html
