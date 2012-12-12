(function () {
    $.getJSON('/featured_stats', function (data) {
        $('#stats-pane').append(Mustache.render(_tmpl.stats, data));
    });

    $('#all-stats').click(function () {
        $.getJSON('/all_stats', function (data) {
            $('#stats-pane').empty().append(Mustache.render(_tmpl.stats, data));
        });
    });
})();
