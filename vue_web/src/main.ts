import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';

// View UI
import ViewUI from "view-design";
import 'view-design/dist/styles/iview.css';
// Bootstrap
import BootstrapVue from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
//Font Awesome
import '@fortawesome/fontawesome-free/css/all.min.css';


Vue.config.productionTip = false;
Vue.use(ViewUI);
Vue.use(BootstrapVue);

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
