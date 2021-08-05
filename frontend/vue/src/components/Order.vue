<template>
    <div class="col-lg-4 col-sm-5 d-none d-md-block">
        <ul class="nav float-right">
            <li class="nav-item py-3 pl-1" v-for="order in orders" :key=order.id>
                <button type="button" class="btn btn-sm btn-block btn-outline-secondary" :class="{active: order_id === order.id }" @click="change(order.id)" :title="$t(order.name)">{{ $t(order.name) }}</button>
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    name: 'Order',
    data() {
        return {
            order_id: 'updated_datetime',
            orders: [
                {'id': 'updated_datetime', 'name': 'New'},
                {'id': 'recommend_count', 'name': 'Recommend'},
                {'id': 'reply_count', 'name': 'Reply'},
                {'id': 'click_count', 'name': 'Lookup'}
            ]
        };
    },
    methods: {
        change(order_id) {
            this.order_id = order_id;
            this.$emit('changeOrder', order_id);
        }
    }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
