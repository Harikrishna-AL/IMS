// document.querySelector(".jsFilter").addEventListener("click", function () {
//   document.querySelector(".filter-menu").classList.toggle("active");
// });

// document.querySelector(".grid").addEventListener("click", function () {
//   document.querySelector(".list").classList.remove("active");
//   document.querySelector(".grid").classList.add("active");
//   document.querySelector(".products-area-wrapper").classList.add("gridView");
//   document
//     .querySelector(".products-area-wrapper")
//     .classList.remove("tableView");
// });

// document.querySelector(".list").addEventListener("click", function () {
//   document.querySelector(".list").classList.add("active");
//   document.querySelector(".grid").classList.remove("active");
//   document.querySelector(".products-area-wrapper").classList.remove("gridView");
//   document.querySelector(".products-area-wrapper").classList.add("tableView");
// });

function toggleMode() {
  var element = document.body;
  document.documentElement.classList.toggle("light");
  element.classList.toggle("active");

}
