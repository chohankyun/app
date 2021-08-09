import Vue from 'vue';
import store from '../store';
import VueRouter from 'vue-router';
import Home from './home';
import Board from './board';
import Login from './login';
import Post from './post';
import Search from './search';

Vue.use(VueRouter);

const routes = [
    ...Home,
    ...Board,
    ...Login,
    ...Post,
    ...Search
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
