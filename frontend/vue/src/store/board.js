import util from '@/util';
import * as board_api from '@/api/board';

export default {
    namespaced: true,
    state: {
        category_id: 'home',
        category_default: [
            { id: 'home', name: 'Home' },
            { id: 'all', name: 'All' }
        ],
        categories: []
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
        async init_categories(context) {
            try {
                const response = await board_api.get_categories();
                context.commit('setCategories', response.data);
            } catch (error) {
                context.commit('setCategories', []);
                util.$server_error(error);
            }
        }
    }
};
