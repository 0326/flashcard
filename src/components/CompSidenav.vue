<template>
  <md-sidenav class="md-left" ref="leftSidenav" @open="open('Left')" @close="close('Left')">
    <md-toolbar class="md-large">
        <div class="md-toolbar-container">
          <h3 class="md-title">动感小前端</h3>
        </div>
        <p>动次打次</p>
    </md-toolbar>
    <md-list>
      <md-list-item>
        <md-icon>move_to_inbox</md-icon> <span>卡牌广场</span>
      </md-list-item>

      <md-list-item>
        <md-icon>send</md-icon> <span>决斗大厅</span>
      </md-list-item>

      <md-list-item>
        <md-icon>delete</md-icon> <span>我的卡牌</span>
      </md-list-item>

      <md-list-item>
        <md-icon>delete</md-icon> <span>我的卡包</span>
      </md-list-item>

      <md-list-item>
        <md-icon>delete</md-icon> <span>我的成就</span>
        <md-divider class="md-inset"></md-divider>
      </md-list-item>

      <md-list-item>
        <md-icon>delete</md-icon> <span>设置</span>
      </md-list-item>

      <md-list-item>
        <md-icon>delete</md-icon> <span>帮助</span>
      </md-list-item>
    </md-list>
    <div class="footer">
      <p>问题反馈</p>
      <p>参与贡献</p>
      <p>作者：0326</p>
    </div>
  </md-sidenav>
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
<style lang="less">
  .md-sidenav {
    .md-sidenav-content{
      position: fixed;
      z-index: 9999;
    }
    .md-toolbar-container {
      color: #FFF;
    }
  }
</style>
