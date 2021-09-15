<template>
    <div class="user user-padding">
        <div id="id_user" class="row justify-content-center mt-5">
            <div class="card  site-polaroid" style="width: 30rem;">
                <div class="card-header text-light bg-info">
                    <h2 align="center"><strong>{{ $t('My info') }}</strong></h2>
                </div>
                <div class="card-body small">
                    <div class="form-group">
                        <h5><span class="badge badge-secondary">{{ $t('App Id') }}</span></h5>
                        <input name="app_id" id="id_app_id" class="form-control form-control-sm" type="text" v-model="user.app_id" :placeholder="$t('App Id')"/>
                    </div>
                    <div class="form-group">
                        <h5><span class="badge badge-secondary">{{ $t('User Name') }}</span></h5>
                        <input name="app_id" id="id_name" class="form-control form-control-sm" type="text" v-model="user.name" :placeholder="$t('User Name')"/>
                    </div>
                    <div class="form-group">
                        <h5><span class="badge badge-secondary">{{ $t('Email') }}</span></h5>
                        <input name="email" id="id_email" class="form-control form-control-sm" type="email" :value="user.email" :placeholder="$t('Email')" disabled/>
                    </div>
                    <div class="form-group">
                        <h5><span class="badge badge-secondary">{{ $t('Last login time') }}</span></h5>
                        <input name="login_time" id="id_login_time" class="form-control form-control-sm" type="text" :value="user.last_login | local_time" :placeholder="$t('Last login time')" disabled/>
                    </div>
                    <div>
                        <button type="button" class="btn btn-sm btn-outline-info" @click="update_user" :title="$t('Update')">{{ $t('Update') }}</button>
                        <button type="button" class="btn btn-sm btn-outline-info mx-1" @click="$router.go(-1)" :title="$t('Cancel')">{{ $t('Cancel') }}</button>
                        <button type="button" class="float-right btn btn-sm btn-outline-danger" :title="$t('Withdrawal')">{{ $t('Withdrawal') }}</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import * as user_api from '@/api/user';

export default {
    name: 'User',
    data() {
        return {
            user: ''
        };

    },
    created() {
        user_api.get_user(this.$store.state.user.user.id)
            .then(response => {
                this.user = response.data;
            })
            .catch(error => {
                this.user = [];
                this.$server_error(error);
            });
    },
    methods: {
        async update_user() {
            try {
                const response = await user_api.update_user(this.$store.state.user.user.id, this.user);
                this.$server_message(response);
                await this.$router.push('/').catch(() => {
                });
            } catch (error) {
                this.$server_error(error);
            }
        }
    }
};
</script>

<style scoped>
.user-padding {
    padding-top: 55px;
    padding-bottom: 50px;
}

.user {
    background-color: #eee;
}
</style>
