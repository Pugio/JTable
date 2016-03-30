Template.meal_form.rendered = function () {
  var animation_props = { duration: 700, queue: false };
  if ($("#height-extender").length == 0)
    $('body').append('<div id="height-extender" style="height: 700px"></div>'); // hack to extend page height, so we can scroll all the way to the form
  
  $("#meal-form").show().animate({'opacity':'1'}, animation_props);
  $('html, body').animate({scrollTop: $("#meal-form").offset().top}, animation_props);
}

Template.meal_form.helpers({
  guest: function() {
    return Session.get('showMealForm') == 'find';
  },

  mealFormType: function() {
    var meal_form_type = Session.get('showMealForm');
    return meal_form_type.charAt(0).toUpperCase() + meal_form_type.slice(1);
  }
});

Template.meal_form_datepicker.rendered = function () {
  this.$('input').fdatepicker({
    daysOfWeekDisabled: [0,1,2,3,4] // TODO: eventually update this to include yomim tovimte
  });
}