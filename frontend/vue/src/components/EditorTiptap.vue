<template>
    <div class="editor">
        <editor-menu-bar :editor="editor" v-slot="{ commands, isActive }">
            <div class="menubar">
                <button class="menubar__button" :class="{ 'is-active': isActive.bold() }" @click="commands.bold">
                    <i class="fas fa-bold"></i>
                </button>
                <button class="menubar__button" :class="{ 'is-active': isActive.italic() }" @click="commands.italic">
                    <i class="fas fa-italic"></i>
                </button>
                <button class="menubar__button" :class="{ 'is-active': isActive.strike() }" @click="commands.strike">
                    <i class="fas fa-strikethrough"></i>
                </button>
                <button class="menubar__button" :class="{ 'is-active': isActive.underline() }" @click="commands.underline">
                    <i class="fas fa-underline"></i>
                </button>
                <button class="menubar__button" :class="{ 'is-active': isActive.code() }" @click="commands.code">
                    <i class="fas fa-code"></i>
                </button>
                <button class="menubar__button" @click="showImagePrompt(commands.image)">
                    <i class="far fa-image"></i>
                </button>
                <button class="menubar__button" :class="{ 'is-active': isActive.paragraph() }" @click="commands.paragraph">
                    <i class="fas fa-paragraph"></i>
                </button>
                <button class="menubar__button" :class="{ 'is-active': isActive.heading({ level: 1 }) }" @click="commands.heading({ level: 1 })">
                    H1
                </button>
                <button class="menubar__button" :class="{ 'is-active': isActive.heading({ level: 2 }) }" @click="commands.heading({ level: 2 })">
                    H2
                </button>
                <button class="menubar__button" :class="{ 'is-active': isActive.heading({ level: 3 }) }" @click="commands.heading({ level: 3 })">
                    H3
                </button>
                <button class="menubar__button" :class="{ 'is-active': isActive.bullet_list() }" @click="commands.bullet_list">
                    <i class="fas fa-list-ul"></i>
                </button>
                <button class="menubar__button" :class="{ 'is-active': isActive.ordered_list() }" @click="commands.ordered_list">
                    <i class="fas fa-list-ol"></i>
                </button>
                <button class="menubar__button" :class="{ 'is-active': isActive.blockquote() }" @click="commands.blockquote">
                    <i class="fas fa-quote-right"></i>
                </button>
                <button class="menubar__button" :class="{ 'is-active': isActive.code_block() }" @click="commands.code_block">
                    <i class="fas fa-code"></i>
                </button>
                <button class="menubar__button" @click="commands.horizontal_rule">
                    <i class="fas fa-minus"></i>
                </button>
                <button class="menubar__button" @click="commands.undo">
                    <i class="fas fa-undo"></i>
                </button>
                <button class="menubar__button" @click="commands.redo">
                    <i class="fas fa-redo"></i>
                </button>
            </div>
        </editor-menu-bar>
        <editor-menu-bubble class="menububble" :editor="editor" @hide="hideLinkMenu" v-slot="{ commands, isActive, getMarkAttrs, menu }">
            <div class="menububble" :class="{ 'is-active': menu.isActive }" :style="`left: ${menu.left}px; bottom: ${menu.bottom}px;`">
                <form class="menububble__form" v-if="linkMenuIsActive" @submit.prevent="setLinkUrl(commands.link, linkUrl)">
                    <input class="menububble__input" type="text" v-model="linkUrl" placeholder="https://" ref="linkInput" @keydown.esc="hideLinkMenu"/>
                    <button class="menububble__button" @click="setLinkUrl(commands.link, null)" type="button">
                        <i class="fas fa-trash"></i>
                    </button>
                </form>

                <template v-else>
                    <button class="menububble__button" @click="showLinkMenu(getMarkAttrs('link'))" :class="{ 'is-active': isActive.link() }">
                        <span>{{ isActive.link() ? 'Update Link' : 'Add Link' }}</span>
                        <i class="fas fa-link"></i>
                    </button>
                </template>
            </div>
        </editor-menu-bubble>
        <editor-content class="editor__content" :editor="editor"/>
    </div>
</template>

<script>
import {Editor, EditorContent, EditorMenuBar, EditorMenuBubble} from 'tiptap';
import {Blockquote, CodeBlock, HardBreak, Image, Heading, HorizontalRule, OrderedList, BulletList, ListItem, TodoItem, TodoList, Bold, Code, Italic, Link, Strike, Underline, History, Placeholder} from 'tiptap-extensions';

export default {
    components: {
        EditorContent,
        EditorMenuBar,
        EditorMenuBubble
    },
    data() {
        return {
            editor: new Editor({
                extensions: [
                    new Blockquote(),
                    new BulletList(),
                    new CodeBlock(),
                    new HardBreak(),
                    new Image(),
                    new Heading({levels: [1, 2, 3]}),
                    new HorizontalRule(),
                    new ListItem(),
                    new OrderedList(),
                    new TodoItem(),
                    new TodoList(),
                    new Link(),
                    new Bold(),
                    new Code(),
                    new Italic(),
                    new Strike(),
                    new Underline(),
                    new History(),
                    new Placeholder({
                        emptyEditorClass: 'is-editor-empty',
                        emptyNodeClass: 'is-empty',
                        emptyNodeText: this.$t('Please enter your contents. (20000 characters or less)'),
                        showOnlyWhenEditable: true,
                        showOnlyCurrent: true
                    })
                ]
            }),
            linkUrl: null,
            linkMenuIsActive: false
        };
    },
    methods: {
        showLinkMenu(attrs) {
            this.linkUrl = attrs.href;
            this.linkMenuIsActive = true;
            this.$nextTick(() => {
                this.$refs.linkInput.focus();
            });
        },
        hideLinkMenu() {
            this.linkUrl = null;
            this.linkMenuIsActive = false;
        },
        setLinkUrl(command, url) {
            command({href: url});
            this.hideLinkMenu();
        },
        showImagePrompt(command) {
            const src = prompt('Enter the url of your image here')
            if (src !== null) {
                command({src})
            }
        },
    },
    beforeDestroy() {
        this.editor.destroy();
    }
};
</script>
<style lang="scss">
.editor p.is-editor-empty:first-child::before {
    content: attr(data-empty-text);
    float: left;
    color: #aaa;
    pointer-events: none;
    height: 0;
    font-style: italic;
}
</style>
