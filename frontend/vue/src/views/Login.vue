<template>
    <div class="login login-padding">
        <div id="login" class="row justify-content-center mt-5">
                <div class="card site-polaroid" style="width: 21rem;">
                <div class="card-header text-white bg-info">
                    <h2 align="center"><strong>{{ $t('Login') }}</strong></h2>
                </div>
                <div class="card-body small">
                    <form role="form" name="loginForm" novalidate>
                        <div class="form-group">
                            <h5><span class="badge badge-secondary">{{ $t('Username') }}</span></h5>
                            <input name="username" id="id_username" type="text" :placeholder="$t('Username')" class="form-control form-control-sm" required/>
                        </div>
                        <div class="form-group">
                            <h5><span class="badge badge-secondary">{{ $t('Password') }}</span></h5>
                            <input name="password" id="id_password" type="password" :placeholder="$t('Password')" class="form-control form-control-sm" required/>
                        </div>
                        <div>
                            <button type="submit" class="btn btn-sm btn-outline-info" :title="$t('Login')">{{ $t('Login') }}</button>
                            <button type="button" class="btn btn-sm btn-outline-info mx-1" :title="$t('Register')">{{ $t('Register') }}</button>
                            <button type="button" class="btn btn-sm btn-outline-info" :title="$t('Cancel')">{{ $t('Cancel') }}</button>
                        </div>
                    </form>
                    <div class="mt-4">
                        <a class="mr-1" :title="$t('Go to find username')">{{ $t('Forgot your username?') }}</a>
                        <a class="ml-1" :title="$t('Go to find password')">{{ $t('Forgot your password?') }}</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: "Login"
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