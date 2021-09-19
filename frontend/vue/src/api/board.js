import http from './http';

export async function get_categories() {
    return http.get('/api/board/categories');
}

export async function create_post(post) {
    return http.post('/api/board/posts', post);
}

export async function update_post(post) {
    return http.put('/api/board/posts/' + post.id, post);
}

export async function get_post(post_id) {
    return http.get('/api/board/posts/' + post_id);
}

export async function get_posts(category, order) {
    return http.get('/api/board/posts', {params: {category: category, order: order}});
}

export async function create_reply(reply) {
    return http.post('/api/board/replies', reply);
}

export async function update_reply(reply) {
    return http.put('/api/board/replies/' + reply.id, reply);
}

export async function get_replies(post_id) {
    return http.get('/api/board/posts/' + post_id + '/replies');
}

export async function create_recommend(recommend) {
    return http.post('/api/board/recommends', recommend);
}

export async function delete_recommend(post_id) {
    return http.delete('/api/board/recommends/' + post_id);
}

export async function get_recommend_toggle(post_id) {
    return http.get('/api/board/posts/' + post_id + '/recommend-toggle');
}
