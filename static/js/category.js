(function () {

    var category = window.location.pathname.split('/').pop();
    var opts = opts || {
        url   : '/timeline/' + category,
        chosen: category,
        data  : {}
    }

    $.getJSON(opts.url, opts.data, function (data) {
        $('#stats-pane').empty()
                        .append(Mustache.render(_tmpl.timeline, data));
        $('#chosen-categories').html(opts.chosen);

        $('.week').click(function () {
            var el = $(this);

            $('#details-pane').slideUp(function () {
                $(this).remove();
                details(el);
            });
        });

        setTimeout(function () {
            var el = $('.week').first();
            details(el);
        }, 500);

    });

    function details(el) {
        var inx = $('.week').index($(this));
        var url = '/details/'+ category +'/'+ inx;

        $.getJSON(url, function (data) {
            el.append(Mustache.render(_tmpl.details));
            $('#details-pane').hide().slideDown();

            console.log(data);
        });
    }
})();
