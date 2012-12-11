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
      <h2 id="chosen-categories">
        AKTYWNOŚĆ MEDIÓW I MIASTA W TEMATACH: Wszystkie tematy
      </h2>
      <div id="open-close-bar" class="button">
        <p>wybierz temat v</p>
      </div>
    </section>

    <div class="chart half left">
      <h2>{{ active['category'] }}</h2>
      <ul>
        % for w in active['weeks']:
        <li class="clear">
          <div class="left half">
            <p class="left tags-l" style="">&nbsp;</p>
            <p class="bar right" style="width: {{ w[0]/2 }}px">&nbsp;</p>
          </div>
          <div class="right half">
            <p class="right tags-r">&nbsp;</p>
            <p class="bar left" style="width: {{ w[1]/2 }}px">&nbsp;</p>
          </div>
        </li>
        % end
      </ul>
    </div>

    <div class="chart half right">
      <h2>{{ differ['category'] }}</h2>
      <ul>
        % for w in differ['weeks']:
        <li class="clear">
          <div class="left half">
            <p class="left tags-l" style="">&nbsp;</p>
            <p class="bar right" style="width: {{ w[0]/2 }}px">&nbsp;</p>
          </div>
          <div class="right half">
            <p class="right tags-r" style="">&nbsp;</p>
            <p class="bar left" style="width: {{ w[1]/2 }}px">&nbsp;</p>
          </div>
        </li>
        % end
      </ul>
    </div>
    <br />
    <!-- JavaScript includes --> 
    <script src="/static/js/lib/jquery-1.7.2.js"></script>
    <script src="/static/js/lib/underscore.js"></script>

    <script src="/static/js/script.js"></script>
  </body>
</html
