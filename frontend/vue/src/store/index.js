import Vue from 'vue';
import Vuex from 'vuex';
import createPersistedState from 'vuex-persistedstate';

Vue.use(Vuex);

import uauth from './uauth';
import board from './board';
import lang from './lang';
import chat from './chat';

export default new Vuex.Store({
    state: {},
    mutations: {},
    actions: {},
    modules: {
        uauth,
        board,
        lang,
        chat
    },
    plugins: [
        createPersistedState({
            paths: ['uauth', 'board', 'lang', 'chat']
        })
    ]
});
