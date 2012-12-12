(function () {
    var handle_button = function (opts) {
        $.getJSON(opts.url, function (data) {
            $('#stats-pane').empty()
                            .append(Mustache.render(_tmpl.stats, data));
            $('#all-stats').html(opts.label);
            $('#chosen-categories').html(opts.chosen);
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
})();
