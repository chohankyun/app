export default {
    install(Vue) {
        const server_message = function(res) {
            alert(res);
            // alert(res.data.detail);
            return true;
        };
        Vue.server_message = server_message;
        Vue.prototype.$server_message = server_message;

        const server_error = function(error) {
            if (error.response.data.detail !== undefined) {
                alert(error.response.data.detail);
            } else {
                alert(error.response.status + ' : ' + error.response.statusText);
            }
            return true;
        };
        Vue.server_error = server_error;
        Vue.prototype.$server_error = server_error;

        const client_error = function(error) {
            alert(error.response.data.detail);
            return true;
        };
        Vue.client_error = client_error;
        Vue.prototype.$client_error = client_error;
    }
};
