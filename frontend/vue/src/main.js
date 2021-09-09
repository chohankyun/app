import Vue from 'vue';
import App from '@/App.vue';
import router from '@/router';
import store from '@/store';
import i18n from '@/i18n';
import VueSweetalert2 from 'vue-sweetalert2';
import 'expose-loader?exposes[]=$&exposes[]=jQuery!jquery';
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import '@fortawesome/fontawesome-free/css/all.css';
import '@fortawesome/fontawesome-free/js/all.js';
import 'sweetalert2/dist/sweetalert2.min.css';
import util from '@/util';

Vue.config.productionTip = false;

const options = {
    position: 'center'
};

Vue.use(VueSweetalert2, options);
Vue.use(util);

new Vue({
    router,
    store,
    i18n,
    render: h => h(App)
}).$mount('#app');
