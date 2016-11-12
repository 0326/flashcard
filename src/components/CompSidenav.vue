<template>
  <div class="card-ctr">
    <md-sidenav class="md-left" ref="leftSidenav" @open="open('Left')" @close="close('Left')">
      <md-toolbar class="md-large">
        <div class="md-toolbar-container">
          <h3 class="md-title">Sidenav content</h3>
        </div>
      </md-toolbar>
      <md-list>
        <md-list-item>
          <md-icon>move_to_inbox</md-icon> <span>Inbox</span>
        </md-list-item>

        <md-list-item>
          <md-icon>send</md-icon> <span>Sent Mail</span>
        </md-list-item>

        <md-list-item>
          <md-icon>delete</md-icon> <span>Trash</span>
        </md-list-item>
      </md-list>
      <div class="footer">
        <p>返回传统版 Google+</p>
        <p>隐私权政策 - 服务条款 - 地图条款</p>
      </div>
    </md-sidenav>
  </div>
</template>

<script>
export default {
  name: 'CompSidenav',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  props: {
    showLeftSidenav: {
      type: Boolean,
      required: true
    }
  },
  watch: {
    showLeftSidenav: function (val, oldVal) {
      console.log('sidenav', val)
      this.$refs.leftSidenav.toggle()
    }
  },
  methods: {
    toggleLeftSidenav () {
      this.$refs.leftSidenav.toggle()
    },
    open (ref) {
      console.log('Opened: ' + ref)
    },
    close (ref) {
      console.log('Closed: ' + ref)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.footer {
  padding: 16px;
}
</style>
