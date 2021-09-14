import store from '@/store/index'
import dayjs from 'dayjs';
import 'dayjs/locale/ko';
import localizedFormat from 'dayjs/plugin/localizedFormat';

dayjs.locale(store.getters['lang/get_lang']);
dayjs.extend(localizedFormat);
