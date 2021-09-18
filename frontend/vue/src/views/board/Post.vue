<template>
    <div class="row background">
        <div class="container post-padding">
            <div class="card mt-3">
                <div class="card-body">
                    <div class="row">
                        <div class="col-lg-4 col-md-6 col-12">
                            <div class="container">
                                <div class="row">
                                    <h5 class="w-25 text-left">
                                        <span class="align-middle badge-secondary">{{ $t('Date') }}</span>
                                    </h5>
                                    <div class="col-9">
                                        <input type="text" id="id_local_datetime" name="local_datetime" class="form-control form-control-sm" :disabled="true" :value="post.updated_datetime | local_time"/>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-4 col-md-6 col-12">
                            <div class="container">
                                <div class="row">
                                    <h5 class="w-25 text-left">
                                        <span class="align-middle badge-secondary">{{ $t('User') }}</span>
                                    </h5>
                                    <div class="col-xl-9 col-lg-8 col-md-9 col-9">
                                        <input type="text" id="id_user_name" name="user_name" class="form-control form-control-sm" :disabled="true" v-model="post.user_name" required/>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-4 col-md-6 col-12">
                            <div class="container">
                                <div class="row">
                                    <h5 class="w-25 text-left">
                                        <span class="align-middle badge-secondary">{{ $t('Category') }}</span>
                                    </h5>
                                    <div class="col-9">
                                        <select name="category" id="id_category" class="form-control form-control-sm" :disabled="post_disabled()" v-model="post.category" required>
                                            <option value="">--- {{ $t('Please choose') }} ---</option>
                                            <option v-bind:value="category.id" v-for="category in category_list" :key="category.id">
                                                {{ $t(category.name) }}
                                            </option>
                                        </select>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-lg-4 col-md-6 col-12">
                            <div class="container">
                                <div class="row">
                                    <h5 class="w-25 text-left">
                                        <span class="align-middle badge-secondary">{{ $t('Subject') }}</span>
                                    </h5>
                                    <div class="col-9">
                                        <input type="text" id="id_subject" name="subject" class="form-control form-control-sm" :disabled="post_disabled()" v-model="post.subject" :placeholder="$t('Please enter a subject. (300 characters or less)')" required/>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-4 col-12" v-show="post.id !== ''">
                            <div class="container">
                                <div class="row">
                                    <h5>
                                        <span class="align-middle badge-secondary">{{ $t('Reply') }}</span>
                                        <span class="col-1 mx-2 align-middle badge-info">{{ post.reply_count }}</span>
                                        <span class="align-middle badge-secondary">{{ $t('Lookup') }}</span>
                                        <span class="col-1 mx-2 align-middle badge-info">{{ post.click_count }}</span>
                                    </h5>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-4 col-12" v-show="post.id !== ''">
                            <div class="container">
                                <div class="row">
                                    <h5>
                                        <span class="align-middle badge-secondary">{{ $t('Recommend') }}</span>
                                        <span class="col-1 mx-2 align-middle badge-info">{{ recommend_toggle.recommend_count }}</span>
                                    </h5>
                                    <span v-if="user.id !== undefined">
                                        <toggle-button v-model="recommend_toggle.is_recommend" @change="save_recommend()" :sync="true" :labels="true" color="#17a2b8" :width="70" :height="28" :font-size="20"/>
                                    </span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <Editor api-key="p453mc03irhw5ur9757lryy6q5l0yh1kkn8451225emn3v7n" :init="post_init" :disabled="post_disabled()" v-model="post.content"/>
            <div class="card">
                <div class="row justify-content-between mx-0 mb-3">
                    <div class="mt-3 col-3 col-sm-2 float-left">
                        <button type="submit" class="btn btn-sm btn-outline-info btn-block" @click="$router.go(-1)" :title="$t('Cancel')">{{ $t('Cancel') }}</button>
                    </div>
                    <div class="mt-3 col-3 col-sm-2 float-right">
                        <button type="submit" class="btn btn-sm btn-outline-info btn-block" v-if="!post_disabled()" @click="save_post" :title="$t('Save')">{{ $t('Save') }}</button>
                    </div>
                </div>
            </div>
            <div v-for="reply in replies" :key="reply.id">
                <div class="card mt-2">
                    <div class="white-box text-info" style="font-size: small;">
                        <label class="ml-2 my-1"><i class="fa fa-comment-dots" aria-hidden="true"></i>&nbsp;{{ $t('Reply') }}</label>
                        <label class="ml-2">&nbsp;<i class="fa fa-user" aria-hidden="true"></i>&nbsp;{{ reply.user_name }}</label>
                        <label class="ml-2">&nbsp;<i class="fa fa-calendar" aria-hidden="true"></i>&nbsp;{{ reply.updated_datetime | local_time  }}</label>
                    </div>
                </div>
                <Editor api-key="p453mc03irhw5ur9757lryy6q5l0yh1kkn8451225emn3v7n" :init="replies_init" :disabled="replied_disabled(reply.user)" v-model="reply.content"/>
                <div class="card">
                    <div class="row justify-content-between mx-0 mb-3">
                        <div class="mt-3 col-3 col-sm-2 float-left">
                            <button type="submit" class="btn btn-sm btn-outline-info btn-block" @click="$router.go(-1)" :title="$t('Cancel')">{{ $t('Cancel') }}</button>
                        </div>
                        <div class="mt-3 col-3 col-sm-2 float-right">
                            <button type="submit" class="btn btn-sm btn-outline-info btn-block" v-if="!replied_disabled(reply.user)" @click="save_reply" :title="$t('Save')">{{ $t('Save') }}</button>
                        </div>
                    </div>
                </div>
            </div>
            <div v-if="!reply_disabled()">
                <div class="card mt-2">
                    <div class="white-box text-info" style="font-size: small;">
                        <label class="ml-2 my-1"><i class="fa fa-comment-dots" aria-hidden="true"></i>&nbsp;{{ $t('Reply') }}</label>
                        <label class="ml-2">&nbsp;<i class="fa fa-user" aria-hidden="true"></i>&nbsp;{{ reply.user_name }}</label>
                        <label class="ml-2">&nbsp;<i class="fa fa-calendar" aria-hidden="true"></i>&nbsp;{{ reply.updated_datetime | local_time  }}</label>
                    </div>
                </div>
                <Editor api-key="p453mc03irhw5ur9757lryy6q5l0yh1kkn8451225emn3v7n" :init="reply_init" v-model="reply.content"/>
                <div class="card">
                    <div class="row justify-content-between mx-0 mb-3">
                        <div class="mt-3 col-3 col-sm-2 float-left">
                            <button type="submit" class="btn btn-sm btn-outline-info btn-block" @click="$router.go(-1)" :title="$t('Cancel')">{{ $t('Cancel') }}</button>
                        </div>
                        <div class="mt-3 col-3 col-sm-2 float-right">
                            <button type="submit" class="btn btn-sm btn-outline-info btn-block" @click="save_reply" :title="$t('Save')">{{ $t('Save') }}</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Vue from 'vue';
