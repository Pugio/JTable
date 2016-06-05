Template.meal_form.rendered = function () {
  var animation_props = { duration: 700, queue: false };
  if ($("#height-extender").length === 0)
    $('body').append('<div id="height-extender" style="height: 700px"></div>'); // hack to extend page height, so we can scroll all the way to the form
  
  $("#meal-form").show().animate({'opacity':'1'}, animation_props);
  $('html, body').animate({scrollTop: $("#meal-form").offset().top}, animation_props);
};

function submit_meal_form() {
  // Meteor.
  alert('submitting!!');
  // Insert a task into the collection
  // Tasks.insert({
  //   text,
  //   createdAt: new Date(), // current time
  // });
  
  // // Clear form
  // target.text.value = '';
}

Template.meal_form.events({

  // Triggered upon form submission if the user is NOT logged in
  'click .login-submit-meal': function (event) {
    event.preventDefault();

    if (Meteor.userId())  // we actually are logged in
      return submit_meal_form();

    Meteor.loginWithFacebook(function (err) {
      if (err)
        ;//bad
      else
        submit_meal_form();
    });
  },

  // Triggered upon form submission if the user IS logged in
  'click .submit-meal': function (event) {
     // Prevent default browser form submit
     event.preventDefault();

     submit_meal_form();
   }
});



function isGuest() { return Session.get('showMealForm') == 'find'; }

Template.meal_form.helpers({
  guest: isGuest,

  mealFormType: function() {
    var meal_form_type = Session.get('showMealForm');
    return meal_form_type.charAt(0).toUpperCase() + meal_form_type.slice(1);
  },

  meat_dairy_type: function() {
    return isGuest() ? 'checkbox' : 'radio';
  }
});

Template.meal_form_datepicker.rendered = function () {
  var today = new Date(), picker_start,
      days_from_now = 5 - today.getDay(),
      picker_start = days_from_now > 0 ?
                      new Date(today.valueOf() + 86400000 * days_from_now) :
                      today;
  
  abc = picker_start;
  this.$('input').fdatepicker({
    daysOfWeekDisabled: [0,1,2,3,4] // TODO: eventually update this to include yomim tovim
  });
}