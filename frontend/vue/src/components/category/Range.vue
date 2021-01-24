<template>
    <div class="row">
        <div class="col-lg-8 col-sm-7">
            <ul class="nav float-left">
                <li class="nav-item py-3 pr-1" v-for="range in range_list" :key="range.key">
                    <button type="button" class="btn btn-sm btn-block btn-outline-info" @click="select_range(range.key)" :class="{ active: range_key === range.key }">{{ $t(range.name) }}</button>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Range',
    data() {
        return {
            range_key: 'home',
            range_list: this.$store.state.category.range_list
        };
    },
    methods:{
        select_range(range_key){
            this.range_key = range_key;
        }
    }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
