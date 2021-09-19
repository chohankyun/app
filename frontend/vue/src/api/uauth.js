import http from './http';

export async function login(credentials) {
    return http.post('/api/uauth/login', credentials);
}

export async function is_auth() {
    return http.get('/api/uauth/is-auth');
}

export async function logout() {
    return http.get('/api/uauth/logout');
}

export async function register_user(register) {
    return http.post('/api/uauth/register', register);
}

export async function find_uid(email) {
    return http.post('/api/uauth/uid/find', email);
}

export async function reset_password(email) {
    return http.post('/api/uauth/password/reset', email);
}

export async function get_user(user_id) {
    return http.get('/api/uauth/users/' + user_id);
}

export async function change_password(change) {
    return http.post('/api/uauth/password/change', change);
}

export async function update_user(user_id, user) {
    return http.put('/api/uauth/users/' + user_id, user);
}

export async function delete_user(user_id) {
    return http.delete('/api/uauth/users/' + user_id);
}
