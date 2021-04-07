<template>
    <div class="row">
        <div class="col-lg-8 col-sm-7">
            <ul class="nav float-left">
                <li class="nav-item py-3 pr-1" v-for="category in category_default" :key="category.code">
                    <button type="button" class="btn btn-sm btn-block btn-outline-info" @click="select_category(category.code)" :class="{ active: category_code === category.code }">{{ $t(category.name) }}</button>
                </li>
                <li class="nav-item py-3 pr-1" v-for="category in category_list" :key="category.code">
                    <button type="button" class="btn btn-sm btn-block btn-outline-info" @click="select_category(category.code)" :class="{ active: category_code === category.code }">{{ $t(category.name) }}</button>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Category',
    data() {
        return {
            category_code: 'home',
            category_default: this.$store.state.board.category_default,
            category_list: this.$store.state.board.category_list
        };
    },
    beforeMount: function() {
        this.$store.dispatch('board/get_category_list');
    },
    methods: {
        select_category(category_code) {
            this.category_code = category_code;
        }
    }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
