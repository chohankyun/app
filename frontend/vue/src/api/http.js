import axios from 'axios';
import Vue from 'vue';

const instance = axios.create({
    baseURL: '/'
});

instance.interceptors.request.use(
    function(config) {
        return config;
    },
    function(error) {
        return Promise.reject(error);
    }
);

instance.interceptors.response.use(
    function(response) {
        return response;
    },
    function(error) {
        if(error.response.status === 404 ){
            Vue.server_error(error);
            return;
        }
        if(error.response.status === 500 ){
            Vue.server_error(error);
            return;
        }
        return Promise.reject(error);
    }
);

export default instance;
