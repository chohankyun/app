import http from './http';

export async function get_home_posts(order) {
    return http.get('/api/home/posts/', { params: { order: order } });
}
