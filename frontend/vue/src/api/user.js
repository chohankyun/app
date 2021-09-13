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

export async function create_register(register) {
    return http.post('/api/user/register', register);
}

export async function find_app_id(email) {
    return http.post('/api/user/app-id/find', email);
}

export async function reset_password(email) {
    return http.post('/api/user/password/reset', email);
}

export async function get_user(user_id) {
    return http.get('/api/user/users/' + user_id);
}

