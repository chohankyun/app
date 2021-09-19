<template>
    <div class="user user-padding">
        <div id="id_user" class="row justify-content-center mt-5">
            <div class="card  site-polaroid" style="width: 30rem;">
                <div class="card-header text-light bg-info">
                    <h2 align="center"><strong>{{ $t('My info') }}</strong></h2>
                </div>
                <div class="card-body small">
                    <div class="form-group">
                        <h5><span class="badge badge-secondary">{{ $t('User Identifier') }}</span></h5>
                        <input name="uid" id="id_uid" class="form-control form-control-sm" type="text" v-model="user.uid" @keyup.enter="update_user" :placeholder="$t('User Identifier')"/>
                    </div>
                    <div class="form-group">
                        <h5><span class="badge badge-secondary">{{ $t('User Name') }}</span></h5>
                        <input name="name" id="id_name" class="form-control form-control-sm" type="text" v-model="user.name" @keyup.enter="update_user" :placeholder="$t('User Name')"/>
                    </div>
                    <div class="form-group">
                        <h5><span class="badge badge-secondary">{{ $t('Email') }}</span></h5>
                        <input name="email" id="id_email" class="form-control form-control-sm" type="email" :value="user.email" :placeholder="$t('Email')" disabled/>
                    </div>
                    <div class="form-group">
                        <h5><span class="badge badge-secondary">{{ $t('Last login time') }}</span></h5>
                        <input name="login_time" id="id_login_time" class="form-control form-control-sm" type="text" :value="user.last_login | local_time" :placeholder="$t('Last login time')"
                               disabled/>
                    </div>
                    <div>
                        <button type="button" class="btn btn-sm btn-outline-info" @click="update_user" :title="$t('Update')">{{ $t('Update') }}</button>
                        <button type="button" class="btn btn-sm btn-outline-info mx-1" @click="$router.go(-1)" :title="$t('Cancel')">{{ $t('Cancel') }}</button>
                        <button type="button" class="float-right btn btn-sm btn-outline-danger" @click="delete_user" :title="$t('Withdrawal')">{{ $t('Withdrawal') }}</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import * as uauth_api from '@/api/uauth';

export default {
    name: 'User',
    data() {
        return {
            user: ''
        };

    },
    created() {
        uauth_api.get_user(this.$store.state.uauth.user.id)
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
                const response = await uauth_api.update_user(this.$store.state.uauth.user.id, this.user);
                await this.$client_message('User has been updated.');
                this.$store.commit('uauth/setUserName', response.data.name);
                await this.$router.push('/');
            } catch (error) {
                this.$server_error(error);
            }
        },
        async delete_user() {
            try {
                const result = await this.$client_confirm('Delete', 'Are you sure you want to delete it?');
                if (!result.isConfirmed) {
                    return;
                }
                await uauth_api.delete_user(this.$store.state.uauth.user.id);
                await this.$client_message('User has been deleted.');
                this.$store.commit('uauth/setUser', '');
                await this.$router.push('/');
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
