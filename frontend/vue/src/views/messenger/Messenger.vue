<template>
    <div class="message message-padding">
        <div id="message" class="row justify-content-center mt-5">
            <div class="col-lg-5 col-md-5">
                <nav>
                    <div class="nav nav-pills nav-fill nav-tabs">
                        <a class="nav-link" v-for="(tab, index) in tabs" :key="tab.id" :class="{ active: curTab === index }" @click="change(index)">{{ tab }}</a>
                    </div>
                </nav>
                <div class="tab-content">
                    <div class="tab-pane fade show" :class="{ active: curTab === 0 }">
                        <MemberList @enter_room="chat_room"/>
                    </div>
                    <div class="tab-pane fade show" :class="{ active: curTab === 1 }">
                        <Chat ref="chat"/>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import MemberList from '@/components/messenger/MemberList';
import Chat from '@/components/messenger/Chat';

export default {
    name: 'Messenger',
    components: {
        MemberList,
        Chat
    },
    data() {
        return {
            curTab: 0,
            tabs: ['member_list', 'chat']
        };
    },
    methods: {
        change(index) {
            console.log(index);
            this.curTab = index;
            if (this.curTab === 0) {
                this.$refs.chat.disconnect();
            }
        },
        chat_room() {
            this.curTab = 1;
            this.$refs.chat.connect();
        }
    }
};
</script>

<style scoped>
.message-padding {
    padding-top: 55px;
    padding-bottom: 50px;
}

.message {
    background-color: #eee;
}
</style>
