$('.navTrigger').click(function() {
    $(this).toggleClass('active');
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

function setCardHeight() {
    var services = $('.services').height()
    var contacts = $('.contacts').height()
    var map = $('.map').height()
    maxHeight = Math.max(services, contacts, map)
    $('.services').css('height', maxHeight)
    $('.contacts').css('height', maxHeight)
    $('.map').css('height', maxHeight)
}

function setMargin(){
    var elemHeight = $("body > div").height();
    $('.top-margin').css('margin-top', (elemHeight + 5 + 'px'));
}

$(document).ready(function() {
    setFooterStyle();
    window.onresize = setFooterStyle();
    window.onresize = setCardHeight();
    window.onresize = setMargin();
    setMargin();
    setCardHeight();
});

$(window).on("load", function() {
    $(".loader-wrapper").fadeOut("slow");
});