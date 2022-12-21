function saveTask(element){
    form = Object.fromEntries(new FormData(element).entries())
    $.ajax({
        url: 'createtask',
        type: 'POST',
        data: {
            csrfmiddlewaretoken: form.csrfmiddlewaretoken,
            body: {
                'taskname': form.taskname,
                'date_time': form.date_time,
                'color': form.color 
            }
        }
    },
    function(data,status){
    }
    )
}