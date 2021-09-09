export default {
    install(Vue) {
        const server_message = function(res) {
            Vue.alert(res);
            // alert(res);
            // alert(res.data.detail);
            return true;
        };
        const server_error = function(error) {
            if (error.response.data.detail !== undefined) {
                alert(error.response.data.detail);
            } else {
                alert(error.response.status + ' : ' + error.response.statusText);
            }
            return true;
        };
        const client_error = function(error) {
            alert(error.response.data.detail);
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
