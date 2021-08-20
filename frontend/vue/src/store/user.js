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
        async login(context, { app_id, password }) {
            try {
                const response = await user_api.login(app_id, password);
                context.commit('setUser', response.data);
                await router.push('/');
            } catch (e) {
                alert('사용자 정보 전송 실패.');
            }
        },
        async logout(context) {
            try {
                await user_api.logout();
            } catch (e) {
                context.commit('setUser', '');
                alert('로그 아웃.');
                await router.push('/');
            }
        },
        async is_auth(context) {
            try {
                await user_api.is_auth();
            } catch (e) {
                context.commit('setUser', '');
                Vue.$log.debug('인증 정보 전송 실패.');
            }
        },
        async register(context, register) {
            try {
                const response = await user_api.create_register(register);
                context.commit('setUser', response.data);
                await router.push('/');
            } catch (e) {
                alert('사용자 정보 전송 실패.');
            }
        },
    }
};
