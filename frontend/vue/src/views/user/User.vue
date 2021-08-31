<template>
    <div class="user user-padding">
        <div id="id_user" class="row justify-content-center mt-5">
            <div class="card  site-polaroid" style="width: 30rem;">
                <div class="card-header text-light bg-info">
                    <h2 align="center"><strong>{{ $t('My info') }}</strong></h2>
                </div>
                <div class="card-body small">
                    <div class="form-group">
                        <h5><span class="badge badge-secondary">{{ $t('Username') }}</span></h5>
                        <input name="app_id" id="id_app_id" class="form-control form-control-sm" type="text"  :placeholder="$t('App Id')" required/>
                    </div>
                    <div class="form-group">
                        <h5><span class="badge badge-secondary">{{ $('Password') }}</span></h5>
                        <input name="password" id="id_password" class="form-control form-control-sm" type="password" :placeholder="$t('Password')" required/>
                    </div>
                    <div class="form-group">
                        <h5><span class="badge badge-secondary">{{ $t('Email') }}</span></h5>
                        <input name="email" id="id_email" class="form-control form-control-sm" type="email" :placeholder="$t('Email')" disabled/>
                    </div>
                    <div class="form-group">
                        <h5><span class="badge badge-secondary">{{ 'Last login time' | translate }}</span></h5>
                        <input name="login_time" id="id_login_time" class="form-control form-control-sm" type="text" :placeholder="$t('Last login time')" disabled/>
                    </div>
                    <div>
                        <button type="submit" class="btn btn-sm btn-outline-info" :title="$t('Save')">{{ $t('Save') }}</button>
                        <button type="button" class="btn btn-sm btn-outline-info" :title="$t('Update')">{{ $t('Update') }}</button>
                        <button type="button" class="btn btn-sm btn-outline-info" :title="$t('Cancel')">{{ $t('Cancel') }}</button>
                        <button type="button" class="float-right btn btn-sm btn-outline-danger" :title="$t('Withdrawal')">{{ $t('Withdrawal') }}</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'User',
    data() {
    },
    methods: {}
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
