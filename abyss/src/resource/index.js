
var Vue = require('vue').default;
exports.user = Vue.resource('/api/users');
exports.auth = Vue.resource('/api/auth');