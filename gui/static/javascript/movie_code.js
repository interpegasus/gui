$(document).ready(function() {
	$("#movie_code_form").validate({
		rules : {
			code : {
				required : true
			},
		}
	});
});
