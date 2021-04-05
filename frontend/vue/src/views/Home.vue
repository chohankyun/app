<template>
    <div class="home home-padding">
        <div class="container">
            <div id="id_carousel_indicators" class="mt-3 carousel slide site-polaroid d-none d-md-block" data-ride="carousel" data-interval="5000">
                <ol class="carousel-indicators">
                    <li data-target="#id_carousel_indicators" data-slide-to="0" class="active"></li>
                    <li data-target="#id_carousel_indicators" data-slide-to="1"></li>
                    <li data-target="#id_carousel_indicators" data-slide-to="2"></li>
                </ol>
                <div class="carousel-inner">
                    <div class="carousel-item active">
                        <img class="d-block w-100" :src="`${publicPath}/data/carousel/carousel_1.png`" />
                    </div>
                    <div class="carousel-item">
                        <img class="d-block w-100" :src="`${publicPath}/data/carousel/carousel_2.png`" />
                    </div>
                    <div class="carousel-item">
                        <img class="d-block w-100" :src="`${publicPath}/data/carousel/carousel_3.png`" />
                    </div>
                </div>
                <div class="carousel-control-prev" href="#id_carousel_indicators" role="button" data-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="sr-only">Previous</span>
                </div>
                <div class="carousel-control-next" href="#id_carousel_indicators" role="button" data-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="sr-only">Next</span>
                </div>
            </div>
            <Category />
            <div class="row">
                <div class="col m-2">
                    <span class="text-light bg-dark" style="padding: 3px 5px;"> <i class="fa fa-calendar-alt" aria-hidden="true"> </i></span>
                    <strong> {{ $t('New') }}</strong>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
// @ is an alias to /src
import Category from '@/components/Category';

export default {
    name: 'Home',
    components: {
        Category
    },
    data() {
        return {
            publicPath: process.env.BASE_URL
        };
    }
};
</script>
<style scoped>
.home-padding {
    padding-top: 55px;
    margin-bottom: 30px;
}
</style>
