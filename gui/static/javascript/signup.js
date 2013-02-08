$(document).ready(function() {
	$("#create_user_form").validate({
		rules : {
			email : {
				email : true,
				required : true
			},
			confirm_email : {
				email : true,
				required : true,
				equalTo : "#email"
			},
			password : {
				required : true,
				minlength : 7
			},
			confirm_password : {
				required : true,
				minlength : 7,
				equalTo : "#password"
			},
			terms: "required"
		}
	});

	$("#login_user_form").validate({
		rules : {
			email_2 : {
				email : true,
				required : true
			},
			password_2 : {
				required : true,
				minlength : 7
			}
		}
	});
	$('#code').change(function() {
		$('#code_1').val($('#code').val());
		$('#code_2').val($('#code').val());
	});
});
