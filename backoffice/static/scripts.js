
function wipe_form(form){
    form.trigger('reset');
    $('form input:radio').each(function(){
        $(this).closest('label').removeClass('is-checked');
    });
    
    $('form input:checkbox').each(function(){
        $(this).closest('label').removeClass('is-checked');
    });
}

$(document).ready(function(){
    
    var frm = $('form');
    frm.submit(function(e){
        e.preventDefault();
        $.ajax({
            type: frm.attr('method'),
            data: frm.serialize(),
            dataType: 'json',
            success: function (data) {
                wipe_form(frm);
                alert(data['message']);
            },
            error: function(data) {
                alert(data['responseJSON']['message']);
            }
        });
    });
    
})
