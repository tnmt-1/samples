var app = new Vue({
    el: '#app',
    data: {
      birthday: '1988-02-20',
      isComputedCalled: false,
      isComputedCalled2: false,
      left: 0,
      right: 0,
    },
    methods: {
      // この関数が呼び出されたタイミングがわかるように
      // メッセージを表示させる
      setMessage: function () {
        // メッセージを表示
        this.isComputedCalled = true
        const that = this
        setTimeout(function () {
            that.isComputedCalled = false
        }, 2000) // 2秒後にメッセージが消えます
      },
      setMessage2: function () {
        // メッセージを表示
        this.isComputedCalled2 = true
        const that = this
        setTimeout(function () {
            that.isComputedCalled2 = false
        }, 2000) // 2秒後にメッセージが消えます
      }
    },
    computed: {
      age: function () {
        this.setMessage()

        // 誕生日の値が入っていなければマイナスの値を返却する
        // マイナスの場合の表示はテンプレート側で制御する
        if (!this.birthday) {
          return -1
        }

        // 日付の計算にはmoment.jsというライブラリを使う
        moment.locale('ja')
        return moment().diff(this.birthday, 'years')
      },
      total: function () {
        this.setMessage2()

        return this.left + this.right
      }
    }
})
