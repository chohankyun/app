<template>
    <div class="app-footer">
        <footer class="py-4 bg-dark text-white small">
            <div class="container">
                <p class="m-0 text-center">
                    <span class="pr-3" :title="$t('chohankyun.com')"><i class="fa fa-copyright" aria-hidden="true"></i> chohankyun.com </span>
                    <span class="pr-3" title=""><i class="far fa-building" aria-hidden="true"></i> {{ $t('Gyesan-dong, Gyeyang-gu, Incheon 000-0') }}</span>
                    <span title=""><i class="fa fa-phone" aria-hidden="true"></i> 000-0000-0000</span>
                </p>
            </div>
        </footer>
    </div>
</template>

<script>
export default {
    name: 'AppFooter'
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
