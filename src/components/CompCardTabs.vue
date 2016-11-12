<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="less">
  .md-tabs {
    .md-tabs-navigation {
      overflow-x: scroll;
      overflow-y: hidden;
    }
    .md-tab-header {
      min-width: 120px;
      span{
        width: 100%;
        text-overflow: ellipsis;
        overflow: hidden;
      }
    }
  }
</style>

<template>
  <md-tabs md-fixed v-md-theme="'green'">
    <md-tab id="movies" md-label="Movies">
      <comp-card-list></comp-card-list>
    </md-tab>

    <md-tab id="music" md-label="Music">
      <comp-card-list></comp-card-list>
    </md-tab>

    <md-tab id="books" md-label="Books">
     <comp-card-list></comp-card-list>
    </md-tab>

    <md-tab id="music1" md-label="Music1">
      <comp-card-list></comp-card-list>
    </md-tab>

    <md-tab id="books1" md-label="Books1sssssssssssssssssssssssssssssss">
     <comp-card-list></comp-card-list>
    </md-tab>

    <md-tab id="music2" md-label="Music2">
      <comp-card-list></comp-card-list>
    </md-tab>

    <md-tab id="books2" md-label="Books2">
     <comp-card-list></comp-card-list>
    </md-tab>

    <md-tab id="pictures" md-label="Pictures">
     <comp-card-list></comp-card-list>
    </md-tab>
  </md-tabs>
</template>

<script>
  import CompCardList from './CompCardList'
  export default {
    name: 'hello',
    components: {
      CompCardList
    },
    data () {
      return {
        msg: 'Welcome to Your Vue.js App'
      }
    }
  }
</script>
