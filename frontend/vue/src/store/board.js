import * as board_api from '@/api/board';

export default {
    namespaced: true,
    state: {
        category_id: 'home',
        category_default: [
            { id: 'home', name: 'Home' },
            { id: 'all', name: 'All' }
        ],
        categories: null
    },
    mutations: {
        setCategories(state, categories) {
            state.category_list = categories;
        },
        setCategoryId(state, category_id) {
            state.category_id = category_id;
        }
    },
    actions: {
        async set_categories(context) {
            try {
                const response = await board_api.get_categories();
                context.commit('setCategories', response.data);
            } catch (e) {
                context.commit('setCategories', null);
                alert(e.message);
            }
        }
    }
};
