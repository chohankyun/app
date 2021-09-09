import Vue from 'vue';
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
                Vue.server_message('22222222222222222222222222');
                const res = await user_api.login(credentials);
                context.commit('setUser', res.data);
                router.push('/').catch(() => {
                });
            } catch (e) {
                // util.$server_error(e);
            }
        },
        async logout(context) {
            try {
                await user_api.logout();
            } catch (e) {
                // util.$server_error(e);
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
