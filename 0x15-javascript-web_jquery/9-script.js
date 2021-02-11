// fetches from https://fourtonfish.com/hellosalut/?lang=fr and displays
//    the value of hello from that fetch in the HTML’s tag DIV#hello.
// The translation of “hello” must be displayed in the HTML tag DIV#hello
// must work when it is imported from the HEAD tag
document.addEventListener('DOMContentLoaded', function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function( data ) {
    $('DIV#hello').text(data.hello);
  });
});
