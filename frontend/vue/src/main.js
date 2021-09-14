import Vue from 'vue';
import App from '@/App.vue';
import router from '@/router';
import store from '@/store';
import i18n from '@/i18n';
import 'expose-loader?exposes[]=$&exposes[]=jQuery!jquery';
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import '@fortawesome/fontawesome-free/css/all.css';
import '@fortawesome/fontawesome-free/js/all.js';
import sweetalert from '@/utils/sweetalert';
import '@/utils/dayjs';
import '@/utils/filters';

Vue.config.productionTip = false;

Vue.use(sweetalert);

new Vue({
    router,
    store,
    i18n,
    render: h => h(App)
}).$mount('#app');
