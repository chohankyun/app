import http from './http';

export async function get_categories() {
    return http.get('/api/board/categories/');
}

export async function create_post(post) {
    return http.post('/api/board/posts/', post);
}

export async function get_post(id) {
    return http.get('/api/board/posts/' + id);
}

export async function get_posts_by_category_order(category, order) {
    return http.get('/api/board/posts/' + category + '/' + order);
}

export async function get_posts_for_home(order) {
    return http.get('/api/home/posts/' + order);
}

export async function create_reply(reply) {
    return http.post('/api/board/replies/', reply);
}

export async function get_replies_post(post_id) {
    return http.get('/api/board/replies/post/' + post_id);
}

export async function search_post(search_word, order) {
    return http.get('/api/search/posts/' + search_word + '/' + order);
}
