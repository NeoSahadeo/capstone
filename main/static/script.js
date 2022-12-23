function saveTask(element){
    date = `${$( "#datepicker" ).datepicker( "getDate" ).getFullYear()} ${$( "#datepicker" ).datepicker( "getDate" ).getMonth()+1} ${$( "#datepicker" ).datepicker( "getDate" ).getDate()}`
    $("#id_date").val($( "#datepicker" ).datepicker( "getDate" ))
    time = ` ${$('#id_time').val().replace(':',' ')}`
    date_time = date.concat(time)
    form = Object.fromEntries(new FormData(element).entries())
    
    // $.ajax({
    //     url: 'createtask',
    //     type: 'POST',
    //     data: {
    //         csrfmiddlewaretoken: form.csrfmiddlewaretoken,
    //         body: {
    //             'taskname': form.taskname,
    //             'date_time': date_time,
    //             'color': form.color 
    //         }
    //     },
    //     success: ()=>{
    //         console.log('saved')
    //     }
    // })
}
$('.time').clockTimePicker({
    modeSwitchSpeed: 10,
    i18n: {
		cancelButton: 'Cancel'
	}
});
function showDatePicker(){
    $( "#datepicker" ).datepicker()
}
// const findOverflows = () => {
//     const documentWidth = document.documentElement.offsetWidth;

//     document.querySelectorAll('*').forEach(element => {
//         const box = element.getBoundingClientRect();

//         if (box.left < 0 || box.right > documentWidth) {
//             console.log(element);
//             element.style.border = '1px solid red';
//         }
//     });
// };

// // Execute findOverflows to find overflows on the page.
// findOverflows();