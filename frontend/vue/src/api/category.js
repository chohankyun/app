import http from './http';

export async function get_range_list() {
    return http.get('/api/category/range/list/');
}
