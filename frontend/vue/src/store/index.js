import Vue from 'vue';
import Vuex from 'vuex';
import createPersistedState from 'vuex-persistedstate';

Vue.use(Vuex);

import user from './user';
import board from './board';

export default new Vuex.Store({
    state: {},
    mutations: {},
    actions: {},
    modules: {
        user,
        board
    },
    plugins: [
        createPersistedState({
            paths: ['user', 'board']
        })
    ]
});
