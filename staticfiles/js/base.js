$('.navTrigger').click(function() {
    $(this).toggleClass('active');
    // console.log("Clicked menu");
    $("#menu-wrapper").fadeToggle("3000");
});

function setFooterStyle() {
    var docHeight = $(window).height();
    var footerHeight = $('.footer').outerHeight();
    var footerTop = $('.footer').position().top + footerHeight;
    if (footerTop < docHeight) {
        $('.footer').css('margin-top', (docHeight - footerTop + 'px'));
    } else {
        $('.footer').css('margin-top', '');
    }
    $('.footer').removeClass('invisible');
}

function setMargin(){
    var elemHeight = $("body > div").height();
    $('.top-margin').css('margin-top', (elemHeight + 5 + 'px'));
}

$(document).ready(function() {
    setFooterStyle();
    window.onresize = setFooterStyle;
    setMargin();
});

$(window).on("load", function() {
    $(".loader-wrapper").fadeOut("slow");
});