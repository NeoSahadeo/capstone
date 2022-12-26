function saveTask(element){
    date = `${$( "#datepicker" ).datepicker( "getDate" ).getFullYear()} ${$( "#datepicker" ).datepicker( "getDate" ).getMonth()+1} ${$( "#datepicker" ).datepicker( "getDate" ).getDate()}`
    $("#id_date").val($( "#datepicker" ).datepicker( "getDate" ))
    time = ` ${$('#id_time').val().replace(':',' ')}`
    date_time = date.concat(time)
    color = $('#color_storage')[0].value
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
            try{
                fetchDay(parseInt($('#icurrentDay').val()))
            }catch{}
        }
    })
}
function initializePlugins(mode){
    colorpicker()
    $('#id_time').clockTimePicker()
    $('#datepicker').datepicker()
    if (mode == 'Month Mode'){  
        year = new Date().getFullYear()
        month = parseInt($('#month_id').val())
        day = parseInt($('#icurrentDay').val())
        $('#datepicker').datepicker('setDate', new Date(year,month,day))
    }
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
function colorpicker(){
    if ($('#id_color')[0].style.backgroundColor == ''){
        color = `#${Math.floor(Math.random()*16777215).toString(16)}`
        $('#id_color')[0].style.backgroundColor = color
        $('#color_storage')[0].value = color
    }
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