import ToggleButton from 'vue-js-toggle-button';
import dayjs from 'dayjs';
import Editor from '@tinymce/tinymce-vue';
import * as board_api from '@/api/board';

Vue.use(ToggleButton);

export default {
    name: 'Post',
    components: {
        Editor
    },
    data() {
        return {
            category_list: this.$store.state.board.category_list,
            post_init: {
                language: this.$store.state.lang.locale,
                min_height: 500,
                menubar: true,
                autoresize_bottom_margin: 10,
                plugins: ['advlist autolink lists link image charmap print preview anchor', 'searchreplace visualblocks code fullscreen', 'insertdatetime media table paste code help wordcount', 'autoresize'],
                toolbar: 'undo redo | formatselect | bold italic backcolor | \
                    alignleft aligncenter alignright alignjustify | \
                    bullist numlist outdent indent | removeformat | help'
            },
            reply_init: {
                language: this.$store.state.lang.locale,
                min_height: 150,
                menubar: false,
                autoresize_bottom_margin: 10,
                plugins: ['advlist autolink lists link image charmap print preview anchor', 'searchreplace visualblocks code fullscreen', 'insertdatetime media table paste code help wordcount', 'autoresize'],
                toolbar: 'undo redo | formatselect | bold italic backcolor | \
                    alignleft aligncenter alignright alignjustify | \
                    bullist numlist outdent indent | removeformat | link image media | help'
            },
            replies_init: {
                language: this.$store.state.lang.locale,
                menubar: false,
                autoresize_bottom_margin: 10,
                plugins: ['advlist autolink lists link image charmap print preview anchor', 'searchreplace visualblocks code fullscreen', 'insertdatetime media table paste code help wordcount', 'autoresize'],
                toolbar: 'undo redo | formatselect | bold italic backcolor | \
                    alignleft aligncenter alignright alignjustify | \
                    bullist numlist outdent indent | removeformat | link image media | help'
            },
            post: {
                id: '',
                user: this.$store.state.uauth.user.id,
                category: '',
                updated_datetime: dayjs(),
                user_name: this.$store.state.uauth.user.name,
                subject: '',
                reply_count: 0,
                click_count: 0,
                recommend_count: 0,
                content: ''
            },
            reply: {
                id: '',
                post: this.$route.params.id,
                user: this.$store.state.uauth.user.id,
                user_name: this.$store.state.uauth.user.name,
                updated_datetime: dayjs(),
                content: ''
            },
            replies: [],
            recommend: {
                id: '',
                user: this.$store.state.uauth.user.id,
                post: this.$route.params.id
            },
            post_disabled: () => {
                return this.post.id !== '' && this.post.user !== this.$store.state.uauth.user.id;
            },
            reply_disabled: () => {
                return this.post.id === '' || this.$store.state.uauth.user.id === undefined;
            },
            replied_disabled: (user_id) => {
                return user_id !== this.$store.state.uauth.user.id;
            },
            recommend_toggle: {
                recommend_count: 0,
                is_recommend: false
            }
        };
    },
    computed: {
        user: function () {
            return this.$store.state.uauth.user;
        }
    },
    created() {
        if (this.$route.params.id !== undefined) {
            board_api.get_post(this.$route.params.id)
                .then(response => {
                    this.post = response.data;
                })
                .catch(error => {
                    this.$server_error(error);
                    this.$router.push('/').catch(() => {
                    });
                });
            board_api.get_replies(this.$route.params.id)
                .then(response => {
                    this.replies = response.data;
                })
                .catch(error => {
                    this.$server_error(error);
                    this.$router.push('/').catch(() => {
                    });
                });
            board_api.get_recommend_toggle(this.$route.params.id)
                .then(response => {
                    this.recommend_toggle = response.data;
                })
                .catch(error => {
                    this.$server_error(error);
                    this.$router.push('/').catch(() => {
                    });
                });
        }
    },
    methods: {
        async save_post() {
            try {
                await board_api.create_post(this.post);
                this.$router.go(0);
            } catch (error) {
                this.$server_error(error);
            }
        },
        async save_reply() {
            try {
                await board_api.create_reply(this.reply);
                this.$router.go(0);
            } catch (error) {
                this.$server_error(error);
            }
        },
        async save_recommend() {
            if (this.recommend_toggle.is_recommend === true) {
                try {
                    await board_api.create_recommend(this.recommend);
                    const response = await board_api.get_recommend_toggle(this.$route.params.id);
                    this.recommend_toggle = response.data;
                } catch (error) {
                    this.$server_error(error);
                }
            } else {
                try {
                    await board_api.delete_recommend(this.$route.params.id);
                    const response = await board_api.get_recommend_toggle(this.$route.params.id);
                    this.recommend_toggle = response.data;
                } catch (error) {
                    this.$server_error(error);
                }
            }
        }
    }
};
</script>

<style scoped>
.background {
    background-color: #eee;
}

.post-padding {
    padding-top: 55px;
    margin-bottom: 30px;
}
</style>
