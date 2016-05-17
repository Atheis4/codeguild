'use strict';

function getRawColorString() {
  return $('#color-input').val();
}

/*
Take a color value between 0 and 1 and return it between 0 and 255 as an "int"
*/
function renormalizeColor(componentValue) {
  return Math.round(componentValue * 255);
}

/*
Take Raw user input string "0 1 0" and convert to CSS color string like "rgb(0, 255, 0)"
*/
function convertRawColorToCSSColor () {
  var colorComponentStrings = _.split(rawColor, ' ');
  var colorComponentNumbers = _.map(colorComponentStrings, Number);
  var normalizedColorComponents = _.map(
    colorComponentNumbers, renormalizeColor);

  var joinedColorComponents = _.join(colorComponents, ', ');

  return 'rgb(' + joinedColorComponents + ')';
}

function selectSwatch () {
  return $('.swatch');
}

function applyCSSCOlorAsBackground(element, cssColor) {

}
