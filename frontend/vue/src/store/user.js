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
                const response = await user_api.login(credentials);
                context.commit('setUser', response.data);
                router.push('/').catch(() => {
                });
            } catch (error) {
                Vue.server_error(error);
            }
        },
        async logout(context) {
            try {
                await user_api.logout();
            } catch (error) {
                Vue.server_error(error);
                context.commit('setUser', '');
                router.push('/').catch(() => {
                });
            }
        },
        async is_auth(context) {
            try {
                await user_api.is_auth();
            } catch (error) {
                context.commit('setUser', '');
            }
        },
    }
};
