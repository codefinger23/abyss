// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import VueResource from 'vue-resource'
import 'jquery'
import "./assets/semantic/semantic.min.css"
import "./assets/semantic/semantic.min.js"
Vue.config.productionTip = false
Vue.use(VueResource);
global.api = require('./resource');
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
