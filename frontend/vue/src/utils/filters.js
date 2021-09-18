import Vue from 'vue';
import dayjs from 'dayjs';

Vue.filter('local_time', (date) => {
    if (!date) {
        return '';
    }
    return dayjs(date).format('LLL');
});
