<template>
    <div class="password password-padding">
        <div id="password" class="row justify-content-center mt-5">
            <div class="card  site-polaroid" style="width: 30rem;">
                <div class="card-header text-light bg-info">
                    <h2 align="center"><strong>{{ $t('Change password') }}</strong></h2>
                </div>
                <div class="card-body small">
                    <div class="form-group">
                        <h5><span class="badge badge-secondary">{{ $t('Old password') }}</span></h5>
                        <input name="password" id="id_password" class="form-control form-control-sm" type="password" v-model="change.old_password" :placeholder="$t('Old password')" required/>
                    </div>
                    <div class="form-group">
                        <h5><span class="badge badge-secondary">{{ $t('New password') }}</span></h5>
                        <div class="text-danger">{{ $t('The password is a combination of 8 or more characters, numbers and letters.') }}</div>
                        <input name="new_password1" id="id_new_password1" class="form-control form-control-sm" type="password" v-model="change.new_password1" :placeholder="$t('New password')" required/>
                    </div>
                    <div class="form-group">
                        <h5><span class="badge badge-secondary">{{ $t('New password') }} {{ $t('Confirm') }}</span></h5>
                        <input name="new_password2" id="id_new_password2" class="form-control form-control-sm" type="password" v-model="change.new_password2" :placeholder="$t('New password') + $t('Confirm')" required/>
                    </div>
                    <div>
                        <button type="submit" class="btn btn-sm btn-outline-info" @click="change_password" :title="$t('Save')">{{ $t('Save') }}</button>
                        <button type="button" class="btn btn-sm btn-outline-info mx-1" @click="$router.go(-1)" :title="$t('Cancel')">{{ $t('Cancel') }}</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import * as user_api from '@/api/user';

export default {
    name: 'Password',
    data() {
        return {
            change: {
                old_password: '',
                new_password1: '',
                new_password2: ''
            }
        };
    },
    methods: {
        async change_password() {
            try {
                const response = await user_api.change_password(this.change);
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
.password-padding {
    padding-top: 55px;
    padding-bottom: 50px;
}

.password {
    background-color: #eee;
}
</style>
