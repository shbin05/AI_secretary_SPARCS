var isClicked = false;

function micClicked() {
  var image = document.querySelector('#mic');
  if (isClicked) {
    image.src = 'images/mic-on.svg';
    isClicked = false;
  } else {
    image.src = 'images/mic-off.svg';
    isClicked = true;
  }
}
