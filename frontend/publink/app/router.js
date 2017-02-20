import Ember from 'ember';
import config from './config/environment';

const Router = Ember.Router.extend({
  location: config.locationType,
  rootURL: config.rootURL
});

Router.map(function() {
  this.route('datasets');
  this.route('publications');
  this.route('dataset-publications');
});

export default Router;
