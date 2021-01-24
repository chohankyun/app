<template>
    <div id="id_carousel_indicators" class="mt-3 carousel slide site-polaroid d-none d-md-block" data-ride="carousel">
        <ol class="carousel-indicators">
            <li data-target="#id_carousel_indicators" data-slide-to="0" class="active"></li>
            <li data-target="#id_carousel_indicators" data-slide-to="1"></li>
            <li data-target="#id_carousel_indicators" data-slide-to="2"></li>
        </ol>
        <div class="carousel-inner">
            <div class="carousel-item active">
                <img class="d-block w-100" src="https://s3.ap-northeast-2.amazonaws.com/chohankyun.com/carousel_1.png" />
            </div>
            <div class="carousel-item">
                <img class="d-block w-100" src="https://s3.ap-northeast-2.amazonaws.com/chohankyun.com/carousel_2.png" />
            </div>
            <div class="carousel-item">
                <img class="d-block w-100" src="https://s3.ap-northeast-2.amazonaws.com/chohankyun.com/carousel_3.png" />
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
</template>

<script>
import $ from 'jquery';

export default {
    name: 'Header',
    props: {
        msg: String
    },
    mounted() {
        $('.carousel').carousel({
            interval: 5000
        });
    }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
    margin: 40px 0 0;
}

ul {
    list-style-type: none;
    padding: 0;
}

li {
    display: inline-block;
    margin: 0 10px;
}

a {
    color: #42b983;
}
</style>
