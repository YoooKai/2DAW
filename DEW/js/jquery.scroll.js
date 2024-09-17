// 指定したボックス内をスムーススクロール
$(window).on('load resize', function() {
  var win = window.innerWidth ? window.innerWidth : $(window).width();
  $('a[href^=#]').click(function() {
    if (win <= 600 || !$(this).data('box')) {
      var speed = 500;
      var href = $(this).attr("href");
      var target = $(href == "#" || href == "" ? 'html' : href);
      var position = target.offset().top;
      $('body,html').animate({scrollTop:position}, speed, 'swing');
    }
    else {
      var $box = $($(this).data('box'));
      var $tareget = $($(this).attr('href'));
      var dist = $tareget.position().top - $box.position().top;
      $box.stop().animate({
        scrollTop: $box.scrollTop() + dist
      });
    }
    return false;
  });
});