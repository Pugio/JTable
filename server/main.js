Meteor.startup(function () {
  configureFacebook = function(config) {
    ServiceConfiguration.configurations.upsert( { service: 'facebook' }, { $set: config });
  };

  // set the settings object with meteor --settings settings-development.json
  var facebookConfig = Meteor.settings.facebook;
  if(facebookConfig) {
      console.log('Got settings for facebook', facebookConfig);
      configureFacebook(facebookConfig);
  }
});