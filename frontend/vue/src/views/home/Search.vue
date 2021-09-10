<template>
    <div class="container">
        <div class="search search-padding">
            <div class="row">
                <div class="col-lg-8 col-sm-7 py-4">
                    <span class="text-light bg-dark" style="padding: 3px 5px;"> <i class="fa fa-list-ol" aria-hidden="true"></i></span> <strong>{{ $t('Total results') }} : {{ search.total }} </strong>
                </div>
                <Order @change="change_order"/>
            </div>
            <div class="row">
                <div class="col small">
                    <div class="card mb-2" v-for="post in search" :key="post.id">
                        <div class="card-body">
                            <p class="card-text text-truncate font-weight-bold">
                                <router-link :to="{ path: '/post/' + post.id }" style="color: #5bc0de"><i class="fas fa-external-link-alt" aria-hidden="true"></i>{{ post.subject }}</router-link>
                            </p>
                        </div>
                        <ul class="list-group list-group-flush">
                            <li class="list-group-item img-fluid">
                                <i class="fa fa-sticky-note" aria-hidden="true"></i>
                                <div v-html="post.content"/>
                            </li>
                            <li class="list-group-item img-fluid" v-show="post.reply_content">
                                <i class="fa fa-comment-dots" aria-hidden="true"></i>
                                <div v-html="post.reply_content"/>
                            </li>
                            <li class="list-group-item  text-light bg-secondary">
                                <div class="cart-text">
                                    <div>
                                        <i class="far fa-sticky-note" aria-hidden="true"></i> {{ post.category_name }} <i class="fa fa-user"></i> {{ post.user_name }} <i class="fa fa-thumbs-up" aria-hidden="true"> </i> {{ post.recommend_count }}
                                        <i class="fa fa-comment-dots" aria-hidden="true"></i> {{ post.reply_count }} <i class="fa fa-envelope-open" aria-hidden="true"></i> {{ post.click_count }} <i class="fa fa-calendar" aria-hidden="true"> </i> {{ post.local_datetime }}
                                    </div>
                                </div>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Order from '@/components/Order';
import * as search_api from '@/api/search';

export default {
    name: 'Search',
    components: { Order },
    data() {
        return {
            order: 'updated_datetime',
            search: ''
        };
    },
    created() {
        search_api.get_posts(this.$route.params.search_word, this.order)
            .then(response => {
                this.search = response.data;
            })
            .catch(error => {
                this.$server_error(error);
            });
    },
    methods: {
        async change_order(order) {
            try {
                const response = await search_api.get_posts(this.$route.params.search_word, order);
                this.search = response.data;
            } catch (error) {
                this.$server_error(error);
            }
        }
    }
};
</script>

<style scoped>
.search-padding {
    padding-top: 55px;
    margin-bottom: 30px;
}
</style>
