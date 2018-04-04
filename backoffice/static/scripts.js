
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

  var species_text = $("#species");
  $('.species.mdl-menu__item').click(function() {
    var item = $(this);
    $('input[name=species]').val(item.attr('data-val'));

    species_text.closest('.getmdl-select').addClass('is-focused');
    species_text.val(item.text());
  })
});
