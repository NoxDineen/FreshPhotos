$(function(){
	var view_width = $(window).width()-20;
	$('#carousel').css('width', 'view_width');
	$('carousel ul').attr('style', '-webkit-transform: translate3d(1000px|0px|0px)');
	$('#carousel .next').click(function(){
		alert('Hey');
	})
});