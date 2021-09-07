import router from '@/router';
import * as user_api from '@/api/user';

export default {
    namespaced: true,
    state: {
        user: ''
    },
    mutations: {
        setUser(state, user) {
            state.user = user;
        }
    },
    actions: {
        async login(context, credentials) {
            try {
                const response = await user_api.login(credentials);
                context.commit('setUser', response.data);
                router.push('/').catch(() => {
                });
            } catch (e) {
                if (e.response.data.detail !== undefined) {
                    alert(e.response.data.detail);
                } else {
                    alert(e.response.status + ' : ' + e.response.statusText);
                }
            }
        },
        async logout(context) {
            try {
                await user_api.logout();
            } catch (e) {
                if (e.response.data.detail !== undefined) {
                    alert(e.response.data.detail);
                } else {
                    alert(e.response.status + ' : ' + e.response.statusText);
                }
                context.commit('setUser', '');
                await router.push('/').catch(() => {
                });
            }
        },
        async is_auth(context) {
            try {
                await user_api.is_auth();
            } catch (e) {
                context.commit('setUser', '');
            }
        },
    }
};
