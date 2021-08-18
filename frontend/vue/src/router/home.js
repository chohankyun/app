import Home from '@/views/Home';
import Login from '@/views/Login';
import Search from '@/views/Search';
import Register from '@/views/auth/Register';

export default [
    {
        path: '/',
        component: Home,
        meta: { title: 'chohankyun.com' }
    },
    {
        path: '/search/:search_word',
        component: Search,
        meta: { title: 'Search' }
    },
    {
        path: '/login',
        component: Login,
        meta: { title: 'Login' }
    },
    {
        path: '/register',
        component: Register,
        meta: { title: 'Register' }
    }
];
