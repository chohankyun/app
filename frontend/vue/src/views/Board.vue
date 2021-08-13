<template>
    <div class="container">
        <div class="board board-padding">
            <div class="row">
                <Category />
                <Order @change="change_order" />
            </div>
            <div class="row">
                <div class="col-lg-3 col-md-6 col-sm-6 portfolio-item small" v-for="post in posts" :key="post.id">
                    <div class="card h-100 site-polaroid">
                        <router-link :to="{ path: '/post/' + post.id }"><img class="card-img-top site-thumbnail" :src="post.first_image_source ? post.first_image_source : 'http://via.placeholder.com/250x150?text=Text Only'"/></router-link>
                        <div class="card-body text-center px-1 py-3">
                            <p class="card-text text-truncate font-weight-bold">
                                <router-link :to="{ path: '/post/' + post.id }" style="color: #5bc0de">{{ post.subject }}</router-link>
                            </p>
                        </div>
                        <ul class="list-group list-group-flush">
                            <li class="list-group-item text-white bg-secondary text-center px-1 py-2">
                                <div class="cart-text">
                                    <div>
                                        <i class="fa fa-folder-open" aria-hidden="true"></i> {{ $t(post.category_name) }} <i class="fa fa-user" aria-hidden="true"></i> {{ post.user_name }} <i class="fa fa-thumbs-up" aria-hidden="true"> </i> {{ post.recommend_count }}
                                        <i class="fa fa-comment-dots" aria-hidden="true"></i> {{ post.reply_count }} <i class="fa fa-envelope-open" aria-hidden="true"></i> {{ post.click_count }}
                                    </div>
                                    <div><i class="fa fa-calendar" aria-hidden="true"> </i> {{ post.local_datetime }}</div>
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
import Category from '@/components/Category';
import Order from '@/components/Order';
import * as board_api from '@/api/board';

export default {
    name: 'Board',
    components: {
        Category,
        Order
    },
    data() {
        return {
            category_id: 'all',
            order: 'updated_datetime',
            posts: []
        };
    },
    created() {
        this.category_id = this.$route.params.category_id;
        board_api
            .get_posts_by_category_order(this.category_id, this.order)
            .then(res => {
                this.posts = res.data.results;
            })
            .catch(e => {
                this.posts = null;
                alert(e.message);
            });
    },
    methods: {
        async change_order(order) {
            try {
                const response = await board_api.get_posts_by_category_order(this.category_id, order);
                this.posts = response.data.results;
            } catch (e) {
                this.posts = null;
                alert(e.message);
            }
        }
    }
};
</script>

<style scoped>
.board-padding {
    padding-top: 55px;
    margin-bottom: 30px;
}

.portfolio-item {
    margin-bottom: 30px;
}

.pagination {
    margin-bottom: 30px;
}
</style>
