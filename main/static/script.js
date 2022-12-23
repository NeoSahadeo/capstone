function saveTask(element){
    date = `${$( "#datepicker" ).datepicker( "getDate" ).getFullYear()} ${$( "#datepicker" ).datepicker( "getDate" ).getMonth()+1} ${$( "#datepicker" ).datepicker( "getDate" ).getDate()}`
    $("#id_date").val($( "#datepicker" ).datepicker( "getDate" ))
    time = ` ${$('#id_time').val().replace(':',' ')}`
    date_time = date.concat(time)
    form = Object.fromEntries(new FormData(element).entries())
    console.log(date_time)
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
function initializePlugins(){
    $('#datepicker').datepicker()
    $('#id_time').clockTimePicker()
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