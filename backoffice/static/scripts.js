
$(document).ready(function(){

  var frm = $('form');

  $('#form-submit').click(function(){
    frm.submit();
  });

  $('#delete').click(function(e){
    e.preventDefault();
    if (confirm("Do you want to delete this animal?")){
        window.location.href = $(this).attr('href');
    }
  });

  // emulate floating label effect on species text
  var species_text = $("#species");
  $('.species.mdl-menu__item').click(function() {
    var item = $(this);
    $('input[name=species]').val(item.attr('data-val'));

    species_text.closest('.getmdl-select').addClass('is-focused');
    species_text.val(item.text());
  })

  // image input
  function readURL(input) {

    if (input.files && input.files[0]) {
      var reader = new FileReader();

      var animal_pic = $('#animal-pic');
      reader.onload = function(e) {
        animal_pic.attr('src', e.target.result);
        animal_pic.removeClass('hidden');
      }

      reader.readAsDataURL(input.files[0]);
    }
  }

  var file_input = $("input[name=file]");
  var file_text = $(".file_text");

  file_input.change(function(){
    var filename = $(this).val().split('fakepath\\')[1];
    file_text.text(filename);
    readURL(this);
  });


  //asign semi-random color to a card
  var colors = ['teal', 'pink', 'purple', 'deep-purple', 'indigo', 'blue', 'light-blue',
                'cyan', 'red', 'green', 'light-green', 'lime', 'yellow',
                'amber', 'orange', 'deep-orange', 'brown', 'grey', 'blue-grey'];

  var card = $(".demo-updates").find('.mdl-card__title');
  card.each(function(){
    var pic = $(this).find('input[name=animal-pic]');
    if (pic.val()){
      $(this).css('min-height', '200px');
      $(this).css('background-image', 'url('+pic.val()+')');
    }
    var name = $(this).find('.mdl-card__title-text').text();
    $(this).addClass('mdl-color--' + colors[name.length % colors.length] + '-300');
  });

});
