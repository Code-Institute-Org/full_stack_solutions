$(document).ready(function() {
    $(".stream-nav").on("click", function() {
        /**
         * When we click on an element that has
         * a 'box' class, this event will be fired.
         */
        var elementId = $(this).attr("id");
        var cardClass = $(".card").attr("class").split(" ")[0];

        if ($("." + elementId).css("background-color") == "rgb(235, 82, 85)") {
            $("." + elementId).css("background-color", "#fff");
        } else {
            $("." + cardClass).css("background-color", "#fff");
            $("." + elementId).css("background-color", "rgb(235, 82, 85)");
        }
    });
});
