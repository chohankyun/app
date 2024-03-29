import http from './http';

export async function get_posts(search_word, order) {
    return http.get('/api/search/posts', { params: { search_word: search_word, order: order } });
}
