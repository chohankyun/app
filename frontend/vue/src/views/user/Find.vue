<template>
    <div class="find find-padding">
        <div id="find" class="row justify-content-center mt-5">
            <div class="card  site-polaroid" style="width: 23rem;">
                <div class="card-header text-white bg-info">
                    <h2 align="center"><strong>{{ $t(types[type]) }}</strong></h2>
                </div>
                <div class="card-body small">
                    <div class="form-group">
                        <h5><span class="badge badge-secondary">{{ $t('Email') }}</span></h5>
                        <input name="email" id="id_email" type="text" v-model="email" :placeholder="$t('Email')" class="form-control form-control-sm" required/>
                    </div>
                    <div>
                        <button type="submit" class="btn btn-sm btn-outline-info" @click="find()" :title="$t('Send email')">{{ $t('Send email') }}</button>
                        <button type="button" class="btn btn-sm btn-outline-info mx-1" @click="$router.push('/login')" :title="$t('Login')">{{ $t('Login') }}</button>
                        <button type="button" class="btn btn-sm btn-outline-info" @click="$router.go(-1)" :title="$t('Cancel')">{{ $t('Cancel') }}</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import * as user_api from '@/api/user';

export default {
    name: 'Find',
    data() {
        return {
            email: '',
            types: {
                app_id: 'App Id',
                password: 'Password'
            },
            type: this.$route.params.type
        };
    },
    methods: {
        async find() {
            let response = null;
            try {
                if (this.type === 'app_id') {
                    response = await user_api.find_app_id({ 'email': this.email });
                }
                if (this.type === 'password') {
                    response = await user_api.reset_password({ 'email': this.email });
                }
                this.$server_message(response);
                this.$router.push('/').catch(() => {
                });
            } catch (error) {
                this.$server_error(error);
            }
        }
    }
};
</script>

<style scoped>
.find-padding {
    padding-top: 55px;
    padding-bottom: 50px;
}

.find {
    background-color: #eee;
}
</style>
