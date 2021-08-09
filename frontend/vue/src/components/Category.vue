<template>
    <div class="col-lg-8 col-sm-7">
        <ul class="nav float-left">
            <li class="nav-item py-3 pr-1" v-for="category in category_default" :key="category.id">
                <button type="button" class="btn btn-sm btn-block btn-outline-info" @click="select_category(category.id)" :class="{ active: category_id === category.id }">{{ $t(category.name) }}</button>
            </li>
            <li class="nav-item py-3 pr-1" v-for="category in category_list" :key="category.id">
                <button type="button" class="btn btn-sm btn-block btn-outline-info" @click="select_category(category.id)" :class="{ active: category_id === category.id }">{{ $t(category.name) }}</button>
            </li>
        </ul>
    </div>
</template>

<script>
import router from '@/router';

export default {
    name: 'Category',
    data() {
        return {
            category_id: this.$store.state.board.category_id,
            category_default: this.$store.state.board.category_default,
            category_list: this.$store.state.board.category_list
        };
    },
    beforeMount: function() {
        this.$store.dispatch('board/set_categories');
    },
    methods: {
        select_category(category_id) {
            this.$store.commit('board/setCategoryId', category_id);
            router.push({ name: 'Board', params: { category_id: category_id } });
        }
    }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
