<template>
    <div class="home home-padding">
        <div class="container">
            <div id="id_carousel_indicators" class="mt-3 carousel slide site-polaroid d-none d-md-block" data-ride="carousel" data-interval="5000">
                <ol class="carousel-indicators">
                    <li data-target="#id_carousel_indicators" data-slide-to="0" class="active"></li>
                    <li data-target="#id_carousel_indicators" data-slide-to="1"></li>
                    <li data-target="#id_carousel_indicators" data-slide-to="2"></li>
                </ol>
                <div class="carousel-inner">
                    <div class="carousel-item active">
                        <img class="d-block w-100" :src="`${publicPath}/data/carousel/carousel_1.png`"/>
                    </div>
                    <div class="carousel-item">
                        <img class="d-block w-100" :src="`${publicPath}/data/carousel/carousel_2.png`"/>
                    </div>
                    <div class="carousel-item">
                        <img class="d-block w-100" :src="`${publicPath}/data/carousel/carousel_3.png`"/>
                    </div>
                </div>
                <div class="carousel-control-prev" href="#id_carousel_indicators" role="button" data-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="sr-only">Previous</span>
                </div>
                <div class="carousel-control-next" href="#id_carousel_indicators" role="button" data-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="sr-only">Next</span>
                </div>
            </div>
            <div class="row">
                <Category/>
            </div>
            <div class="row">
                <div class="col m-2">
                    <span class="text-light bg-dark" style="padding: 3px 5px;"> <i class="fa fa-calendar-alt" aria-hidden="true"> </i></span>
                    <strong> {{ $t('New') }}</strong>
                </div>
            </div>
            <div class="row">
                <div class="mb-4 col-lg-3 col-md-6 col-sm-6 portfolio-item small" v-for="post in posts.updated_datetime" :key="post.id">
                    <div class="card h-100 site-polaroid">
                        <router-link :to="{name: 'Post', params:{id: post.id}}"><img class="card-img-top site-thumbnail" :src="post.first_image_source ? post.first_image_source : 'http://via.placeholder.com/250x150?text=Text Only'"></router-link>
                        <div class="card-body text-center px-1 py-3">
                            <p class="card-text text-truncate font-weight-bold">
                                <router-link :to="{name: 'Post', params:{id: post.id}}" style="color: #5bc0de">{{ post.subject }}</router-link>
                            </p>
                        </div>
                        <ul class="list-group list-group-flush">
                            <li class="list-group-item text-white bg-secondary text-center px-1 py-2">
                                <div class="cart-text">
                                    <div>
                                        <i class="fa fa-folder-open" aria-hidden="true"></i> {{ $t(post.category_name) }}
                                        <i class="fa fa-user" aria-hidden="true"></i> {{ post.username }}
                                        <i class="fa fa-thumbs-up" aria-hidden="true"> </i> {{ post.recommend_count }}
                                        <i class="fa fa-comment-dots" aria-hidden="true"></i> {{ post.reply_count }}
                                        <i class="fa fa-envelope-open" aria-hidden="true"></i> {{ post.click_count }}
                                    </div>
                                    <div>
                                        <i class="fa fa-calendar" aria-hidden="true"> </i> {{ post.local_datetime }}
                                    </div>
                                </div>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col m-2">
                    <span class="text-light bg-dark" style="padding: 2px 6px;"><i class="fa fa-thumbs-up" aria-hidden="true"> </i></span>
                    <strong>{{ $t('Recommend') }}</strong>
                </div>
            </div>
            <div class="row">
                <div class="mb-4 col-lg-3 col-md-6 col-sm-6 portfolio-item small" v-for="post in posts.recommend_count" :key="post.id">
                    <div class="card h-100 site-polaroid">
                        <router-link :to="{name: 'Post', params:{id: post.id}}"><img class="card-img-top site-thumbnail" :src="post.first_image_source ? post.first_image_source : 'http://via.placeholder.com/250x150?text=Text Only'"></router-link>
                        <div class="card-body text-center px-1 py-3">
                            <p class="card-text text-truncate font-weight-bold">
                                <router-link :to="{name: 'Post', params:{id: post.id}}" style="color: #5bc0de">{{ post.subject }}</router-link>
                            </p>
                        </div>
                        <ul class="list-group list-group-flush">
                            <li class="list-group-item text-white bg-secondary text-center px-1 py-2">
                                <div class="cart-text">
                                    <div>
                                        <i class="fa fa-folder-open" aria-hidden="true"></i> {{ $t(post.category_name) }}
                                        <i class="fa fa-user" aria-hidden="true"></i> {{ post.username }}
                                        <i class="fa fa-thumbs-up" aria-hidden="true"> </i> {{ post.recommend_count }}
                                        <i class="fa fa-comment-dots" aria-hidden="true"></i> {{ post.reply_count }}
                                        <i class="fa fa-envelope-open" aria-hidden="true"></i> {{ post.click_count }}
                                    </div>
                                    <div>
                                        <i class="fa fa-calendar" aria-hidden="true"> </i> {{ post.local_datetime }}
                                    </div>
                                </div>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col m-2">
                    <span class="text-light bg-dark" style="padding: 3px 5px;"> <i class="fa fa-comment-dots" aria-hidden="true"></i></span>
                    <strong>{{ $t('Reply') }}</strong>
                </div>
            </div>
            <div class="row">
                <div class="mb-4 col-lg-3 col-md-6 col-sm-6 portfolio-item small" v-for="post in posts.reply_count" :key="post.id">
                    <div class="card h-100 site-polaroid">
                        <router-link :to="{name: 'Post', params:{id: post.id}}"><img class="card-img-top site-thumbnail" :src="post.first_image_source ? post.first_image_source : 'http://via.placeholder.com/250x150?text=Text Only'"></router-link>
                        <div class="card-body text-center px-1 py-3">
                            <p class="card-text text-truncate font-weight-bold">
                                <router-link :to="{name: 'Post', params:{id: post.id}}" style="color: #5bc0de">{{ post.subject }}</router-link>
                            </p>
                        </div>
                        <ul class="list-group list-group-flush">
                            <li class="list-group-item text-white bg-secondary text-center px-1 py-2">
                                <div class="cart-text">
                                    <div>
                                        <i class="fa fa-folder-open" aria-hidden="true"></i> {{ $t(post.category_name) }}
                                        <i class="fa fa-user" aria-hidden="true"></i> {{ post.username }}
                                        <i class="fa fa-thumbs-up" aria-hidden="true"> </i> {{ post.recommend_count }}
                                        <i class="fa fa-comment-dots" aria-hidden="true"></i> {{ post.reply_count }}
                                        <i class="fa fa-envelope-open" aria-hidden="true"></i> {{ post.click_count }}
                                    </div>
                                    <div>
                                        <i class="fa fa-calendar" aria-hidden="true"></i> {{ post.local_datetime }}
                                    </div>
                                </div>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col m-2">
                    <span class="text-light bg-dark" style="padding: 3px 5px;"> <i class="fa fa-envelope-open" aria-hidden="true"></i></span>
                    <strong>{{ $t('Lookup') }}</strong>
                </div>
            </div>
            <div class="row">
                <div class="mb-4 col-lg-3 col-md-6 col-sm-6 portfolio-item small" v-for="post in posts.click_count" :key="post.id">
                    <div class="card h-100 site-polaroid">
                        <router-link :to="{name: 'Post', params:{id: post.id}}"><img class="card-img-top site-thumbnail" :src="post.first_image_source ? post.first_image_source : 'http://via.placeholder.com/250x150?text=Text Only'"></router-link>
                        <div class="card-body text-center px-1 py-3">
                            <p class="card-text text-truncate font-weight-bold">
                                <router-link :to="{name: 'Post', params:{id: post.id}}" style="color: #5bc0de">{{ post.subject }}</router-link>
                            </p>
                        </div>
                        <ul class="list-group list-group-flush">
                            <li class="list-group-item text-white bg-secondary text-center px-1 py-2">
                                <div class="cart-text">
                                    <div>
                                        <i class="fa fa-folder-open" aria-hidden="true"></i> {{ $t(post.category_name) }}
                                        <i class="fa fa-user" aria-hidden="true"></i> {{ post.username }}
                                        <i class="fa fa-thumbs-up" aria-hidden="true"> </i> {{ post.recommend_count }}
                                        <i class="fa fa-comment-dots" aria-hidden="true"></i> {{ post.reply_count }}
                                        <i class="fa fa-envelope-open" aria-hidden="true"></i> {{ post.click_count }}
                                    </div>
                                    <div>
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
// @ is an alias to /src
import Category from '@/components/Category';
import * as board_api from '@/api/board';

export default {
    name: 'Home',
    components: {
        Category
    },
    data() {
        return {
            publicPath: process.env.BASE_URL,
            posts: {
                updated_datetime: [],
                click_count: [],
                reply_count: [],
                recommend_count: []
            }
        };
    },
    created() {
        this.$store.commit('board/setCategoryId', 'home');
        Object.keys(this.posts).forEach((value) => {
            board_api
                .get_posts_for_home(value)
                .then(res => {
                    this.posts[value] = res.data;
                })
                .catch(e => {
                    this.posts[value] = [];
                    alert(e.message);
                });
        });
    }
};
</script>
<style scoped>
.home-padding {
    padding-top: 55px;
    margin-bottom: 30px;
}
</style>
