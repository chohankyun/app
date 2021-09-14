export default {
    namespaced: true,
    state: {
        locale: 'none'
    },
    mutations: {
        setLocale(state, lang) {
            console.log(lang);
            if (lang === 'ko') {
                state.locale = 'ko_KR';
            } else {
                state.locale = 'en_US';
            }
        }
    },
    getters: {
        get_lang: function(state) {
            return state.locale.substring(0, 2);
        },
        get_locale: function(state) {
            return state.locale;
        }
    },
    actions: {}
};
