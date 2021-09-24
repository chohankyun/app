<template>
    <div class="mesgs">
        <div class="msg_history">
            <div v-for="(message, index) in this.messages" :key="index">
                <div class="incoming_msg" v-if="message.message.id !== $store.state.uauth.user.id">
                    <div class="incoming_msg_img"><img src="https://ptetutorials.com/images/user-profile.png" alt="sunil"></div>
                    <div class="received_msg">
                        <div class="received_withd_msg">
                            <p>{{ message.message.name }}: {{ message.message.message }}</p>
                            <span class="time_date"> 11:01 AM    |    June 9</span></div>
                    </div>
                </div>
                <div class="outgoing_msg" v-if="message.message.id === $store.state.uauth.user.id">
                    <div class="sent_msg">
                        <p>{{ message.message.message }}</p>
                        <span class="time_date"> 11:01 AM    |    June 9</span></div>
                </div>
            </div>
        </div>
        <div class="type_msg">
            <div class="input_msg_write">
                <input type="text" class="write_msg" placeholder="Type a message" @keyup.enter="sendMessage" v-model="message"/>
                <button class="msg_send_btn" type="button" @click="sendMessage"><i class="far fa-paper-plane" aria-hidden="true"></i></button>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Chat',
    data() {
        return {
            address: 'ws://localhost:8000/ws/chat/',
            disabled: true,
            message: '',
            selected: 'json',
            json: {
                key: 'value'
            },
            messages: []
        };
    },
    methods: {
        connect(room) {
            if (this.socket === undefined || this.socket.readyState === 3) {
                this.socket = new WebSocket(this.address + room);
                this.socket.onopen = () => {
                    console.log({type: 'INFO', msg: 'CONNECTED'})
                    this.disabled = false;
                }
                this.socket.onerror = () => {
                    console.log({type: 'ERROR', msg: 'ERROR:'})
                }
                this.socket.onmessage = ({data}) => {
                    console.log({type: 'RECV', msg: 'RECV:' + data})
                    this.messages.push(JSON.parse(data));
                }
                this.socket.onclose = (msg) => {
                    console.log({type: 'ERROR', msg: 'Closed (Code: ' + msg.code + ', Message: ' + msg.reason + ')'})
                }
            }
        },
        sendMessage() {
            if (this.selected === 'plain') {
                console.log({type: 'SENT', msg: 'SENT:' + this.message})
                this.socket.send(this.message)
            } else if (this.selected === 'json') {
                this.json = {id: this.$store.state.uauth.user.id, name: this.$store.state.uauth.user.name, message: this.message}
                console.log({type: 'SENT', msg: 'SENT:' + JSON.stringify(this.json)})
                this.socket.send(JSON.stringify(this.json))
            }
        },
        disconnect() {
            if (this.socket.readyState === 1) {
                this.socket.close()
                console.log({type: 'INFO', msg: 'DISCONNECTED'})
                this.disabled = true
            }
        }
    }
}
;
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
img {
    max-width: 100%;
}

.recent_heading h4 {
    color: #05728f;
    font-size: 21px;
    margin: auto;
}

.srch_bar input {
    border: 1px solid #cdcdcd;
    border-width: 0 0 1px 0;
    width: 80%;
    padding: 2px 0 4px 6px;
    background: none;
}

.srch_bar .input-group-addon button {
    background: rgba(0, 0, 0, 0) none repeat scroll 0 0;
    border: medium none;
    padding: 0;
    color: #707070;
    font-size: 18px;
}

.srch_bar .input-group-addon {
    margin: 0 0 0 -27px;
}

.chat_ib h5 {
    font-size: 15px;
    color: #464646;
    margin: 0 0 8px 0;
}

.chat_ib h5 span {
    font-size: 13px;
    float: right;
}

.chat_ib p {
    font-size: 14px;
    color: #989898;
    margin: auto
}

.incoming_msg_img {
    display: inline-block;
    width: 6%;
}

.received_msg {
    display: inline-block;
    padding: 0 0 0 10px;
    vertical-align: top;
    width: 92%;
}

.received_withd_msg p {
    background: #ebebeb none repeat scroll 0 0;
    border-radius: 3px;
    color: #646464;
    font-size: 14px;
    margin: 0;
    padding: 5px 10px 5px 12px;
    width: 100%;
}

.time_date {
    color: #747474;
    display: block;
    font-size: 12px;
    margin: 8px 0 0;
}

.received_withd_msg {
    width: 57%;
}

.mesgs {
    padding: 30px 15px 0 25px;
}

.sent_msg p {
    background: #05728f none repeat scroll 0 0;
    border-radius: 3px;
    font-size: 14px;
    margin: 0;
    color: #fff;
    padding: 5px 10px 5px 12px;
    width: 100%;
}

.outgoing_msg {
    overflow: hidden;
    margin: 26px 0 26px;
}

.sent_msg {
    float: right;
    width: 46%;
}

.input_msg_write input {
    background: rgba(0, 0, 0, 0) none repeat scroll 0 0;
    border: medium none;
    color: #4c4c4c;
    font-size: 15px;
    min-height: 48px;
    width: 100%;
}

.type_msg {
    border-top: 1px solid #c4c4c4;
    position: relative;
}

.msg_send_btn {
    background: #05728f none repeat scroll 0 0;
    border: medium none;
    border-radius: 50%;
    color: #fff;
    cursor: pointer;
    font-size: 17px;
    height: 33px;
    position: absolute;
    right: 0;
    top: 11px;
    width: 33px;
}

.msg_history {
    height: 516px;
    overflow-y: auto;
}
</style>
