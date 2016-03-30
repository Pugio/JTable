Meteor.startup(function () {
  // code to run on server at startup
  DeleteThisCollection = new Mongo.Collection("deletecollection");
  DeleteThisCollection.insert({ text: "Hello world!", createdAt: new Date() });
});