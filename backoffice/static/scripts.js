
$(document).ready(function(){

  var frm = $('form');

  $('#form-clear').click(function(){
    frm.trigger('reset');
    $('form input:radio').each(function(){
      $(this).closest('label').removeClass('is-checked');
    });

    $('form input:checkbox').each(function(){
      $(this).closest('label').removeClass('is-checked');
    });
  });

  $('#form-submit').click(function(){
    frm.submit();
  });

});
