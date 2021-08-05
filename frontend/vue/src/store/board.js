import * as board_api from '@/api/board';

export default {
    namespaced: true,
    state: {
        category_default: [
            { id: 'home', name: 'Home' },
            { id: 'all', name: 'All' }
        ],
        category_list: null,
        category_id: 'home'
    },
    mutations: {
        setCategoryList(state, category_list) {
            state.category_list = category_list;
        },
        setCategoryId(state, category_id) {
            console.log(category_id);
            state.category_id = category_id;
        }
    },
    actions: {
        async get_categories(context) {
            try {
                const response = await board_api.get_categories();

                if (response.status === 200) {
                    context.commit('setCategoryList', response.data);
                }
            } catch (e) {
                alert('카테고리 리스트 전송 실패.');
            }
        }
    }
};
