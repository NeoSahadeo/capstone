function saveTask(element){
    date = `${$( "#datepicker" ).datepicker( "getDate" ).getFullYear()} ${$( "#datepicker" ).datepicker( "getDate" ).getMonth()+1} ${$( "#datepicker" ).datepicker( "getDate" ).getDate()}`
    $("#id_date").val($( "#datepicker" ).datepicker( "getDate" ))
    time = ` ${$('#id_time').val().replace(':',' ')}`
    date_time = date.concat(time)
    color = $('#id_color').val()
    taskname = $('#id_taskname').val()
    form = Object.fromEntries(new FormData(element).entries())
    $.ajax({
        url: 'createtask',
        type: 'POST',
        data: {
            csrfmiddlewaretoken: form.csrfmiddlewaretoken,
            body: {
                'taskname': taskname,
                'date_time': date_time,
                'color': color 
            }
        },
        success: ()=>{
            console.log('saved')
        }
    })
}
function initializePlugins(){
    $('#datepicker').datepicker()
    $('#id_time').clockTimePicker()
}
function switchMode(mode){
    if (mode == 'Month Mode'){
        $.ajax({
            url: 'switchmode',
            type: 'GET',
            data: {
                body: {
                    'mode': 'Week Mode'
                }
            },
            success: ()=>{
                $(location).attr('href','/')
            }
        })
    }
    if (mode == 'Week Mode'){
        $.ajax({
            url: 'switchmode',
            type: 'GET',
            data: {
                body: {
                    'mode': 'Month Mode'
                }
            },
            success: ()=>{
                $(location).attr('href','/')
            }
        })
    }
}
function setCurrentDay(day_id){
    // console.log($(`#day_${day_id}`)[0].styles.backgroundColor)
    document.querySelector(`#day_${day_id}`).classList.add('selected')
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