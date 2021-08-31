import Vue from 'vue';
import Vuex from 'vuex';
import createPersistedState from 'vuex-persistedstate';

Vue.use(Vuex);

import join from './join';
import board from './board';
import lang from './lang';

export default new Vuex.Store({
    state: {},
    mutations: {},
    actions: {},
    modules: {
        join,
        board,
        lang
    },
    plugins: [
        createPersistedState({
            paths: ['join', 'board', 'lang']
        })
    ]
});
