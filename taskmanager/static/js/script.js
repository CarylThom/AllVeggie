document.addEventListener("DOMContentLoaded", function () {

  let modal = document.querySelectorAll('.modal');
  M.Modal.init(modal);

  // sidenav initialization
  let sidenav = document.querySelectorAll(".sidenav");
  M.Sidenav.init(sidenav);

  // select initialization
  let selects = document.querySelectorAll("select");
  M.FormSelect.init(selects);

  // collapsible initializataion
  let collapsibles = document.querySelectorAll(".collapsible");
  M.Collapsible.init(collapsibles);
});


  