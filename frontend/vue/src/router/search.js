import Search from '@/views/Search';

export default [
    {
        path: '/search/:search_word',
        name: 'Search',
        component: Search,
        meta: {title: 'Search'}
    }
];

