import * as board_api from '@/api/board';

export default {
    namespaced: true,
    state: {
        category_list: null
    },
    mutations: {
        setCategoryList(state, category_list) {
            state.category_list = category_list;
        }
    },
    actions: {
        async get_category_list(context) {
            try {
                const response = await board_api.get_category_list();

                if (response.status === 200) {
                    context.commit('setCategoryList', response.data);
                }
            } catch (e) {
                alert('카테고리 리스트 전송 실패.');
            }
        },
    }
};
