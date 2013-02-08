$(document).ready(function() {
    $('#scheduled_date').datepicker({
        numberOfMonths: 1,
        minDate: 0,
        maxDate: 30
    });
    $('#scheduled_time').timepicker({
        //hourMin: 0,
        //hourMax: 23
        }
    );
    $('#environment').val('production');
    $("#environment").change(function() {
        if ($(this).val() === 'sandbox_test') {
            $('#sandbox_tokens').show('slow')
        } else if ($(this).val() === 'production_test') {
            $('#sandbox_tokens').show('slow')
        } else {
            $('#sandbox_tokens').hide('slow')
        }
    });

    $('#schedule_input').live('change', function(){
        checkScheduleBox();
    });

    $('#schedule_for_timezone').live('change', function(){
        checkTimezoneBox()
    });

    checkScheduleBox();
    checkTimezoneBox()

    $("#notification_form").validate({
        rules : {
            alert_message : {
                required : true,
                maxlength: 100,
                minlength: 3
            },
            url : {
                required : false,
                maxlength: 35,
                minlength: 12
            }
        }
    });

});

function checkScheduleBox(){
    if($('#schedule_input').is(':checked')){
        $('#schedule_me').show('slow');
    } else{
        $('#schedule_me').hide('slow');
    }
}

function checkTimezoneBox(){
    if($('#schedule_for_timezone').is(':checked')){
        $('#schedule_for_timezone_select').show('slow');
    } else{
        $('#schedule_for_timezone_select').hide('slow');
    }
}