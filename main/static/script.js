function saveTask(element){
    date = `${$( "#datepicker" ).datepicker( "getDate" ).getFullYear()} ${$( "#datepicker" ).datepicker( "getDate" ).getMonth()+1} ${$( "#datepicker" ).datepicker( "getDate" ).getDate()}`
    $("#id_date").val($( "#datepicker" ).datepicker( "getDate" ))
    time = ` ${$('#id_time').val().replace(':',' ')}`
    date_time = date.concat(time)
    color = $('#color_storage')[0].value
    taskname = $('#id_taskname').val()
    task_id_number = -1
    allow_delete = false
    if ($('#task_id_number').length > 0){
        task_id_number = $('#task_id_number')[0].value
        allow_delete = $('#allow_delete')[0].value
    }
    form = Object.fromEntries(new FormData(element).entries())
    $.ajax({
        url: 'createtask',
        type: 'POST',
        data: {
            csrfmiddlewaretoken: form.csrfmiddlewaretoken,
            body: {
                'taskname': taskname,
                'date_time': date_time,
                'color': color,
                'task_id_number': task_id_number,
                'allow_delete': allow_delete
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
    year = new Date().getFullYear()
    if (mode == 'Month Mode'){
        let month = parseInt($('#month_id').val())
        let day = parseInt($('#icurrentDay').val())
        $('#icurrentDay_storage').val(day)
        $('#datepicker').datepicker('setDate', new Date(year,month,day))
    }
    if (mode == 'Week Mode'){
        $('#datepicker').datepicker('setDate', new Date($('#weight').val()))
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
    color = `#${Math.floor(Math.random()*16777215).toString(16)}`
    if ($('#id_color')[0].style.backgroundColor == ''){
        $('#id_color')[0].style.backgroundColor = color
        $('#color_storage')[0].value = color.slice(1,)
    }
    return color
}
function colorpickertool(){
    window.scrollTo(0,0)
    if ($('#color_container')[0].classList.contains('hidden')){
        $('html').css('overflow','clip')
        color = $('#color_storage')[0].value
        $('#color_display')[0].style.backgroundColor = color
        $('#color_container')[0].classList.remove('hidden')
        color = $('#color_display')[0].style.backgroundColor
        colorRGB = color.slice(color.indexOf('(')+1,color.indexOf(')')).split(', ')
        $('.slider')[0].value = parseInt(colorRGB[0])
        $('.slider')[1].value = parseInt(colorRGB[1])
        $('.slider')[2].value = parseInt(colorRGB[2])
    }else{
        $('html').css('overflow-y','scroll')
        $('#color_container')[0].classList.add('hidden')
    }
}
function updatecolorpicker(){
    red = parseInt($('.slider')[0].value)
    green = parseInt($('.slider')[1].value)
    blue = parseInt($('.slider')[2].value)
    $('#color_display')[0].style.backgroundColor = `rgb(${red}, ${green} ,${blue})`
    $('#id_color')[0].style.backgroundColor = `rgb(${red}, ${green} ,${blue})`
    $('#color_storage')[0].value = `${red.toString(16).padStart(2, '0')}${green.toString(16).padStart(2, '0')}${blue.toString(16).padStart(2, '0')}`
}
function formatdate_time(date_time){
    $("#id_time")[0].value = date_time.split(' ')[1]
}
function askPermission() {
    return new Promise(function (resolve, reject) {
      const permissionResult = Notification.requestPermission(function (result) {
        resolve(result);
      });  
      if (permissionResult) {
        permissionResult.then(resolve, reject);
      }
    }).then(function (permissionResult) {
      if (permissionResult !== 'granted') {
      }
    });
}