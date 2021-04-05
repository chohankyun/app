<template>
    <div id="app">
        <app-header />
        <router-view :key="$route.fullPath" />
        <app-footer />
    </div>
</template>

<script>
import AppHeader from '@/components/layout/AppHeader';
import AppFooter from '@/components/layout/AppFooter';

export default {
    components: {
        AppHeader,
        AppFooter
    }
};
</script>

<style>
.mouse-hand {
    cursor: pointer;
}
.card {
    border-radius: 0rem !important;
}
.card-header {
    border-radius: 0rem !important;
}
.site-polaroid {
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}
</style>
