<template>
    <div class="message message-padding">
        <div id="message" class="row justify-content-center mt-5">
            <div class="col-lg-5 col-md-5">
                <nav>
                    <div class="nav nav-pills nav-fill nav-tabs" id="nav-tab" role="tablist">
                        <a class="nav-link active" id="nav-home-tab" data-toggle="tab" href="#nav-home" role="tab" aria-controls="nav-home" aria-selected="true">Chat List</a>
                        <a class="nav-link" id="nav-profile-tab" data-toggle="tab" href="#nav-profile" role="tab" aria-controls="nav-profile" aria-selected="false">Chat</a>
                    </div>
                </nav>
                <div class="tab-content" id="nav-tabContent">
                    <div class="tab-pane fade show active" id="nav-home" role="tabpanel" aria-labelledby="nav-home-tab">
                        <MemberList/>
                    </div>
                    <div class="tab-pane fade" id="nav-profile" role="tabpanel" aria-labelledby="nav-profile-tab">
                        <Chat/>
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

    },
    methods: {}
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
