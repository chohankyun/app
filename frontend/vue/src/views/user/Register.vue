<template>
    <div class="register register-padding">
        <div id="register" class="row justify-content-center mt-5">
            <div class="card  site-polaroid" style="width: 30rem;">
                <div class="card-header text-light bg-info">
                    <h2 align="center"><strong>{{ $t('Register') }}</strong></h2>
                </div>
                <div class="card-body small">
                    <div class="form-group">
                        <h5><span class="badge badge-secondary">{{ $t('User identifier') }}</span></h5>
                        <input name="uid" id="id_uid" class="form-control form-control-sm" type="text" @keyup.enter="register" v-model="user.uid" :placeholder="$t('User identifier')" required/>
                    </div>
                    <div class="form-group">
                        <h5><span class="badge badge-secondary">{{ $t('User') }}</span></h5>
                        <input name="name" id="id_name" class="form-control form-control-sm" type="text" @keyup.enter="register" v-model="user.name" :placeholder="$t('User Name')" required/>
                    </div>
                    <div class="form-group">
                        <h5><span class="badge badge-secondary">{{ $t('Password') }}</span></h5>
                        <div class="text-danger">{{ $t('The password is a combination of 8 or more characters, numbers and letters.') }}</div>
                        <input name="password1" id="id_password1" class="form-control form-control-sm" type="password" @keyup.enter="register" v-model="user.password" :placeholder="$t('Password')" required/>
                    </div>
                    <div class="form-group">
                        <h5><span class="badge badge-secondary">{{ $t('Password') }} {{ $t('Confirm') }}</span></h5>
                        <input name="password2" id="id_password2" class="form-control form-control-sm" type="password" @keyup.enter="register" v-model="user.re_password" :placeholder="$t('Password') + $t('Confirm')" required/>
                    </div>
                    <div class="form-group">
                        <h5><span class="badge badge-secondary">{{ $t('Email') }}</span></h5>
                        <div class="text-danger">{{ $t('Please enter the correct email.') }}</div>
                        <div class="text-danger">{{ $t('If it is a invalid email, we will not be able to process your email verification.') }}</div>
                        <div class="text-danger">{{ $t('You need the registration process again.') }}</div>
                        <input name="email" id="id_email" class="form-control form-control-sm" type="email" @keyup.enter="register" v-model="user.email" :placeholder="$t('Email')" required/>
                    </div>
                    <div>
                        <button type="submit" class="btn btn-sm btn-outline-info" @click="register" :title="$t('Register')">{{ $t('Register') }}</button>
                        <button type="button" class="btn btn-sm btn-outline-info  mx-1" @click="$router.push('/login')" :title="$t('Login')">{{ $t('Login') }}</button>
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
    name: 'Register',
    data() {
        return {
            user: {
                uid: '',
                name: '',
                password: '',
                re_password: '',
                email: ''
            }
        };
    },
    methods: {
        async register() {
            if (Object.values(this.user).includes('')) {
                this.$client_error(this.$t('Enter your registration information.'));
                return;
            }
            try {
                const response = await user_api.create_register(this.user);
                this.$server_message(response).then(() => this.$router.push('/'));
            } catch (error) {
                this.$server_error(error);
            }
        }
    }
};
</script>

<style scoped>
.register-padding {
    padding-top: 55px;
    padding-bottom: 50px;
}

.register {
    background-color: #eee;
}
</style>
