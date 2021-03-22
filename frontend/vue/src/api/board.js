import http from './http';

export async function get_category_list() {
    return http.get('/api/board/category/list/');
}
