"use strict";

function getUrl () {
  return $("#url-input").val();
}

function createImgElem () {
  var imgElement = $("<img>").attr("src", getUrl());
  return imgElement;
}

function createImgLink () {
  var imgLink = $("<a></a>").text("Image Source").attr("href", getUrl());
  return imgLink;
}

function createTile () {
  var imgElement = createImgElem();
  var imgLink = createImgLink();
  var newTile = $("<div></div>").append(imgElement, imgLink);
  return newTile;
}

function createDelLink (newTile) {
  var delLink = $("<button></button>").text("remove").attr("href", "");
  delLink.on("click", function (event) {
    event.preventDefault();
    newTile.remove("div");
    $("h2").text("Current Tile(s): " + countTiles());
  });
  return newTile.append(delLink);
}

function addTileToGallery (newTile) {
  $("#gallery").append(newTile)
}

function createTileAndAddToGallery () {
  var newTile = createDelLink(createTile());
  addTileToGallery(newTile);
}

function countTiles () {
  var tileCount = $("div").length;
  return tileCount;
}

function clearTextBox () {
  $("textbox").text();
}

function registerEventHandlers () {
  $("form").on("submit", function (event) {
    event.preventDefault ();
    createTileAndAddToGallery ();
    $("h2").text("Current Tile(s): " + countTiles());
    $("#url-input").val("");
  })
}

$(document).ready(function () {
  registerEventHandlers();
});
