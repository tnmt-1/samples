var app = new Vue({
    el: '#app',
    data: {
        email: '',
        username: '',
        error: {}
    },
    watch: {
        // watch に指定するメソッド名は data のプロパティ名に依存します
        email: function (value) {
            if (value === '') {
                this.error.email = 'メールアドレスは必須です。'
            } else if (!/[a-zA-Z0-9]+/.test(value)) {
                this.error.email = 'メールアドレスは半角英数のみです。'
            } else {
                this.error.email = ''
            }
        },
        username: function (value) {
            if (value === '') {
                this.error.username = 'ユーザー名は必須です。'
            } else if (!/[a-zA-Z0-9]+/.test(value)) {
                this.error.username = 'ユーザー名は半角英数のみです。'
            } else {
                this.error.username = ''
            }
        }
    }
})
