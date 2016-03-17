// counter starts at 0
Session.setDefault('counter', 0);

Template.host_find_buttons.events({
  'click button': function () {

    var animation_props = { duration: 700, queue: false };
    $('body').append('<div style="height: 700px"></div>'); // hack to extend page height, so we can scroll all the way to the form
    
    $("#meal-form").show().animate({'opacity':'1'}, animation_props);
    $('html, body').animate({scrollTop: $("#meal-form").offset().top}, animation_props);
  }
});
