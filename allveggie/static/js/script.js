/* jshint esversion: 11 */

document.addEventListener("DOMContentLoaded", function () {

  // sidenav initialization
  let sidenav = document.querySelectorAll(".sidenav");
  M.Sidenav.init(sidenav);

  // select initialization
  let selects = document.querySelectorAll("select");
  M.FormSelect.init(selects);

  // collapsible initializataion
  let collapsibles = document.querySelectorAll(".collapsible");
  M.Collapsible.init(collapsibles);

  // modal initialization
  let modal = document.querySelectorAll('.modal');
  M.Modal.init(modal);
});