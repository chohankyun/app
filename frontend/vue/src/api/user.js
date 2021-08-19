import http from './http';

export async function login(app_id, password) {
    return http.post('/api/user/login/', {
        app_id,
        password
    });
}

export async function is_auth() {
    return http.get('/api/user/is_auth/');
}

export async function logout() {
    return http.get('/api/user/logout/');
}

export async function create_register(register) {
    return http.post('/api/user/register/', register);
}
