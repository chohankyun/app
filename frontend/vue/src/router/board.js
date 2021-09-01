import Board from '@/views/board/Board';
import Post from '@/views/board/Post';

export default [
    {
        path: '/board/home',
        redirect: '/'
    },
    {
        path: '/board/:category_id',
        component: Board,
        meta: { title: 'Board' }
    },
    {
        path: '/post',
        children: [
            {
                path: ':id',
                meta: { title: 'Post' }
            }
        ],
        component: Post,
        meta: { title: 'Post' }
    }
];
