import http from './http';

export async function login(credentials) {
    return http.post('/api/user/login', credentials);
}

export async function is_auth() {
    return http.get('/api/user/is-auth');
}

export async function logout() {
    return http.get('/api/user/logout');
}

export async function register_user(register) {
    return http.post('/api/user/register', register);
}

export async function find_uid(email) {
    return http.post('/api/user/uid/find', email);
}

export async function reset_password(email) {
    return http.post('/api/user/password/reset', email);
}

export async function get_user(user_id) {
    return http.get('/api/user/users/' + user_id);
}

export async function change_password(change) {
    return http.post('/api/user/password/change', change);
}

export async function update_user(user_id, user) {
    return http.put('/api/user/users/' + user_id, user);
}
