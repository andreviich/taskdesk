console.log('thats works')

$('.main-section-right-form').submit((e)=>{
    e.preventDefault()
    url = $('.main-section-right-form').attr('action')
    subject = $('.main-section-right-form').find('select[name="subject"]').val()
    text = $('.main-section-right-form').find('input[name="text"]').val()
    date =  $('.main-section-right-form').find('input[name="expire"]').val()
    console.log(subject, text, date)
     $.ajax({
      type: "POST",
      url: url,
      data: {
        'subject': subject,
          'text'  : text,
          'date' : date
      },
      success: function (response) {
          console.log(response)
          $.notify('Новое домашнее задание добавлено!', 'success')
          $('.main-section-right-form').trigger('reset');
      }
    });
})