import http from './http';

export async function search_post(search_word, order) {
    return http.get('/api/search/posts/', { params: { search_word: search_word, order: order } });
}
