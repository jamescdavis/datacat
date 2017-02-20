import DS from 'ember-data';

export default DS.Model.extend({
    title: DS.attr(),
    url: DS.attr(),
    "dataset-publications": DS.hasMany('dataset-publication')
});
