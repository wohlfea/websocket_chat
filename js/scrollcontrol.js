var scrolled = false;

function updateScroll(){
    if(!scrolled){
        window.scrollTo(0,document.body.scrollHeight);
        scrolled = false;
    } else {
        if($(window).scrollTop() + $(window).height() >= $(document).height() - 100) {
            scrolled = false;
        }
    }
}

$(window).on('scroll', function(){
    if($(window).scrollTop() + $(window).height() <= $(document).height() - 100) {
        scrolled = true;
    }
});
