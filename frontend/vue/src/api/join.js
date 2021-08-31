import http from './http';

export async function login(app_id, password) {
    return http.post('/api/join/login/', {
        app_id,
        password
    });
}

export async function is_auth() {
    return http.get('/api/join/is_auth/');
}

export async function logout() {
    return http.get('/api/join/logout/');
}


export async function create_register(register) {
    return http.post('/api/join/register/', register);
}

export async function find_app_id(email) {
    return http.post('/api/join/find/app_id/', email);
}

export async function reset_password(email) {
    return http.post('/api/join/reset/password/', email);
}
