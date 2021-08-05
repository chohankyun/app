import Vue from 'vue';
import store from '../store';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import Board from '../views/Board.vue';
import Login from '../views/Login.vue';
import Post from '../views/Post.vue';

Vue.use(VueRouter);

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
        meta: {title: 'chohankyun.com'}
    },
    {
        path: '/board/:category_id',
        name: 'Board',
        component: Board,
        meta: {title: 'Board'}
    },
    {
        path: '/login',
        name: 'Login',
        component: Login,
        meta: {title: 'Login'}
    },
    {
        path: '/post/:id',
        name: 'Post',
        component: Post,
        meta: {title: 'Post'}
    },
    {
        path: '/post',
        name: 'Post',
        component: Post,
        meta: {title: 'Post'}
    }
];

const router = new VueRouter({
    mode: 'hash',
    base: process.env.BASE_URL,
    routes
});

router.beforeEach((to, from, next) => {
    document.title = to.meta.title;
    store.dispatch('user/is_auth').then(() => next());
});

export default router;
