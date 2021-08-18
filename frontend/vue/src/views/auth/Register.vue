<template>
    <div class="register register-padding">
        <div id="register" class="row justify-content-center mt-5">
            <div class="card  site-polaroid" style="width: 30rem;">
                <div class="card-header text-light bg-info">
                    <h2 align="center"><strong>{{ $t('Register') }}</strong></h2>
                </div>
                <div class="card-body small">
                    <div class="form-group">
                        <h5><span class="badge badge-secondary">{{ $t('App Id') }}</span></h5>
                        <input name="username" id="id_app_id" class="form-control form-control-sm" type="text" v-model="register.app_id" :placeholder="$t('App Id')" required/>
                    </div>
                    <div class="form-group">
                        <h5><span class="badge badge-secondary">{{ $t('User') }}</span></h5>
                        <input name="username" id="id_name" class="form-control form-control-sm" type="text" v-model="register.name" :placeholder="$t('User Name')" required/>
                    </div>
                    <div class="form-group">
                        <h5><span class="badge badge-secondary">{{ $t('Password') }}</span></h5>
                        <div class="text-danger">{{ $t('The password is a combination of 8 or more characters, numbers and letters.') }}</div>
                        <input name="password1" id="id_password1" class="form-control form-control-sm" type="password" v-model="register.password1" :placeholder="$t('Password')" required/>
                    </div>
                    <div class="form-group">
                        <h5><span class="badge badge-secondary">{{ $t('Password') }} {{ $t('Confirm') }}</span></h5>
                        <input name="password2" id="id_password2" class="form-control form-control-sm" type="password" v-model="register.password2" :placeholder="$t('Password') + $t('Confirm')" required/>
                    </div>
                    <div class="form-group">
                        <h5><span class="badge badge-secondary">{{ $t('Email') }}</span></h5>
                        <div class="text-danger">{{ $t('Please enter the correct email.') }}</div>
                        <div class="text-danger">{{ $t('If it is a invalid email, we will not be able to process your email verification.') }}</div>
                        <div class="text-danger">{{ $t('You need the registration process again.') }}</div>
                        <input name="email" id="id_email" class="form-control form-control-sm" type="email" v-model="register.email" :placeholder="$t('Email')" required/>
                    </div>
                    <div>
                        <button type="submit" class="btn btn-sm btn-outline-info" :title="$t('Register')">{{ $t('Register') }}</button>
                        <button type="button" class="btn btn-sm btn-outline-info  mx-1" @click="$router.push('/login')" :title="$t('Login')">{{ $t('Login') }}</button>
                        <button type="button" class="btn btn-sm btn-outline-info" @click="$router.go(-1)" :title="$t('Cancel')">{{ $t('Cancel') }}</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Register',
    data() {
        return {
            register: {
                id: '',
                app_id: '',
                password1: '',
                password2: '',
                email: ''
            }
        };
    },
    methods: {}
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
