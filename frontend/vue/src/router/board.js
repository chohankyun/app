import Board from '@/views/Board';
import Post from "@/views/Post";

export default [
    {
        path: '/board/home',
        redirect: '/'
    },
    {
        path: '/board/:category_id',
        component: Board,
        meta: {title: 'Board'}
    },
    {
        path: '/post',
        children: [
            {
                path: ':id'
            }
        ],
        component: Post,
        meta: {title: 'Post'}
    }
];

