navToggleButton = document.getElementById("toggle_nav")
navOpenIcon = document.getElementById("open_icon")
navCloseIcon = document.getElementById("close_icon")

$(navCloseIcon).hide();

$(navToggleButton).click(function(){
    $(navOpenIcon).toggle();
    $(navCloseIcon).toggle();
});
$(navOpenIcon).click(
    function () {
        document.getElementById("header").style.flex = "0 0 auto";
      }
)
$(navCloseIcon).click(
    function () {
        document.getElementById("header").style.flex = "0 0 80px";
      }
)