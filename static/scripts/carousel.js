// calculate the screen width and apply to carousel
$(window).load(function(){
    var view_width = $(window).width() - 20;

    $('#carousel').css('width', view_width);

    $('#carousel ul li:first-child').addClass('active');

    var img_width = $('#carousel ul li.active').width();

    var left = (view_width - img_width) / 2;

    // move ul to the intial position
    $('#carousel ul').attr('style', '-webkit-transform: translate3d('+left+'px, 0px, 0px);');

    // attach event to the carousel
    $('#carousel .next').click(function() {
        var img_width = $('#carousel ul li.active').next().width();
        var left = ((view_width - img_width) / 2) - $('#carousel ul li.active').width();

        $('#carousel ul').addClass('animate');
        var new_position = "translate3d(" + left + "px, 0px, 0px)";
        $('#carousel ul').css('-webkit-transform', new_position);
        $('#carousel ul li.active').removeClass('active').next().addClass('active');
    });
});