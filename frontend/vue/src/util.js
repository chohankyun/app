export default {
    install(Vue) {
        const server_message = function (res) {
            Vue.swal(res.data.detail).then(() => {
            });
            return true;
        };
        const server_error = function (error) {
            if (error.response.data.detail !== undefined) {
                Vue.swal(error.response.data.detail).then(() => {
                });
            } else {
                Vue.swal(error.response.status + ' : ' + error.response.statusText).then(() => {
                });
            }
            return true;
        };
        const client_error = function (error) {
            Vue.swal(error).then(() => {
            });
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
