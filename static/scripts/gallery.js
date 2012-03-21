// $.post(url, data, function/success(), data-type)
$(function(){
	var form = $('#comment-form');

	form.submit(
		function(e) {
			$.post(
				'/photo/1/',
				form.serializeArray(),
				function(data) {
					console.log(data);
				},
				'json'
			);
		e.preventDefault();
	}
	);
});