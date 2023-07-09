"use strict";
var slideIndex = 1;
showDivs(slideIndex);

function plusDivs(n) {
  showDivs((slideIndex += n));
}

function showDivs(n) {
  var i;
  var x = document.getElementsByClassName("mySlides");
  if (n > x.length) {
    slideIndex = 1;
  }
  if (n < 1) {
    slideIndex = x.length;
  }
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  x[slideIndex - 1].style.display = "flex";
  x[slideIndex - 1].style.flexDirection = "column";
  x[slideIndex - 1].style.justifyContent = "space-around ";
  x[slideIndex - 1].style.alignItems = "center";

  $(".index").html(slideIndex);
}

let isMoreInfoOpened = {};
let isExist = {};
function showMoreInfo(firstInfo, secondInfo, wrapperTotalReq, seeMoreBtn) {
  let firstElement = document.getElementById(`${firstInfo}`).style;
  let secondElement = document.getElementById(`${secondInfo}`).style;
  let thirdElement = document.getElementById(`${wrapperTotalReq}`).style;
  let fourthElement = document.getElementById(`${seeMoreBtn}`);
  for (let property in isMoreInfoOpened) {
    if (property == `${firstInfo}`) {
      isExist[`${firstInfo}`] = true;
    }
  }

  if (isExist[`${firstInfo}`]) {
    if (isMoreInfoOpened[`${firstInfo}`] == false) {
      isMoreInfoOpened[`${firstInfo}`] = true;
      firstElement.opacity = "100%";
      secondElement.opacity = "100%";
      thirdElement.height = "30rem";
      fourthElement.innerHTML = "کمتر";
    } else {
      isMoreInfoOpened[`${firstInfo}`] = false;
      firstElement.opacity = "0%";
      secondElement.opacity = "0%";
      thirdElement.height = "27rem";
      fourthElement.innerHTML = "مشاهده بیشتر";
    }
  } else {
    isMoreInfoOpened[`${firstInfo}`] = true;
    firstElement.opacity = "100%";
    secondElement.opacity = "100%";
    thirdElement.height = "30rem";
    fourthElement.innerHTML = "کمتر";
  }

  console.log(isMoreInfoOpened, isExist);
}
