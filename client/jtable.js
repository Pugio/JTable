// counter starts at 0
Session.setDefault('counter', 0);

Template.host_find_buttons.events({
  'click button': function (event) {
    var meal_form_type = event.target.id.replace(/btn-(\w+)-a-meal/,"$1");
    Session.set('showMealForm', meal_form_type); // either 'host' or 'find'

    if ($("#meal-form").length > 0)
      Template.meal_form.rendered();
  }
});


Template.body.helpers({
  showMealForm: function() {
    return Session.get('showMealForm');
  }
});


fakey = new Mongo.Collection('fakey');