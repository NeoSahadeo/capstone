$('#displayContentSliderWeekMode').on('input',function(e){
    currentDateTime = new Date($.now())
    $.ajax({
        type: 'GET',
        url: 'selectcontentweek',
        data: { 
            val: $(this).val(),
        }
    })
})
// $('#displayContentSliderMonthMode').on('input',function(e){