import * as user_api from '@/api/user';

export default {
    namespaced: true,
    state: {
        user: null
    },
    mutations: {
        setUser(state, user) {
            state.user = user;
        }
    },
    actions: {
        async login(context, {app_id, password}) {
            try {
                const response = await user_api.login(app_id, password);

                if (response.status === 200) {
                    context.commit('setUser', response.data);
                    window.location.href = '/';
                }
            } catch (e) {
                alert('사용자 정보 전송 실패.');
            }
        },
        async logout(context) {
            try {
                await user_api.logout();
            } catch (e) {
                context.commit('setUser', '');
                window.location.href = '/';
                console.log('로그 아웃.');
            }
        },
        async is_auth(context) {
            try {
                await user_api.is_auth();
            } catch (e) {
                context.commit('setUser', '');
                console.log('인증 정보 전송 실패.');
            }
        }
    }
};
