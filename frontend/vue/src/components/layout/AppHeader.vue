<template>
    <div class="app-header">
        <nav class="navbar navbar-expand-lg navbar-light bg-light fixed-top site-top-border">
            <div class="container">
                <a class="navbar-brand col-lg-3 col-md-4 col-sm-6 col" href="#/"> <img src="../../assets/logo.png" class="img-fluid" alt="logo image" :title="$t('chohankyun.com')" /> </a>
                <div class="d-none d-md-block col">
                    <form class="input-group  pull-left">
                        <input type="text" class="form-control form-control-sm" :placeholder="$t('Please enter your search term.')" />
                        <div class="input-group-append">
                            <button class="btn btn-info btn-sm" type="submit" :title="$t('Search')">
                                <i class="fa fa-search" aria-hidden="true"></i>
                            </button>
                        </div>
                    </form>
                </div>
                <ul class="nav">
                    <li class="nav-item ml-1">
                        <button type="button" class="btn btn-sm btn-block btn-outline-info" :title="$t('Login')" @click="$router.push('Login')">{{ $t('Login') }}</button>
                    </li>
                    <li class="nav-item ml-1">
                        <button type="button" class="btn btn-sm btn-block btn-outline-info" :title="$t('Register')">{{ $t('Register') }}</button>
                    </li>
                    <li class="nav-item ml-1">
                        <div id="lang" class="dropdown show">
                            <a class="btn btn-sm btn-block btn-outline-info dropdown-toggle" href="#" role="button" id="dropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" :title="$t('Change Language')">
                                {{ lang }}
                            </a>
                            <div class="dropdown-menu" aria-labelledby="dropdownMenuLink">
                                <a class="dropdown-item" href="#" v-on:click="change_lang(value, key)" v-for="(value, key) in options" :key="key">{{ value }}</a>
                            </div>
                        </div>
                    </li>
                </ul>
            </div>
        </nav>
    </div>
</template>

<script>
export default {
    name: 'AppHeader',
    data() {
        return {
            lang: '한국어',
            options: { ko: '한국어', en: 'English' }
        };
    },
    created() {
        let locale = navigator.language || navigator.userLanguage;
        locale = locale.substring(0, 2);
        if (locale !== 'ko') locale = 'en'; // 한국어가 아닌 경우 무조건 영어로 설정
        this.$i18n.locale = locale;
        this.lang = this.options[locale];
    },
    methods: {
        change_lang(value, key) {
            this.$i18n.locale = key;
            this.lang = value;
        }
    }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.site-top-border {
    border-top: 3px solid #5bc0de;
    border-bottom: 1px solid rgba(0, 0, 0, 0.125);
}
</style>
