import DS from 'ember-data';

export default DS.Model.extend({
    dataset: DS.belongsTo('dataset'),
    publication: DS.belongsTo('publication')
});
