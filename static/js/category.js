(function () {

    var category = window.location.pathname.split('/').pop();

    handle_button();
    $('#categories').hide();


    $('#show-more-categories').click(function () {
        if($('#categories').is(':visible')) {
            close_categories_panel();
        }
        else {
            open_categories_panel();
        }
    });


    $('#filter-categories').click(function () {
        var cats = $('input:checked').map(function () { 
                                          return $(this).attr('name') 
                                      }).toArray()
        var categories = cats.join(',');
        var opts = {
            url   : '/selected_stats',
            label : 'Pokaż wszystkie',
            chosen: $(':checkbox').length === cats.length ? 
                    'Wszystkie tematy' : categories,
            data  : {categories: categories}
        }
        handle_button(opts);
    });


    function open_categories_panel() {
        select_checkboxes();

        $('#categories').slideDown(function () {
                            $('#show-more-categories').html('SCHOWAJ PANEL');
                        });
    }

    function close_categories_panel() {
        $('#categories').slideUp(function () {
                            $('#show-more-categories').html('WYBIERZ TEMATY');
                        });
    }

    function handle_button(opts) {
        var category = window.location.pathname.split('/').pop();
        var opts = opts || {
            url   : '/timeline/' + category,
            label : 'Pokaż wszystkie',
            chosen: category,
            data  : {}
        }

        $.getJSON(opts.url, opts.data, function (data) {
            $('#stats-pane').empty()
                            .append(Mustache.render(_tmpl.timeline, data));
            $('#all-stats').html(opts.label);
            $('#chosen-categories').html(opts.chosen);
            arm_details();
            close_categories_panel();
        });
    };


    function arm_details() {
        $('.details').click(function () {
            // TODO code here
            console.log($(this).attr('id'));
        });
    }

    function select_checkboxes() {
       var categories = $('.details').map(function () { 
                                return $(this).attr('id'); 
                         }).toArray();

       $(':checkbox').each(function () {
           var name    = $(this).attr('name');
           var present = _.contains(categories, name);

           $(this).attr('checked', present);
       });
    }

})();
