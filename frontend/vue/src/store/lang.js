export default {
    namespaced: true,
    state: {
        locale: 'none'
    },
    mutations: {
        setLocale(state, language) {
            if (language === 'ko') {
                state.locale = 'ko_KR';
            } else {
                state.locale = 'en_US';
            }
        }
    },
    actions: {}
};
