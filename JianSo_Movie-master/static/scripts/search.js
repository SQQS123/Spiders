//=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=
//
//          BY BUT0N
//
//=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=
(function (doc, win) {
    var docEl = doc.documentElement,
    resizeEvt = 'orientationchange' in window ? 'orientationchange' : 'resize',
    recalc = function () {
        var clientWidth = docEl.clientWidth;
        if (!clientWidth) return;
        docEl.style.fontSize = 20 * (clientWidth / 320) + 'px';
    };

    if (!doc.addEventListener) return;
    win.addEventListener(resizeEvt, recalc, false);
    doc.addEventListener('DOMContentLoaded', recalc, false);
})(document, window);

$(function() {
    $(".label-title").each(function(i,e) {
        $(e).click(function() {
            // $(".item").removeClass("item-active");
            $(".item-active").find(".dash-label").click()
            $(e).parent().parent().addClass("item-active");
            $(e).text($(e).parent().parent().attr("_src"));
        })
    });
    $('.dash-label').each(function(i,e) {
        $(e).click(function() {
            $(e).parent().parent().removeClass("item-active");
            $(e).parent().next().next().find(".label-title").text($(e).text())
        });
    });
    $('.dash-icon').each(function(i,e) {
        $(e).click(function() {
            window.location.href = $(e).parent().parent().attr("_src")
        });
    });
    $('.item-img').each(function(i,e) {
        $(e).click(function() {
            $(e).next().children().eq(0).click()
        });
    });
});
