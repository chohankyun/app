import Home from '@/views/home/Home';
import Search from '@/views/home/Search';
import Login from '@/views/uauth/Login';
import Register from '@/views/uauth/Register';
import User from '@/views/uauth/User';
import Password from '@/views/uauth/Password';

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
        path: '/user',
        component: User,
        meta: { title: 'User' }
    },
    {
        path: '/password',
        component: Password,
        meta: { title: 'Password' }
    }
];
