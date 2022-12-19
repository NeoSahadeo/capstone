// $('#displayContentSliderWeekMode').on('input',function(e){
//     currentDateTime = new Date($.now())
//     $.ajax({
//         type: 'GET',
//         url: 'selectcontentweek',
//         data: { 
//             val: $(this).val(),
//         },
//         success: (data)=>{
//             // Update 'Header' details
//             $('#currentContentHeader')[0].innerHTML = data['current']
//             // Update 'todo' list
//             $('#currentContentHeader + ul')[0].innerHTML = ''
//             data['daytasks'].forEach(element => {
//                 $('#currentContentHeader + ul')[0].innerHTML += element['taskname']
//             });
//         }
//     })
// })
// $('#displayContentSliderMonthMode').on('input',function(e){

odaylookup = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday',
}
const dayupdate = (element) => {
    $('#currentContentHeader')[0].innerHTML = odaylookup[element.value]
}