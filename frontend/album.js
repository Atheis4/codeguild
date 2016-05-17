"use strict";

function getUrl () {
  return $("#url-input").val();
}

function createImgElement () {
  var imgElement = $("<img>").attr("src", getUrl());
  return imgElement;
}

function createNewLink () {
  var newLink = $("<a>SOME TEXT</a>").attr("href", getUrl());
  return newLink;
}

function createDelLink (newDiv) {
  var delLink = $("<a></a>").text("X").attr("href", "");
  delLink.on("click", function (event) {
    event.preventDefault();
    newDiv.remove("div");
    });
  return delLink;
}

function addImgToDiv (imgElement, newLink, delLink) {
  var newDiv = $("<div></div>").append(imgElement, newLink, delLink);
  return newDiv;
}

function addDivToSection (newDiv) {
  $("#gallery").append(newDiv);
}

function registerGlobalEventHandlers () {
  $("form").on("submit", function (event) {
    event.preventDefault();
    var imgElement = createImgElement();
    var newLink = createNewLink();
    var delLink = createDelLink();
    var newDiv = addImgToDiv(imgElement, newLink, delLink);
    addDivToSection(newDiv);
  });
}

$(document).ready(function () {
  registerGlobalEventHandlers();
})
