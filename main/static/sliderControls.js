$('#displayContentSliderWeekMode').on('input',function(e){
    currentDateTime = new Date($.now())
    $.ajax({
        type: 'GET',
        url: 'selectcontentweek',
        data: { 
            val: $(this).val(),
        },
        success: (data)=>{
            // Update 'Header' details
            $('#currentContentHeader')[0].innerHTML = data['current']
            // Update 'todo' list
            $('#currentContentHeader + ul')[0].innerHTML = ''
            data['daytasks'].forEach(element => {
                $('#currentContentHeader + ul')[0].innerHTML += element['taskname']
            });
        }
    })
})
// $('#displayContentSliderMonthMode').on('input',function(e){