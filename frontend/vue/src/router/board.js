import Board from '@/views/Board';

export default [
    {
        path: '/board/home',
        redirect: '/'
    },
    {
        path: '/board/:category_id',
        name: 'Board',
        component: Board,
        meta: { title: 'Board' }
    }
];

