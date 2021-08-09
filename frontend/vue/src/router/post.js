import Post from '@/views/Post';

export default [
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

