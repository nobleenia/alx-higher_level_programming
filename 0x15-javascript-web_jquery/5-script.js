$('DIV#add_item').click(() => {
  $('UL.my_list').append($('<li></li>').text('Item'));
});
