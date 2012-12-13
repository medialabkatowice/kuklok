(function () {

    handle_button();
    $('#categories').hide();

    $('#all-stats').click(function () {
        if($(this).html() === 'Pokaż wszystkie') {
            handle_button({
                url   : '/all_stats',
                label : 'Pokaż najciekawsze',
                chosen: 'Wszystkie tematy'
            });
        }
        else {
            handle_button();
        }
    });


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
            chosen: categories,
            data  : {categories: categories}
        }
        handle_button(opts);
    });


    function open_categories_panel() {
        $('#categories').find('input')
                        .attr('checked', false)
                        .end()
                        .slideDown(function () {
                            $('#show-more-categories').html('SCHOWAJ PANEL');
                        });
    }

    function close_categories_panel() {
        $('#categories').slideUp(function () {
                            $('#show-more-categories').html('WYBIERZ TEMATY');
                        });
    }

    function handle_button(opts) {
        var opts = opts || {
            url   : '/featured_stats',
            label : 'Pokaż wszystkie',
            chosen: 'Najciekawsze tematy',
            data  : {}
        }

        $.getJSON(opts.url, opts.data, function (data) {
            $('#stats-pane').empty()
                            .append(Mustache.render(_tmpl.stats, data));
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
})();
