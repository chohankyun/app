<template>
    <div class="login login-padding">
        <div id="login" class="row justify-content-center mt-5">
            <div class="card site-polaroid" style="width: 25rem;">
                <div class="card-header text-white bg-info">
                    <h2 align="center">
                        <strong>{{ $t('Login') }}</strong>
                    </h2>
                </div>
                <div class="card-body small">
                    <div class="form-group">
                        <h5>
                            <span class="badge badge-secondary">{{ $t('User identifier') }}</span>
                        </h5>
                        <input name="uid" id="id_uid" type="text" @keyup.enter="login" v-model="credentials.uid" :placeholder="$t('User identifier')" class="form-control form-control-sm" required/>
                    </div>
                    <div class="form-group">
                        <h5>
                            <span class="badge badge-secondary">{{ $t('Password') }}</span>
                        </h5>
                        <input name="password" id="id_password" type="password" @keyup.enter="login" v-model="credentials.password" :placeholder="$t('Password')" class="form-control form-control-sm"
                               required/>
                    </div>
                    <div>
                        <button type="button" class="btn btn-sm btn-outline-info" @click="login" :title="$t('Login')">{{ $t('Login') }}</button>
                        <button type="button" class="btn btn-sm btn-outline-info mx-1" @click="$router.push('/register')" :title="$t('Register')">{{ $t('Register') }}</button>
                        <button type="button" class="btn btn-sm btn-outline-info" @click="$router.go(-1)" :title="$t('Cancel')">{{ $t('Cancel') }}</button>
                    </div>
                    <div class="mt-4">
                        <router-link :to="{ path: '/find/uid' }" class="mr-1" :title="$t('Go to find user identifier')">{{ $t('Forgot your user identifier?') }}</router-link>
                        <router-link :to="{ path: '/find/password' }" class="mr-1" :title="$t('Go to find password')">{{ $t('Forgot your password?') }}</router-link>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Login',
    data() {
        return {
            credentials: {
                uid: '',
                password: ''
            }
        };
    },
    methods: {
        login() {
            if (Object.values(this.credentials).includes('')) {
                this.$client_error(this.$t('Enter user identifier or password.'));
                return;
            }
            this.$store.dispatch('uauth/login', this.credentials);
        }
    }
};
</script>

<style scoped>
.login-padding {
    padding-top: 55px;
    padding-bottom: 50px;
}

.login {
    background-color: #eee;
}
</style>
