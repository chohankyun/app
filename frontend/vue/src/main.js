import Vue from 'vue';
import App from '@/App.vue';
import router from '@/router';
import store from '@/store';
import i18n from '@/i18n';
import util from '@utul';
import 'expose-loader?exposes[]=$&exposes[]=jQuery!jquery';
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import '@fortawesome/fontawesome-free/css/all.css';
import '@fortawesome/fontawesome-free/js/all.js';

Vue.config.productionTip = false;
Vue.use(util);

new Vue({
    router,
    store,
    i18n,
    util,
    render: h => h(App)
}).$mount('#app');
