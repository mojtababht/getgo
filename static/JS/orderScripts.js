"use strict";
function textOfBtnEnterMouse() {
  let btnPayElement = document.getElementById("payBtn");
  btnPayElement.innerText = "";
  let createNodeImageOne = document.createElement("img");
  createNodeImageOne.setAttribute("src", "../static/image/box1.png");
  createNodeImageOne.setAttribute("id", "boxPic");
  let createNodeImageTwo = document.createElement("img");
  createNodeImageTwo.setAttribute("src", "../static/image/truck1.png");
  createNodeImageTwo.setAttribute("id", "truckPic");
  btnPayElement.appendChild(createNodeImageTwo);
  btnPayElement.appendChild(createNodeImageOne);
}

function textOfBtnLeaveMouse() {
  let btnPayElement = document.getElementById("payBtn");
  btnPayElement.innerText = "پرداخت";
}
