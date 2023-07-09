"use strict";
function hoveringMenu(idOfRecElement) {
  let recElement = document.getElementById(idOfRecElement).style;
  recElement.width = "100%";
  recElement.transition = "0.3s";
}

function undoHoveringMenu(idOfRecElement) {
  let recElement = document.getElementById(idOfRecElement).style;
  recElement.width = "0%";
  recElement.transition = "0.3s";
}

let menuIsOpen = false;
function clickingMenuBtn() {
  let menuSideElement = document.getElementById("wrapperSideMenu").style;
  let menuIconElement = document.getElementById("menuIcon");

  if (!menuIsOpen) {
    menuSideElement.right = "0vw";
    menuSideElement.transition = "1s";
    menuIconElement.setAttribute(
      "src",
      "../static/image/cross-svgrepo-com1.svg"
    );
    menuIsOpen = true;
  } else {
    menuSideElement.right = "-47vw";
    menuSideElement.transition = "0.5s";
    menuIconElement.setAttribute("src", `../static/image/MenuIcon.svg`);
    menuIsOpen = false;
  }
}

function resizingWindow() {
  let screenWidth = screen.width;
  let menuSideElement = document.getElementById("wrapperSideMenu").style;
  let menuIconElement = document.getElementById("menuIcon");
  if (screenWidth > 850) {
    menuSideElement.right = "-47vw";
    menuIconElement.setAttribute("src", `../static/image/MenuIcon.svg`);
    menuIsOpen = false;
  }
}

window.onscroll = function () {
  scrollingPage();
};
function scrollingPage() {
  let navbarElement = document.getElementById("headerPart").style;
  if (document.body.scrollTop !== 0) {
    navbarElement.boxShadow = "0 0.5px 5px rgba(128, 128, 128, 0.744)";
  } else {
    navbarElement.boxShadow = "none";
  }
}
