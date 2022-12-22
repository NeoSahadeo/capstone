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
        },
        success: ()=>{
            console.log('saved')
        }
    })
}
$('.time').clockTimePicker({
    modeSwitchSpeed: 10000,
    i18n: {
		cancelButton: 'Cancel'
	}
});
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