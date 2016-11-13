
<style lang="less" scoped>
  #app {
    padding-top: 76px;
  }
  .md-toolbar {
    position: fixed;
    top: 0;
    width: 100%;
    min-width: 990px;
    z-index: 1001;

    .md-icon-button{
      color: #FFF;
    }
  }
  .md-title {
    p{
      display: inline-block;
      margin-right: 16px;
      color: #FFF;
    }
    .main {
      font-weight: bold;
    }
    .sub{
      border-left: 1px solid #FFF;
      padding-left: 16px;
    }
  }
  .hd-search {
    flex: 1;
    padding: 0 32px;
    label {
      top: 21px;
      left: 6px;
    }
    span {
      vertical-align: middle;
    }
    .md-input-container:after {
      display: none;
    }
    .md-input {
      padding-left: 6px;
      background: rgba(255,255,255,.7);
      border-radius: 3px;
    }
  }
  .new-card-fab {
    position: fixed;
    right: 16px;
    bottom: 16px;
  }
  footer {
    padding: 20px;
    text-align: center;
  }
</style>
<template>
  <div id="app" v-md-theme="'vgreen'">
    <!--导航工具栏-->
    <md-toolbar>
      <md-button class="md-icon-button" @click="toggleLeftSidenav">
        <md-icon>menu</md-icon>
      </md-button>

      <div class="md-title">
        <p class="main">FlashCard+</p>
        <p class="sub">首页</p>
      </div>

      <div class="hd-search">
        <md-input-container md-inline>
          <label><md-icon>search</md-icon><span>Search</span></label>
          <md-input></md-input>
        </md-input-container>
      </div>

      <md-button class="md-icon-button">
        <md-icon>favorite</md-icon>
      </md-button>
      <md-button class="md-icon-button">
        <md-icon>favorite</md-icon>
      </md-button>
      <md-avatar>
        <img src="./assets/yoona.jpg" alt="People">
      </md-avatar>
    </md-toolbar>

    <!--侧边菜单栏-->
   <comp-sidenav :show-left-sidenav="showLeftSidenav"></comp-sidenav>

    <!--FlashCard Tabs切换模块-->
    <comp-card-tabs></comp-card-tabs>

    <!--新增flash按钮-->
    <md-button class="md-fab new-card-fab">
      <md-icon>edit</md-icon>
    </md-button>

    <footer>
      <p>© 2016 FlashCard, @0326. </p>
    </footer>
  </div>
</template>

<script>
import CompCardlist from './components/CompCardlist'
import CompCardTabs from './components/CompCardTabs'
import CompSidenav from './components/CompSidenav'

export default {
  name: 'app',
  data () {
    return {
      showLeftSidenav: false
    }
  },
  components: {
    CompCardlist,
    CompCardTabs,
    CompSidenav
  },
  methods: {
    toggleLeftSidenav () {
      this.showLeftSidenav = !this.showLeftSidenav
    }
  }
}
</script>

