import Post from '@/views/Post';

export default [
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

