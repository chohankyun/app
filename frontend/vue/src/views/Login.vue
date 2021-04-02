<template>
    <div class="login login-padding">
        <div id="login" class="row justify-content-center mt-5">
            <div class="card site-polaroid" style="width: 25rem;">
                <div class="card-header text-white bg-info">
                    <h2 align="center"><strong>{{ $t('Login') }}</strong></h2>
                </div>
                <div class="card-body small">
                    <div class="form-group">
                        <h5><span class="badge badge-secondary">{{ $t('App Id') }}</span></h5>
                        <input name="app_id" id="id_app_id" type="text" v-model="app_id" :placeholder="$t('App Id')" class="form-control form-control-sm" required/>
                    </div>
                    <div class="form-group">
                        <h5><span class="badge badge-secondary">{{ $t('Password') }}</span></h5>
                        <input name="password" id="id_password" type="password" v-model="password" :placeholder="$t('Password')" class="form-control form-control-sm" required/>
                    </div>
                    <div>
                        <button type="button" class="btn btn-sm btn-outline-info" @click="login" :title="$t('Login')">{{ $t('Login') }}</button>
                        <button type="button" class="btn btn-sm btn-outline-info mx-1" :title="$t('Register')">{{ $t('Register') }}</button>
                        <button type="button" class="btn btn-sm btn-outline-info" @click="$router.push('/')" :title="$t('Cancel')">{{ $t('Cancel') }}</button>
                    </div>
                    <div class="mt-4">
                        <a class="mr-1" :title="$t('Go to find app id')">{{ $t('Forgot your app id?') }}</a>
                        <a class="ml-1" :title="$t('Go to find password')">{{ $t('Forgot your password?') }}</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: "Login",
    data() {
        return {
            app_id: '',
            password: ''
        };
    },
    methods: {
        login() {
            this.$store.dispatch('user/login', {
                app_id: this.app_id,
                password: this.password
            }).then(() => window.location.href = '/');
        }
    }
}
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