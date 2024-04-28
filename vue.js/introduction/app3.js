var app = new Vue({
    el: '#app',
    data: {
      messages: [
        { text: 'This is normal message.', error: false },
        { text: 'This is ERROR message!', error: true },
      ],
      progress: 70
    }
})
