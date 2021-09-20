import Vue from 'vue';
import store from '@/store';
import VueRouter from 'vue-router';
import Home from '@/router/home';
import Board from '@/router/board';
import Login from '@/router/login';
import Messenger from '@/router/messenger';

Vue.use(VueRouter);

const routes = [...Home, ...Board, ...Login, ...Messenger];

const router = new VueRouter({
    mode: 'hash',
    base: process.env.BASE_URL,
    routes
});

router.beforeEach((to, from, next) => {
    document.title = to.meta.title;
    store.dispatch('uauth/is_auth').then(() => next());
});

export default router;
