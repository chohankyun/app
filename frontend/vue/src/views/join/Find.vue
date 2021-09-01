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
                        <button type="submit" class="btn btn-sm btn-outline-info" :title="$t(types[type]) + $t('Send email')">{{ $t(types[type]) }} {{ $t('Send email') }}</button>
                        <button type="button" class="btn btn-sm btn-outline-info mx-1" @click="$router.push('/login')" :title="$t('Login')">{{ $t('Login') }}</button>
                        <button type="button" class="btn btn-sm btn-outline-info" @click="$router.go(-1)" :title="$t('Cancel')">{{ $t('Cancel') }}</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import * as join_api from '@/api/join';

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
            try {
                let response = null;
                if (this.type === 'App Id') {
                    response = await join_api.find_app_id(this.email);
                }
                if (this.type === 'Password') {
                    response = await join_api.reset_password(this.email);
                }
                alert(response.data);
                await this.$router.push('/');
            } catch (e) {
                alert(e.message);
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
