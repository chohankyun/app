import Home from '../views/Home.vue';
import Login from "@/views/Login";
import Search from "@/views/Search";

export default [
    {
        path: '/',
        component: Home,
        meta: {title: 'chohankyun.com'}
    },
    {
        path: '/search/:search_word',
        name: 'Search',
        component: Search,
        meta: {title: 'Search'}
    },
    {
        path: '/login',
        name: 'Login',
        component: Login,
        meta: {title: 'Login'}
    }
];

