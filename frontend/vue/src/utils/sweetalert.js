import Vue from 'vue';
import i18n from '@/i18n';
import VueSweetalert2 from 'vue-sweetalert2';
import 'sweetalert2/dist/sweetalert2.min.css';

const options = {
    width: 'auto',
    confirmButtonColor: '#17a2b8',
    confirmButtonText: i18n.t('Confirm')
};

Vue.use(VueSweetalert2, options);

export default {
    install(Vue) {
        const server_message = function(response) {
            Vue.swal({ text: response.data.detail });
            return true;
        };
        const server_error = function(error) {
            if (error.response.data.detail !== undefined) {
                Vue.swal({ text: error.response.data.detail });
            } else {
                Vue.swal({ text: error.response.status + ' : ' + error.response.statusText });
            }
            return true;
        };
        const client_error = function(error) {
            Vue.swal({ text: error });
            return true;
        };

        Vue.server_message = server_message;
        Vue.server_error = server_error;
        Vue.client_error = client_error;

        Vue.prototype.$server_message = server_message;
        Vue.prototype.$server_error = server_error;
        Vue.prototype.$client_error = client_error;
    }
};
