<template>
    <div class="row background">
        <div class="container post post-padding">
            <div class="card mt-3">
                <div class="card-body">
                    <div class="row">
                        <div class="col-lg-4 col-md-6 col-12">
                            <div class="container">
                                <div class="row">
                                    <h5 class="w-25 text-left">
                                        <span class="badge badge-secondary">{{ $t('Date') }}</span>
                                    </h5>
                                    <div class="col-9">
                                        <input type="text" id="id_local_datetime" name="local_datetime" class="form-control form-control-sm" v-model="today"/>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-4 col-md-6 col-12">
                            <div class="container">
                                <div class="row">
                                    <h5 class="w-25 text-left">
                                        <span class="badge badge-secondary">{{ $t('Username') }}</span>
                                    </h5>
                                    <div class="col-xl-9 col-lg-8 col-md-9 col-9">
                                        <input type="text" id="id_username" name="username" class="form-control form-control-sm" required/>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-4 col-md-6 col-12">
                            <div class="container">
                                <div class="row">
                                    <h5 class="w-25 text-left">
                                        <span class="badge badge-secondary">{{ $t('Category') }}</span>
                                    </h5>
                                    <div class="col-9">
                                        <select name="category" id="id_category" class="form-control form-control-sm" v-model="category_code" required>
                                            <option value="">--- {{ $t('Please choose') }} ---</option>
                                            <option v-for="category in category_list" :key="category.code">
                                                {{ $t(category.name) }}
                                            </option>
                                        </select>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-lg-4 col-md-6 col-12">
                            <div class="container">
                                <div class="row">
                                    <h5 class="w-25 text-left">
                                        <span class="badge badge-secondary">{{ $t('Subject') }}</span>
                                    </h5>
                                    <div class="col-9">
                                        <input type="text" id="id_subject" name="subject" class="form-control form-control-sm" :placeholder="$t('Please enter a subject. (300 characters or less)')" required/>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-4 col-md-12 col-12">
                            <div class="container">
                                <div class="row">
                                    <h5>
                                        <span class="badge badge-secondary">{{ $t('Reply') }}</span>
                                        <span class="badge badge-info"></span>
                                        <span class="badge badge-secondary">{{ $t('Lookup') }}</span>
                                        <span class="badge badge-info"></span>
                                    </h5>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-4 col-md-12 col-12">
                            <div class="container">
                                <div class="row">
                                    <h5>
                                        <span class="badge badge-secondary">{{ $t('Recommend') }}</span>
                                        <span class="badge badge-info"></span>
                                    </h5>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <editor
                api-key="p453mc03irhw5ur9757lryy6q5l0yh1kkn8451225emn3v7n"
                :init=editor_init
            />
        </div>
    </div>
</template>

<script>
import dayjs from 'dayjs';
import Editor from '@tinymce/tinymce-vue'

export default {
    name: 'Post',
    components: {
        'editor': Editor
    },
    data() {
        return {
            editor_init: {
                language: 'ko_KR',
                height: 500,
                menubar: true,
                plugins: [
                    'advlist autolink lists link image charmap print preview anchor',
                    'searchreplace visualblocks code fullscreen',
                    'insertdatetime media table paste code help wordcount'
                ],
                toolbar:
                    'undo redo | formatselect | bold italic backcolor | \
                    alignleft aligncenter alignright alignjustify | \
                    bullist numlist outdent indent | removeformat | help'
            },
            today: dayjs().format('YYYY-MM-DD'),
            category_code: '',
            category_list: this.$store.state.board.category_list
        };
    }
};
</script>

<style scoped>
.background {
    background-color: #eee;
}

.post-padding {
    padding-top: 55px;
    margin-bottom: 30px;
}
</style>
