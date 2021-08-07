<template>
    <div class="container">
        <div class="search search-padding">
            <div class="row">
                <div class="col-lg-8 col-sm-7 py-4">
                    <span class="text-light bg-dark" style="padding: 3px 5px;">
                        <i class="fa fa-list-ol" aria-hidden="true"></i></span> <strong>{{ $t('Total results') }} : {{ search.total }} </strong>
                </div>
                <Order @changeOrder="change_order"/>
            </div>
            <div class="row">
                <div class="col small">
                    <div class="card mb-2" v-for="post in search.results" :key="post.id">
                        <div class="card-body">
                            <p class="card-text text-truncate font-weight-bold">
                                <a style="color: #5bc0de">
                                    <i class="fa fa-external-link" aria-hidden="true"></i> {{ post.subject }}</a>
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
                                        <i class="fa fa-folder-open" aria-hidden="true"></i> {{ post.category_name }}
                                        <i class="fa fa-user" aria-hidden="true"></i> {{ post.user_name }}
                                        <i class="fa fa-thumbs-up" aria-hidden="true"> </i> {{ post.recommend_count }}
                                        <i class="fa fa-comment-dots" aria-hidden="true"></i> {{ post.reply_count }}
                                        <i class="fa fa-envelope-open" aria-hidden="true"></i> {{ post.click_count }}
                                        <i class="fa fa-calendar" aria-hidden="true"> </i> {{ post.local_datetime }}
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

import Order from "@/components/Order";
import * as board_api from "@/api/board";

export default {
    name: 'Search',
    components: {Order},
    data() {
        return {
            order: 'updated_datetime',
            search: null
        }
    },
    created() {
        board_api.search_post(this.$route.params.search_word, this.order).then(res => {
            this.search = res.data;
            console.log(this.search);
        });
    },
    methods: {
        change_order(order) {
            board_api.search_post(this.$route.params.search_word, order).then(res => {
                this.posts = res.data.results;
            });
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
