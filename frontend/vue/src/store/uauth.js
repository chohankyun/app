import Vue from 'vue';
import router from '@/router';
import * as uauth_api from '@/api/uauth';

export default {
    namespaced: true,
    state: {
        user: ''
    },
    mutations: {
        setUser(state, user) {
            state.user = user;
        },
        setUserName(state, user_name) {
            console.log(user_name);
            state.user.name = user_name;
        }
    },
    actions: {
        async login(context, credentials) {
            try {
                const response = await uauth_api.login(credentials);
                context.commit('setUser', response.data);
                router.push('/');
            } catch (error) {
                Vue.server_error(error);
            }
        },
        async logout(context) {
            try {
                await uauth_api.logout();
            } catch (error) {
                await Vue.server_error(error);
                context.commit('setUser', '');
                router.push('/').catch(() => {
                });
            }
        },
        async is_auth(context) {
            try {
                await uauth_api.is_auth();
            } catch (error) {
                context.commit('setUser', '');
            }
        }
    }
};
