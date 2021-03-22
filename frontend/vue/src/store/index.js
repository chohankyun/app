import Vue from 'vue';
import Vuex from 'vuex';
import createPersistedState from 'vuex-persistedstate';

Vue.use(Vuex);

import board from './board';

export default new Vuex.Store({
    state: {},
    mutations: {},
    actions: {},
    modules: {
        board
    },
    plugins: [
        createPersistedState({
            paths: ['board'],
        })
    ]
});
