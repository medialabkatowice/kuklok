(function () {
    var handle_button = function (opts) {
        $.getJSON(opts.url, function (data) {
            $('#stats-pane').empty()
                            .append(Mustache.render(_tmpl.stats, data));
            $('#all-stats').html(opts.label);
            $('#chosen-categories').html(opts.chosen);
            arm_details();
            $('#show-more-categories').html('WYBIERZ TEMATY');
            $('#categories').slideUp();
        });
    };

    var defaults = {
        url   : '/featured_stats',
        label : 'Pokaż wszystkie',
        chosen: 'Najciekawsze tematy'
    }
    handle_button(defaults);

    $('#all-stats').click(function () {
        if($(this).html() === 'Pokaż wszystkie') {
            handle_button({
                url   : '/all_stats',
                label : 'Pokaż najciekawsze',
                chosen: 'Wszystkie tematy'
            });
        }
        else {
            handle_button(defaults);
        }
    });

    function arm_details() {
        $('.details').click(function () {
            console.log('Hmm..');
            console.log($(this).attr('id'));
        });
    }

    $('#categories').hide();

    $('#show-more-categories').click(function () {
        if($('#categories').is(':visible')) {
            $(this).html('WYBIERZ TEMATY');
            $('#categories').slideUp();
        }
        else {
            $(this).html('SCHOWAJ PANEL');
            $('#categories').find('input')
                            .attr('checked', false)
                            .end().slideDown();
        }
    });

    $('#filter-categories').click(function () {
        var categories = $('input:checked').map(function () { 
                                                    return $(this).attr('name') 
                                                }).toArray()
        $.getJSON('/selected_stats', {categories: categories.join(',')}, function (data) {
            $('#stats-pane').empty()
                            .append(Mustache.render(_tmpl.stats, data));
            $('#all-stats').html('Pokaż wszystkie');
            $('#chosen-categories').html(categories.join(', '));
            arm_details();
            $('#show-more-categories').html('Wybierz tematy');
            $('#categories').slideUp();

        });
    });
})();
