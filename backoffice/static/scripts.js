
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


  //asign semi-random color to a card
  var colors = ['teal', 'pink', 'purple', 'deep-purpe', 'indigo', 'blue', 'light-blue',
                'cyan', 'red', 'green', 'light-green', 'lime', 'yellow',
                'amber', 'orange', 'deep-orange', 'brown', 'grey', 'blue-grey'];

  var card = $(".demo-updates").find('.mdl-card__title');
  card.each(function(){
    var name = $(this).find('.mdl-card__title-text').text();
    $(this).addClass('mdl-color--' + colors[name.length % colors.length] + '-300');
  });
});
