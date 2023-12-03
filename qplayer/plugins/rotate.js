function rotate() {
  var dimension = 0;

  //   var rotateLeftButton = createButton("&#8635;");
  //   var rotateRightButton = createButton("&#8634;");
  var rotateLeftButton = createButton("<");
  var rotateRightButton = createButton(">");
  // add

  var playbackRate = document.querySelector(".vjs-playback-rate");
  insertAfter(rotateLeftButton, playbackRate);
  insertAfter(rotateRightButton, rotateLeftButton);

  rotateLeftButton.onclick = function () {
    console.log("<<<<<<<<<< left button clicked");
  };

  rotateRightButton.onclick = function () {
    console.log(">>>>>>> right button clicked");
  };

  function createButton(icon) {
    var button = document.createElement("button");
    button.classList.add("vjs-menu-button");
    button.innerHTML = icon;
    button.style.fontSize = "1.86.em";
    return button;
  }

  function insertAfter(newEl, element) {
    console.log("new button = ", newEl);
    console.log("play back rate button = ", newEl);
    element.parentNode.insertBefore(newEl, element.nextSibling);
  }
}

videojs.registerPlugin("rotate", rotate);
