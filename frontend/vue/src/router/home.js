import Home from '@/views/home/Home';
import Search from '@/views/home/Search';
import Login from '@/views/user/Login';
import Register from '@/views/user/Register';
import User from '@/views/user/User';
import Password from '@/views/user/Password';

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
