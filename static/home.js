if ($(".text-slider").length == 1) {
  
    var typed_strings = 
        $(".text-slider-items").text();

    var typed = new Typed(".text-slider", {
        strings: ["Hi", "Im", "Lakee"],
        typeSpeed: 50,
        loop: false,
        backDelay: 900,
        backSpeed: 30,
    });
}