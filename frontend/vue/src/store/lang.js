export default {
    namespaced: true,
    state: {
        locale: 'none'
    },
    mutations: {
        setLocale(state, lang) {
            if (lang === 'ko') {
                state.locale = 'ko_KR';
            } else {
                state.locale = 'en_US';
            }
        }
    },
    getters: {
        lang: function(state) {
            return state.locale.substring(0, 2);
        },
        locale: function(state) {
            return state.locale;
        }
    },
    actions: {}
};
