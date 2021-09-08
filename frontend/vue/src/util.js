export default {
    install(Vue) {
        Vue.prototype.$server_message = function(res) {
            alert(res.data.detail);
        };
        Vue.prototype.$server_error = function(error) {
            if (error.response.data.detail !== undefined) {
                alert(error.response.data.detail);
            } else {
                alert(error.response.status + ' : ' + error.response.statusText);
            }
        };
        Vue.prototype.$client_error = function(error) {
            alert(error.response.data.detail);
        };
    }
};
