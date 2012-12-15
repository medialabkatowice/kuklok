var _tmpl = (function () {
    var self = {};

    self.stats = 
        '<ul id="stats">' + 
          '{{#data}}' + 
            '<li class="chart half left">' + 
              '<h2>{{category}}</h2>' + 
              '<ul>' + 
                '{{#weeks}}' +
                '<li class="clear">' + 
                  '<div class="left half">' + 
                    '<p class="left tags-l">&nbsp;</p>' + 
                    '<p class="bar right" style="width: {{media}}px">&nbsp;</p>' + 
                  '</div>' + 
                  '<div class="right half">' + 
                    '<p class="right tags-r">&nbsp;</p>' + 
                    '<p class="bar left" style="width: {{city}}px">&nbsp;</p>' + 
                  '</div>' + 
                '</li>' + 
                '{{/weeks}}' + 
              '</ul>' + 
              '<br />' + 
              '<a class="details button right" href="/{{category}}" id="{{category}}">Szczegóły</a>' +
            '</li>' + 
          '{{/data}}' + 
        '</ul>';

    self.timeline = 
        '<ul id="timeline">' + 
          '{{#data}}' + 
            '<li class="chart">' + 
              '<h2>{{category}}</h2>' + 
              '<ul>' + 
                '{{#weeks}}' +
                '<li class="clear">' + 
                  '<div class="left half">' + 
                    '<p class="left tags-l">&nbsp;</p>' + 
                    '<p class="bar right" style="width: {{media}}px">&nbsp;</p>' + 
                  '</div>' + 
                  '<div class="right half">' + 
                    '<p class="right tags-r">&nbsp;</p>' + 
                    '<p class="bar left" style="width: {{city}}px">&nbsp;</p>' + 
                  '</div>' + 
                '</li>' + 
                '{{/weeks}}' + 
              '</ul>' + 
              '<br />' + 
            '</li>' + 
          '{{/data}}' + 
        '</ul>';

    return self;
})();
