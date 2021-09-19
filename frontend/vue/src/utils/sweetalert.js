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
        const server_message = function (response) {
            return Vue.swal({text: i18n.t(response.data.detail)});
        };
        const server_error = function (error) {
            if (error.response.data.detail !== undefined) {
                return Vue.swal({text: i18n.t(error.response.data.detail)});
            } else {
                return Vue.swal({text: error.response.status + ' : ' + i18n.t(error.response.statusText)});
            }
        };
        const client_message = function (message) {
            return Vue.swal({text: i18n.t(message)});
        };
        const client_error = function (error) {
            return Vue.swal({text: i18n.t(error)});
        };
        const client_confirm = function (button_text, confirm_message) {
            return Vue.swal({
                showCancelButton: true,
                focusConfirm: false,
                confirmButtonColor: '#d33',
                confirmButtonText: i18n.t(button_text),
                cancelButtonText: i18n.t('Cancel'),
                text: i18n.t(confirm_message)
            });
        };

        Vue.server_message = server_message;
        Vue.server_error = server_error;
        Vue.client_message = client_message;
        Vue.client_error = client_error;
        Vue.client_confirm = client_confirm;

        Vue.prototype.$server_message = server_message;
        Vue.prototype.$server_error = server_error;
        Vue.prototype.$client_message = client_message;
        Vue.prototype.$client_error = client_error;
        Vue.prototype.$client_confirm = client_confirm;
    }
};
