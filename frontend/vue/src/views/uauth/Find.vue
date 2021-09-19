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
                        <input name="email" id="id_email" type="text" v-model="email" @keyup.enter="send_email" :placeholder="$t('Email')" class="form-control form-control-sm" required/>
                    </div>
                    <div>
                        <button type="submit" class="btn btn-sm btn-outline-info" @click="send_email" :title="$t('Send email')">{{ $t('Send email') }}</button>
                        <button type="button" class="btn btn-sm btn-outline-info mx-1" @click="$router.push('/login')" :title="$t('Login')">{{ $t('Login') }}</button>
                        <button type="button" class="btn btn-sm btn-outline-info" @click="$router.go(-1)" :title="$t('Cancel')">{{ $t('Cancel') }}</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import * as uauth_api from '@/api/uauth';

export default {
    name: 'Find',
    data() {
        return {
            email: '',
            type: this.$route.params.type,
            types: {
                uid: 'User identifier',
                password: 'Password'
            }
        };
    },
    methods: {
        async send_email() {
            let response = null;
            try {
                if (this.email === '') {
                    this.$client_error(this.$t('Please enter your email.'));
                    return;
                }
                if (this.type === 'uid') {
                    response = await uauth_api.find_uid({'email': this.email});
                }
                if (this.type === 'password') {
                    response = await uauth_api.reset_password({'email': this.email});
                }
                await this.$server_message(response);
                await this.$router.push('/');
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
