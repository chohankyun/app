import Home from '@/views/home/Home';
import Search from '@/views/home/Search';
import Login from '@/views/join/Login';
import Register from '@/views/join/Register';
import Password from '@/views/join/Password';

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
    },
    {
        path: '/Password',
        component: Password,
        meta: { title: 'Password' }
    }
];
