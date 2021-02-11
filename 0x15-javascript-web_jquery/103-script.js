//  fetches and prints how to say “Hello” depending on the language
// You should use this API service: https://www.fourtonfish.com/hellosalut/hello/
// The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.)
// The translation must be fetched when the user clicks on INPUT#btn_translate
//     OR presses ENTER when the focus is on INPUT#language_code
// The translation of “Hello” must be displayed in the HTML tag DIV#hello
// You can’t use document.querySelector to select the HTML tag
// You must use the jQuery API
// You script must work when imported from the HEAD tag
document.addEventListener('DOMContentLoaded', function () {
  $('INPUT#btn_translate').click(() => {
    const language = $('INPUT#language_code').val();
    const url = 'https://fourtonfish.com/hellosalut/?lang=' + language;
    $.get(url, function( data ) {
      $('DIV#hello').text(data.hello);
    });
  });
  $('INPUT#language_code').keydown((e) => {
    const language = $('INPUT#language_code').val();
    const url = 'https://fourtonfish.com/hellosalut/?lang=' + language;
    if (e.which === 13) {
      $.get(url, function( data ) {
        $('DIV#hello').text(data.hello);
      });
    } else return true;
  });
});
